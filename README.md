#  Figuring out what part of internet is broken.

This project begun as I was snowed in for a couple of days, along with a couple millions other people on the east coast
in 2016. Seeing the my IPS' network brought down to the knees by literally every one on it's networks streaming youtube,
netflix and a couple of music services, all at the same time.

This tool relies on the system's traceroute and requires numpy, matplotlib and click. Use at your own risk.
For now works on Windows only

License is BDS-3 clause.

Usage:
``` 
    statstrace trace youtube.com
```

Returns:
![Output Example](http://i.imgur.com/Kt2b0rh.png)

All rights reserved,
Andrei Kucharavy 2016