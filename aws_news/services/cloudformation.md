# deletionpolicy_attribute_options

- delete = default except for rds
- retain = resource remains after stack is deleted
- snapshot = creates backup for EBS/elasticache/rods/redshift resources 

# cloudformation_sections
- version, description, parameters, resources (only required section), outputs
- metadata = arbitrary JSON or yaml that provides additional configuration to the template

- rules = validates parameters against logical expressions you define

- mappings = key value pairs that can be looked up for conditionals

- conditions = controls whether certain cloudformation resources or properties are set based on Boolean logic typically from parameters

- transforms = aws Sam or ```aws::include``` to include aribitrary cloudformation stored outside of your template 
