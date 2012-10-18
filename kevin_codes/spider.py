from harvestman.apps.spider import HarvestMan

spider = HarvestMan()
spider.init()

cfg = spider.get_config()
cfg.add(url='http://docs.python.org/tutorial/index.html',name='sample_crawl',basedir='~/sample_crawl_dir')
cfg.setup()

spider.main()