# Computing-geopotential-on-model-levels
Computing geopotential on model levels
The geopotential height (**gh**) provided by ECMWF is only provided at model level 1. This is the geopotential height of the surface. ECMWF does not provide **gh** on other levels because it is relatively simple to compute from other parameters (temperature, specific humidity and surface pressure) and saves ECMWF some storage space.

ECMWF provide Python script **compute–geopotential−on−ml.py** which we can use to calculate **gh** at all other model levels. This is available from: [[https://confluence.ecmwf.int/display/MSAPP/Geopotential+height+on+model+levels]]

We need to retrieve in GRIB format both temperature (t) and specific humidity (q) for each model level. Besides, we need both surface geopotential (z) and logarithm of surface pressure (**lnsp**) for model level = 1. If we do this on the Atos using MARS retrieval, we can use **compute–geopotential−on−ml.ksh**.

An important detail is that in the compute script provided by ECMWF **geopotential-on-ml.ksh** by default, data is retrieved for **type=”an”** and **step=0**, but in our case we have to change this to **type=”fc”** and **step=0/to/144/by/3**.

But to get these parameters we can also use EPDM un PREd.

In addition, we also retrieve some other parameters of the model levels here: U component of wind (**u**), V component of wind (**v**), Vertical velocity (**w**), Fraction of cloud cover (**cc**), Specific cloud liquid water content (**clwc**).
For example, we can use PREd WA feed. In this case, the names of the files from the gribs/ folder on ftp server begin with the letters “WA”

Each file contains parameters **t**, **q**, **z**, **lnsp**, **u**, **v**, **w**, **cc**, **clwc** for different steps.
The basic idea is that to calculate **gh** for all levels 137, we need to extract the geopotential, the natural logarithm of pressure,
temperature and specific humidity from each file, and then combine each parameter into one file.
It means that we will get files containing the parameters **t**, **q**, **z**, **lnsp** for all steps.
After that we merge the files with the parameters **t** and **q** to get **tq−ml.grib** and the parameters **z**, **lnsp** to get **zlnsp−ml.grib**.
These files we use as parameters in the file **compute−geopotential−on−ml.py** which compute **gh** for all model levels.
