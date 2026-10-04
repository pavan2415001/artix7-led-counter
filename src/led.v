`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 29.09.2026 11:06:30
// Design Name: 
// Module Name: led
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module led(
    input clk,
    input [1:0] freq,
    output reg [3:0] count  
);

reg clkf=0;
reg [25:0]countr;
reg [25:0]limit;
initial begin
count<=4'b00000;
countr=25'd0;
end
always @(*)begin
case(freq)
 2'b00:limit=26'd49999999;
 2'b01:limit=26'd24999999;
 2'b10:limit=26'd9999999;
 2'b11:limit=26'd4999999;
 default:limit=26'd49999999;
 endcase
 end
 always@(posedge clk) begin
 if (countr>=limit) begin
 countr<=0;
 clkf<=~clkf;
 end
 else begin
 countr<=countr+1;
 end
 end
always@(posedge clkf) begin
count<=count+1;
end
endmodule
