@Library('SharedPipelines@main')


def pipelineConfig = [
    projectKey: 'nlp_model_app',
    projectName: 'nlp_model_app',
    sourcePath : '.'
]


def dataPipeline = new AppDataPipeline(pipelineConfig)
dataPipeline.pipeline()