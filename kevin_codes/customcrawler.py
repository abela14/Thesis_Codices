from harvestman.apps.spider import HarvestMan
from harvestman.lib.common.macros import *

class MyCustomCrawler(HarvestMan):
    """ A custom crawler """

    size_threshold = 4096

    def save_this_url(self, event, *args, **kwargs):
        """ Custom callback function which modifies behaviour
            of saving URLs to disk """

        # Get the url object
        url = event.url
        # If not image, save always
        if not url.is_image():
            return True
        else:
            # If image, check for content-length > 4K
            size = url.clength
            return (size>self.size_threshold)

# Set up the custom crawler
if __name__ == "__main__":
    crawler = MyCustomCrawler()
    crawler.initialize()
    # Get the configuration object
    config = crawler.get_config()
    # Register for 'save_url_data' event which will be called
    # back just before a URL is saved to disk
    crawler.register('save_url_data', crawler.save_this_url)
    # Run
    crawler.main()