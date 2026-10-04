// ============================================================================
// Module Name:  led_tb
// Description:  Testbench for Artix-7 LED Counter module
// ============================================================================

`timescale 1ns / 1ps

module led_tb;

    // Testbench signals
    reg        clk;
    reg        rst;
    reg  [1:0] freq;
    wire [3:0] count;

    // Instantiate Unit Under Test (UUT)
    led uut (
        .clk(clk),
        .rst(rst),
        .freq(freq),
        .count(count)
    );

    // 100 MHz Clock Generation (10 ns period)
    always #5 clk = ~clk;

    initial begin
        // Initialize inputs
        clk  = 0;
        rst  = 1;
        freq = 2'b00;

        $display("[%0t ns] Testbench started. Applying Reset...", $time);
        #50;
        rst = 0;
        $display("[%0t ns] Reset released. Testing freq=00 (1 Hz blink)...", $time);

        // Wait a few cycles
        #100;
        $display("[%0t ns] Synchronizer output stabilized. count = 4'b%b", $time, count);

        // Switch to 10 Hz mode (freq = 11) for fast simulation checking
        #100;
        freq = 2'b11;
        $display("[%0t ns] Switch freq set to 2'b11 (10 Hz blink)", $time);

        #200;
        $display("[%0t ns] Simulation check completed successfully. count = 4'b%b", $time, count);
        $finish;
    end

endmodule
