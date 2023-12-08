from os import getenv
import shimoku_api_python as Shimoku
import pandas as pd



access_token = getenv('API_TOKEN')
universe_id: str = getenv('UNIVERSE_ID')
workspace_id: str = getenv('WORKSPACE_ID')

API_TOKEN='8e596480-dd4c-483d-8802-dad88cf9694f'
UNIVERSE_ID='887ce08e-c68b-4fd1-ac86-201fee9c85dd'
WORKSPACE_ID='69637c67-abdc-416f-b342-bac6cddc223a'


s = Shimoku.Client(
    access_token=API_TOKEN,
    universe_id=UNIVERSE_ID,
    verbosity='INFO',
    async_execution=True,
)

try:
    s.set_workspace(WORKSPACE_ID)
except Exception as e:
    print(e)

try:
    s.set_board('Custom b')
except Exception as e:
    print(e)

try:
    s.set_menu_path('catalog', 'bar-example')
except Exception as e:
    print(e)

leads= pd.read_excel('output.xlsx')

try:
    s.plt.bar(
        order=0, title='Use Case for Converted',
        data=leads, x='Use Case',
        y=['Converted'],
    )
except Exception as e:
    print(e)

s.run()