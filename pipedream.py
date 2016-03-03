import click
import botocore, botocore.session

session = botocore.session.get_session()
iam_client = session.create_client('iam')
account_id = iam_client.get_user()['User']['Arn'].split(':')[4]


@click.group()
@click.option('--profile', metavar='AWS_PROFILE', envvar='AWS_PROFILE', default='default', help='The name of the AWS profile to use.')
@click.argument('repo_name', metavar='GITHUB_REPO_NAME')
@click.pass_context
def cli(ctx, profile, repo_name):
    ctx.obj['PROFILE'] = profile
    ctx.obj['REPO_NAME'] = repo_name

    """The `pipedream` program creates Project Pipelines.
    
    Given a GitHub repository, the `pipedream` program generates a pipeline and an ECR Repository attached to the GitHub project. The GitHub project must have a DockerFile associated with it in the root directory. When a new change is pushed, the pipeline kicks off a new build of the Docker image and pushes it to ECR with a choice of versioning patterns (i.e. "latest", "git-commit-id", "sequential", "fixed").
    
    After the build is finished, `pipedream` finds all ECS task definitions that reference the updated image, and creates new task definition revisions. 
    
    After the new revisions are created, the pipeline updates any ECS services with the updated task definitions."""
    
    click.echo()
    click.echo("Here is your Pipeline configuration:")
    click.echo()
    click.echo("Profile: " + ctx.obj['PROFILE'])
    click.echo("AWS Account ID: " + account_id)
    click.echo("GitHub Repo Name: " + ctx.obj['REPO_NAME'])
    click.echo()

cli.command()
@click.option('--versioning', help='The versioning type to use.', type=click.Choice(['latest', 'git-commit-id', 'sequential', 'fixed']), default='latest')
@click.pass_context
def create(ctx, profile, repo_name):
    ctx.obj['PROFILE'] = profile
    ctx.obj['REPO_NAME'] = repo_name

    click.echo()
    click.echo("Successfully created Pipeline for " + ctx.obj['REPO_NAME'] + " for AWS account: " + account_id + ".")