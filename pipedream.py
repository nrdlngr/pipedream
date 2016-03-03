import click
import botocore, botocore.session

session = botocore.session.get_session()
iam_client = session.create_client('iam')
account_id = iam_client.get_user()['User']['Arn'].split(':')[4]


@click.command()
@click.option('--profile', metavar='AWS_PROFILE', envvar='AWS_PROFILE', default='default', help='The name of the AWS profile to use.')
@click.option('--versioning', help='The versioning type to use.', type=click.Choice(['latest', 'git-commit-id', 'sequential', 'fixed']), default='latest')
@click.argument('repo_name', metavar='GITHUB_REPO_NAME')

def cli(profile, versioning, repo_name):
    """The `pipedream` program creates Project Pipelines.
    
    Given a GitHub repository, the `pipedream` program generates a pipeline and an ECR Repository attached to the GitHub project. The GitHub project must have a DockerFile associated with it in the root directory. When a new change is pushed, the pipeline kicks off a new build of the Docker image and pushes it to ECR with a choice of versioning patterns (i.e. "latest", "git-commit-id", "sequential", "fixed").
    
    After the build is finished, `pipedream` finds all ECS task definitions that reference the updated image, and creates new task definition revisions. 
    
    After the new revisions are created, the pipeline updates any ECS services with the updated task definitions."""
    
    click.echo()
    click.echo("Here is your Pipeline configuration:")
    click.echo()
    click.echo("Profile: " + profile)
    click.echo("Versioning: " + versioning)
    click.echo("AWS Account ID: " + account_id)
    click.echo("GitHub Repo Name: " + repo_name)
    click.echo()
    