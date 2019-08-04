#Show raw data from mouse
mouse = file('/dev/input/mouse0')
while True:
    status, dx, dy = tuple(ord(c) for c in mouse.read(3))

    def to_signed(n):
        return n - ((0x80 &amp; n) &lt;&lt; 1)
        
    dx = to_signed(dx)
    dy = to_signed(dy)
    print "%#02x %d %d" % (status, dx, dy)

#changes to be done for python3
#mouse = open(‘/dev/input/mouse3’, ‘rb’)  
#and the tuple line to  
#status, dx, dy = tuple(c for c in mouse.read(3))
