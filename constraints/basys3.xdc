## ============================================================================
## Constraints File for Digilent Basys 3 (XC7A35TCPG236-1)
## ============================================================================

## 100 MHz Clock Signal
set_property -dict { PACKAGE_PIN W5    IOSTANDARD LVCMOS33 } [get_ports { clk }];
create_clock -add -name sys_clk_pin -period 10.00 -waveform {0 5} [get_ports { clk }];

## Active-High Reset (Button U)
set_property -dict { PACKAGE_PIN U18   IOSTANDARD LVCMOS33 } [get_ports { rst }];

## Speed Select Switches (SW0, SW1)
set_property -dict { PACKAGE_PIN V17   IOSTANDARD LVCMOS33 } [get_ports { freq[0] }];
set_property -dict { PACKAGE_PIN V16   IOSTANDARD LVCMOS33 } [get_ports { freq[1] }];

## 4-Bit LED Counter Output (LED0 - LED3)
set_property -dict { PACKAGE_PIN U16   IOSTANDARD LVCMOS33 } [get_ports { count[0] }];
set_property -dict { PACKAGE_PIN E19   IOSTANDARD LVCMOS33 } [get_ports { count[1] }];
set_property -dict { PACKAGE_PIN U19   IOSTANDARD LVCMOS33 } [get_ports { count[2] }];
set_property -dict { PACKAGE_PIN V19   IOSTANDARD LVCMOS33 } [get_ports { count[3] }];

## Configuration Voltage Settings
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 3.3 [current_design]
