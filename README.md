# RPM Validator

This is a simple test to verify that the files output in the build-system are
valid RPM format files. Currently, this performs only two simple tests:
1) Verify that the file can be parsed as an RPM
2) Verify that the RPM header lists only files in locations permitted by the
   Filesystem Hierarchy Standard (version 3.0):
   http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html
