import scrapy

classe = ['MD82', 'MD83', 'MD87', 'MD88', 'MD90', 'MG21', 'MG23', 'MG25', 'MG29', 'MG31',
          'MI2', 'MI8', 'MIR2', 'MRF1', 'MU2', 'N262', 'NH90', 'NIM', 'P180', 'P28A',
          'P28R', 'P28T', 'P3', 'P32R', 'P46T', 'P808', 'PA18', 'PA23', 'PA27', 'PA31',
          'PA32', 'PA34', 'PA38', 'PA44', 'PA46', 'PAY2', 'PAY3', 'PAY4', 'PC12', 'PC6T',
          'PC7', 'PC9', 'PRM1', 'PZ04', 'R135', 'R44', 'RALL', 'RJ1H', 'RJ70', 'RJ85',
          'S601', 'S61', 'S76', 'SB05', 'SB20', 'SB32', 'SB37', 'SB39', 'SBR2', 'SC7',
          'SF34', 'SH33', 'SH36', 'SR20', 'SR22', 'SU17', 'SU24', 'SU25', 'SU27', 'SU95',
          'SW2', 'SW3', 'SW4', 'T134', 'T154', 'T204', 'T22M', 'T37', 'T38', 'TAMP',
          'TB30', 'TBM7', 'TBM8', 'TOBA', 'TOR', 'TRIN', 'TUCA', 'UH1', 'VC10', 'YK40',
          'YK42']


class TesteSpider(scrapy.Spider):
    name = "teste"

    def start_requests(self):
        for tipo in classe:
            yield scrapy.Request(f"https://contentzone.eurocontrol.int/aircraftperformance/details.aspx?ICAO={tipo}")

    def parse(self, response, **kwargs):
        yield {
            'ICAO': response.css('#MainContent_wsICAOLabel::text').get(),
            'V2IAS': response.css('#wsV2Literal::text').get(),
            'DistDEPRWY': response.css('#wsFARTOLiteral::text').get(),
            'WTC': response.css('#wsWTCLiteral::text').get(),
            'RECAT-EU': response.css('#wsRECATLiteral::text').get(),
            'MTOW': response.css('#wsMTOWLiteral::text').get(),
            'VelIAS5000FT': response.css('#wsINVCLLiteral::text').get(),
            'RazSub5000FT': response.css('#wsINROCLiteral::text').get(),
            'VelIASFL150': response.css('#wsIASVCLLiteral::text').get(),
            'RazSubFL150': response.css('#wsIASROCLiteral::text').get(),
            'VelIASFL240': response.css('#wsIASVCLLiteral2::text').get(),
            'RazSubFL240': response.css('#wsIASROC2Literal::text').get(),
            'machSubCruz': response.css('#wsMACHVCLLiteral::text').get(),
            'RazSubCruz': response.css('#wsMACHROCLiteral::text').get(),
            'VelTASCruzKT': response.css('#wsVCSknotsLiteral::text').get(),
            'VelCruzMach': response.css('#wsVCSmachLiteral::text').get(),
            'FLmax': response.css('#wsCeilingLiteral::text').get(),
            'Range': response.css('#wsRangeLiteral::text').get(),
            'MachDescFL240': response.css('#wsMACHVDESCLiteral::text').get(),
            'RazDescFL240': response.css('#wsMACHRODLiteral::text').get(),
            'VelIASDescFL100': response.css('#wsIASVDESCLiteral::text').get(),
            'RazDescFL100': response.css('#wsIASRODLiteral::text').get(),
            'VelIASARR': response.css('#wsBelowVDESCLiteral::text').get(),
            'RazARR': response.css('#wsBelowRODLiteral::text').get(),
            'MCS': response.css('#wsMCSLiteral::text').get(),
            'VelIASPouso': response.css('#wsVTHLiteral::text').get(),
            'DistPousoRWY': response.css('#wsFARLDLiteral::text').get(),
            'APC': response.css('#wsAPCLiteral::text').get(),
        }