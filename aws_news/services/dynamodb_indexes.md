- global secondary index = different partition and sort key than the primary table
  - Only attributes that can be queried are those that are projected in advance
  - index key does not need to be composed of any of the key attributes from the primary table 

- local secondary index = same partition key, different sort key as the primary table
  - All attributes in the primary table can be returned in a query/scan