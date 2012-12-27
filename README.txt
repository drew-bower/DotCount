Tasks:

1.) Make a directory in HDFS
2.) Copy the data files into HDFS
3.) Modify the mapper key to "lat,lon" (the default value of 1 can stay the same)
4.) Run locally on one of the data files.
5.) See if there is any grouping (i.e. if count is greater than 1)
6.) Determine if the mapper key needs to be adjusted to promote more grouping
7.) Implement the change
8.) Take a peek at my mapper file to see how I implemented a 1 arc second geohash
9.) Run in HDFS, compare to the runtime in the local file system.
