@Library('SharedPipelines')


def pipelineConfig = {
    projectKey: 'nlp_model_app',
    ProjectName: 'nl_model_app',
    sourcePath : '.'
}


def dataPipeline = new AppDataPipeline(pipelineConfig)
dataPipeline.exec()