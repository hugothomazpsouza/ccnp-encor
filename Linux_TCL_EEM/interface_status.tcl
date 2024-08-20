tclsh
# Script to check the status of all interfaces
puts "Checking status of all interfaces:"

set output [exec "show ip interface brief"]

# Parse the output to find interfaces that are down
foreach line [split $output "\n"] {
    if {[regexp {([A-Za-z0-9/]+)\s+([0-9.]+)\s+\w+\s+\w+\s+(\w+)\s+(\w+)} $line match interface ip status protocol]} {
        if {$status == "down" || $protocol == "down"} {
            puts "Interface $interface is down"
        }
    }
}
