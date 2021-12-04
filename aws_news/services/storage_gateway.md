1) file gateway = supports NFS and SMB stored in S3
2) tape gateway = send in tapes
3) volume gateway = iSCSI block based storage
   1) cached = most frequently access stored on-premises
   2) Entire hard drive stored on-premises with async backup to S3
   - can be used to create an ebs snapshot 