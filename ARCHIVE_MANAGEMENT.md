# Managing pywb archives

## Saving snapshots
### https://www.smgov.net/departments/clerk/agendas.aspx
For https://www.smgov.net/departments/clerk/agendas.aspx, we need need to submit a post request to
access the older agenda items. We need to add autointerval
```
wayback --record --live -a --auto-interval 15
```
## Deleting the archive and rebuilding the index
```
rm collections/smgov/archive/file.warc
rm collections/smgov/indexes/*.cdxj
wb-manager reindex
```
