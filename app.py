# FastAPI / Flask app entry point

from prefect import task, flow

@task
def extract():
    return [1, 2, 3, s]

@task
def transform(data):
    return [x * 2 for x in data]

@task
def load(data):
    print('Loaded: ', data)
    
@flow
def mypipeline():
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)
    
if __name__ == '__main__':
    mypipeline()