import scrapy


class TabelogSpider(scrapy.Spider):
    name = 'tabelog.com'
    allowed_domains = ['tabelog.com']
    start_urls = ['https://tabelog.com/rstLst/cafe/']

    def parse(self, response):
        tabelog_cafes = response.xpath('//h4[@class="list-rst__rst-name"]/a')
        for cafe in tabelog_cafes:
            cafe_name = cafe.xpath('.//text()').get()
            yield {
                'cafe_name': cafe_name
            }
            cafe_detail_url = cafe.xpath('.//@href').get() + '/dtlmenu'
            yield scrapy.Request(cafe_detail_url, callback=self.parse_cafe)

        # next_page_urls = tabelog.xpath('//a[@class="c-pagination__num"]/@href').getall()
        next_page_num = 2
        next_page_url = response.urljoin(str(next_page_num))
        if next_page_url is not None:
            yield scrapy.Request(next_page_url, callback=self.parse)
            next_page_num += 1

    def parse_cafe(self, response):
        updated_at = response.xpath('//p[@class="update"]/span/text()').get()
        menu_dict = {}
        menus = response.xpath('//div[@class="rstdtl-menu-lst"]')
        menu_categories = response.xpath('//div[@class="rstdtl-menu-lst__heading"]/div/h4/text()').getall()
        menu_titles = response.xpath('//p[@class="rstdtl-menu-lst__menu-title"]/text()').getall()
        menu_images = response.xpath('//div[@class="rstdtl-menu-lst__img"]/a/img/@src').getall()
        menu_description = response.xpath('//p[@class="rstdtl-menu-lst__ex"]/text()').getall()
        menu_dict[menu_category] = {
            'name': menu_name,
            'img': menu_img,
            'description': menu_description
        }

        official_accounts = response.xpath('//div[@class="rstinfo-sns-table"]/a/@href').getall()
        opening_date = response.xpath('//p[@class="rstinfo-opened-date"]/text()').get()

        genre = response.xpath('//div[@id="rst-data-head"]/table[1]/tbody/tr[2]/td/span/text()').get()
        address = response.xpath('//p[@class="rstinfo-table__address"]/span/a/text()').getall()
        address_detail = response.xpath('//p[@class="rstinfo-table__address"]/span/text()').getall()
        nearest_station = response.xpath('//div[@id="rst-data-head"]/table[1]/tbody/tr[6]/td/p/text()').getall()
        business_hours = response.xpath('//div[@id="rst-data-head"]/table[1]/tbody/tr[7]/td/p/text()').getall()
        budget_lunch = response.xpath('//div[@class="rstinfo-table__budget"]/span/em[@class="gly-b-lunch"]/text()').get()
        budget_dinner = response.xpath('//div[@class="rstinfo-table__budget"]/span/em[@class="gly-b-dinner"]/text()').get()

        seats = response.xpath('//div[@id="rst-data-head"]/table[2]/tbody/tr[1]/td/p/text()').get()
        smoking = response.xpath('//div[@id="rst-data-head"]/table[2]/tbody/tr[4]/td/p/text()').getall()
        parking_lot = response.xpath('//div[@id="rst-data-head"]/table[2]/tbody/tr[5]/td/p/text()').getall()
        space = response.xpath('//div[@id="rst-data-head"]/table[2]/tbody/tr[6]/td/p/text()').getall()

        location = response.xpath('//div[@id="rst-data-head"]/table[4]/tbody/tr[3]/td/p/text()').getall()
        service = response.xpath('//div[@id="rst-data-head"]/table[4]/tbody/tr[4]/td/p/text()').getall()
        photos =

        yield {
            'updated_at': updated_at,
            'address': address,
            'address_detail': address_detail,
            'menu': menu_list,
        }
