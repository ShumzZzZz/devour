multibranchPipelineJob('Feast-CI-devour') {
  displayName('Feast-CI-devour')
  branchSources {
    branchSource {
      source {
        github {
          id('gh-mbp-devour')
          repoOwner('ShumzZzZz')
          repository('devour')
          credentialsId('githubapp-creds')
          configuredByUrl(false)
          repositoryUrl('https://github.com/ShumzZzZz/devour')
          traits {
            gitHubBranchDiscovery { strategyId(1) }

            headWildcardFilter {
              includes('main')
              excludes('')
            }

            gitHubPullRequestDiscovery { strategyId(1) }
          }
        }
      }
    }
  }
  factory {
    workflowBranchProjectFactory {
      scriptPath('jenkins/Jenkinsfile')
    }
  }

  orphanedItemStrategy {
    discardOldItems { numToKeep(5) }
  }

  triggers {
    periodicFolderTrigger { interval('1d') }
  }
}