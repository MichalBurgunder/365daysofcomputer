--  Hello world program.
 use std.textio.all; --  Imports the standard textio package.

 --  Defines a design entity, without any ports.
 entity hello is
 end hello;

 architecture behaviour of hello is
 begin
    process
       variable l : line;
    begin
       write (l, String'("Hello world!"));
       writeline (output, l);
       wait;
    end process;
 end behaviour;
