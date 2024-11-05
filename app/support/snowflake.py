import time
import threading

class SnowflakeIdGenerator:
    # Fixed parameters
    # Number of bits for Machine ID
    MACHINE_ID_BITS = 10
    # Number of bits for Data Center ID (not used in this case)
    DATACENTER_ID_BITS = 0  
    # Number of bits for Sequence ID
    SEQUENCE_BITS = 12
    
    # Maximum value for Machine ID
    MAX_MACHINE_ID = -1 ^ (-1 << MACHINE_ID_BITS)
    # Maximum value for Sequence ID
    MAX_SEQUENCE = -1 ^ (-1 << SEQUENCE_BITS)
    
    # Machine ID offset
    MACHINE_ID_SHIFT = SEQUENCE_BITS
    # Timestamp offset
    TIMESTAMP_SHIFT = SEQUENCE_BITS + MACHINE_ID_BITS
    # Data Center ID offset (if used)
    DATACENTER_ID_SHIFT = TIMESTAMP_SHIFT + DATACENTER_ID_BITS
    
    # Epoch timestamp (Unix epoch time in milliseconds)
    EPOCH = 1609459200000  # 2021-01-01 00:00:00 UTC
    
    # Last generated timestamp
    last_timestamp = -1
    
    # Sequence number
    sequence = 0
    
    # Machine ID
    machine_id = 1

    # Lock for thread safety
    lock = threading.Lock()

    def __init__(self, machine_id):
        if machine_id > self.MAX_MACHINE_ID or machine_id < 0:
            raise ValueError(f"Machine ID must be between 0 and {self.MAX_MACHINE_ID}")
        self.machine_id = machine_id

    def _wait_for_next_millis(self, last_timestamp):
        """If IDs are generated within the same millisecond, wait for the next millisecond."""
        timestamp = self._current_millis()
        while timestamp <= last_timestamp:
            timestamp = self._current_millis()
        return timestamp

    def _current_millis(self):
        """Get current time in milliseconds."""
        return int(time.time() * 1000)

    def generate_id(self):
        """Generate a Snowflake ID."""
        with self.lock:
            timestamp = self._current_millis()

            if timestamp < self.last_timestamp:
                raise Exception("Clock moved backwards, refusing to generate id")

            if timestamp == self.last_timestamp:
                # Generate multiple IDs within the same millisecond
                self.sequence = (self.sequence + 1) & self.MAX_SEQUENCE
                if self.sequence == 0:
                    # If sequence overflows, wait for the next millisecond
                    timestamp = self._wait_for_next_millis(self.last_timestamp)
            else:
                # Reset sequence for a new millisecond
                self.sequence = 0

            self.last_timestamp = timestamp

            # Generate the Snowflake ID
            snowflake_id = ((timestamp - self.EPOCH) << self.TIMESTAMP_SHIFT) | \
                           (self.machine_id << self.MACHINE_ID_SHIFT) | \
                           self.sequence

            return snowflake_id

# Test generating Snowflake IDs
if __name__ == "__main__":
    # Create an ID generator with machine ID (e.g., 1)
    generator = SnowflakeIdGenerator(machine_id=1)
    
    # Generate a Snowflake ID
    snowflake_id = generator.generate_id()
    
    print(f"Generated Snowflake ID: {snowflake_id}")
