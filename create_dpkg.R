require(datasets)
require(dpmr)

print(getwd())
setwd('dpkg')

meta_list <- list(name = 'My_Data_Package',
                    title = 'A fake data package',
                    last_updated = Sys.Date(),
                    version = '0.1',
                    license = data.frame(type = 'PDDL-1.0',
                            url = 'http://opendatacommons.org/licenses/pddl/'),
                    sources = data.frame(name = 'The R Datasets Package',
                            web = 'https://stat.ethz.ch/R-manual/R-devel/library/datasets/'))

datapackage_init(df = cars, meta = meta_list)
