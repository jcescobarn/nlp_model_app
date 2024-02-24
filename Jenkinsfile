@Library('SharedPipelines')


def pipelineConfig = {
    projectKey: "nlp_model_app",
    ProjectName: "nlp_model_app",
    sourcePath : '.'
}


def dataPipeline = new AppDataPipeline(pipelineConfig)
dataPipeline.exec()