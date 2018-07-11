import collect
from config import CONFIG
import analyze
import visualize
import pandas as pd
import matplotlib.pyplot as plt

    # collect
if __name__ == '__main__':
    #resultfiles = dict()
    ##json  file명 저장
    # resultfiles['tourspot_visitor'] = collect.crawling_tourspot_visitor(
    #         district=CONFIG['district'],
    #         service_key = CONFIG['t_service_key'],
    #         **CONFIG['common']) # keyword를 명시하여 넘겨주는 경우 호출하는 함수에 없는 키워드는 명시할수없다.
    #
    #
    # resultfiles['foreign_visitor'] = []
    # for country in CONFIG['countries']:
    #         rf =collect.crawling_foreign_visitor(
    #         country=country,
    #         service_key=CONFIG['f_service_key'],
    #         **CONFIG['common'],
    #         )
    #         resultfiles['foreign_visitor'].append(rf)

    resultfiles ={'tourspot_visitor': '__results__/crawling/서울특별시_tourinstspot_2017_2017.json',
                  'foreign_visitor': ['__results__/crawling/중국(112)_foreignvisitor_2017_2017.json',

                                      '__results__/crawling/일본(130)_foreignvisitor_2017_2017.json',
                                      '__results__/crawling/미국(275)_foreignvisitor_2017_2017.json'],

                  }
    #1. analysis and visualize
    # print("-----------------------")
    # print(resultfiles)
    # #json file명을 dic으로 저장한 reulstfiles 전달
    # #분석한 데이터를 리스트(안에 dic)로 리턴
    # result_analysis = analyze.analysis_correlation2(resultfiles)
    # #visualize
    # visualize.graph_scatter2(result_analysis)


    #
    # 2. analysis and visualize
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)
    print(result_analysis)
    graph_table = pd.DataFrame(result_analysis, columns=('tourspot', 'r_중국', 'r_일본', 'r_미국'))
    graph_table = graph_table.set_index('tourspot')

    graph_table.plot(kind='bar')
    plt.show()
