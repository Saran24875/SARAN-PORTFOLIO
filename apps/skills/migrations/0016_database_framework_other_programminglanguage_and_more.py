# Generated by Django 4.2 on 2025-03-15 08:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0015_rename_level_skills_database_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_database', models.CharField(choices=[('mysql', 'MySQL'), ('postgresql', 'PostgreSQL'), ('sqlite', 'SQLite'), ('mongodb', 'MongoDB'), ('redis', 'Redis'), ('mariadb', 'MariaDB'), ('oracle', 'Oracle'), ('sqlserver', 'SQL Server'), ('firebase', 'Firebase'), ('dynamodb', 'DynamoDB'), ('cassandra', 'Cassandra'), ('neo4j', 'Neo4j'), ('couchdb', 'CouchDB'), ('arangodb', 'ArangoDB'), ('cockroachdb', 'CockroachDB'), ('influxdb', 'InfluxDB'), ('timescaledb', 'TimescaleDB'), ('tidb', 'TiDB'), ('clickhouse', 'ClickHouse'), ('voltdb', 'VoltDB'), ('tarantool', 'Tarantool'), ('memcached', 'Memcached'), ('faunadb', 'FaunaDB'), ('supabase', 'Supabase'), ('other', 'Other')], max_length=100, null=True)),
                ('level', models.IntegerField(default=0, help_text='Give the third technology used level (1-100)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_framework', models.CharField(choices=[('django', 'Django'), ('flask', 'Flask'), ('fastapi', 'FastAPI'), ('express', 'Express.js'), ('nestjs', 'NestJS'), ('spring', 'Spring Boot'), ('rails', 'Ruby on Rails'), ('laravel', 'Laravel'), ('symfony', 'Symfony'), ('codeigniter', 'CodeIgniter'), ('aspnet', 'ASP.NET'), ('dotnetcore', '.NET Core'), ('phoenix', 'Phoenix'), ('nextjs', 'Next.js'), ('nuxtjs', 'Nuxt.js'), ('sveltekit', 'SvelteKit'), ('quasar', 'Quasar'), ('vue', 'Vue.js'), ('angular', 'Angular'), ('react', 'React'), ('blazor', 'Blazor'), ('flutter', 'Flutter'), ('electron', 'Electron'), ('qt', 'Qt'), ('kivy', 'Kivy'), ('tkinter', 'Tkinter'), ('gtk', 'GTK'), ('wxpython', 'wxPython'), ('pyramid', 'Pyramid'), ('bottle', 'Bottle'), ('tornado', 'Tornado'), ('cherrypy', 'CherryPy'), ('falcon', 'Falcon'), ('hanami', 'Hanami'), ('play', 'Play Framework'), ('struts', 'Struts'), ('zend', 'Zend Framework'), ('fuelphp', 'FuelPHP'), ('cakephp', 'CakePHP'), ('adonisjs', 'AdonisJS'), ('feathersjs', 'FeathersJS'), ('meteor', 'Meteor'), ('hapi', 'Hapi.js'), ('backbone', 'Backbone.js'), ('ember', 'Ember.js'), ('mithril', 'Mithril.js'), ('marionette', 'Marionette.js'), ('redwood', 'RedwoodJS'), ('gatsy', 'Gatsby'), ('remix', 'Remix'), ('micro', 'Micro'), ('aurelia', 'Aurelia'), ('other', 'Other')], max_length=100, null=True)),
                ('level', models.IntegerField(default=0, help_text='Give the third technology used level (1-100)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('name', models.CharField(default='Other', max_length=100)),
                ('level', models.IntegerField(default=0, help_text='Give the third technology used level (1-100)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('python', 'Python'), ('java', 'Java'), ('c', 'C'), ('cpp', 'C++'), ('javascript', 'JavaScript'), ('typescript', 'TypeScript'), ('csharp', 'C#'), ('swift', 'Swift'), ('kotlin', 'Kotlin'), ('go', 'Go'), ('rust', 'Rust'), ('dart', 'Dart'), ('ruby', 'Ruby'), ('php', 'PHP'), ('r', 'R'), ('julia', 'Julia'), ('sql', 'SQL'), ('plsql', 'PL/SQL'), ('tsql', 'T-SQL'), ('graphql', 'GraphQL'), ('perl', 'Perl'), ('lua', 'Lua'), ('haskell', 'Haskell'), ('clojure', 'Clojure'), ('scala', 'Scala'), ('erlang', 'Erlang'), ('elixir', 'Elixir'), ('fsharp', 'F#'), ('ocaml', 'OCaml'), ('prolog', 'Prolog'), ('lisp', 'Lisp'), ('scheme', 'Scheme'), ('fortran', 'Fortran'), ('cobol', 'COBOL'), ('basic', 'BASIC'), ('smalltalk', 'Smalltalk'), ('ada', 'Ada'), ('algol', 'ALGOL'), ('pascal', 'Pascal'), ('modula2', 'Modula-2'), ('vhdl', 'VHDL'), ('verilog', 'Verilog'), ('jcl', 'JCL'), ('xquery', 'XQuery'), ('postscript', 'PostScript'), ('bash', 'Bash'), ('powershell', 'PowerShell'), ('nim', 'Nim'), ('zig', 'Zig'), ('gams', 'GAMS'), ('idl', 'IDL'), ('latex', 'LaTeX'), ('brainfuck', 'Brainfuck'), ('whitespace', 'Whitespace'), ('intercal', 'INTERCAL'), ('malbolge', 'Malbolge'), ('piet', 'Piet'), ('befunge', 'Befunge'), ('qsharp', 'Q#'), ('qiskit', 'Qiskit'), ('quipper', 'Quipper'), ('silq', 'Silq'), ('cirq', 'Cirq')], max_length=100, null=True)),
                ('level', models.IntegerField(default=0, help_text='Give the third technology used level (1-100)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='SoftSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_soft_skills', models.CharField(choices=[('communication', 'Communication'), ('typewriting', 'Typewriting'), ('teamwork', 'Teamwork'), ('problem_solving', 'Problem Solving'), ('critical_thinking', 'Critical Thinking'), ('leadership', 'Leadership'), ('adaptability', 'Adaptability'), ('creativity', 'Creativity'), ('time_management', 'Time Management'), ('emotional_intelligence', 'Emotional Intelligence'), ('conflict_resolution', 'Conflict Resolution'), ('decision_making', 'Decision Making'), ('work_ethic', 'Work Ethic'), ('stress_management', 'Stress Management'), ('negotiation', 'Negotiation'), ('self_motivation', 'Self-Motivation'), ('attention_to_detail', 'Attention to Detail'), ('interpersonal_skills', 'Interpersonal Skills'), ('active_listening', 'Active Listening'), ('collaboration', 'Collaboration'), ('presentation_skills', 'Presentation Skills'), ('customer_service', 'Customer Service'), ('other', 'Other')], max_length=100, null=True)),
                ('level', models.IntegerField(default=0, help_text='Give the third technology used level (1-100)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_tools', models.CharField(choices=[('git', 'Git'), ('github', 'GitHub'), ('gitlab', 'GitLab'), ('bitbucket', 'Bitbucket'), ('docker', 'Docker'), ('kubernetes', 'Kubernetes'), ('jenkins', 'Jenkins'), ('ansible', 'Ansible'), ('puppet', 'Puppet'), ('chef', 'Chef'), ('terraform', 'Terraform'), ('vagrant', 'Vagrant'), ('npm', 'NPM'), ('yarn', 'Yarn'), ('pnpm', 'PNPM'), ('webpack', 'Webpack'), ('babel', 'Babel'), ('esbuild', 'ESBuild'), ('rollup', 'Rollup'), ('parcel', 'Parcel'), ('gulp', 'Gulp'), ('grunt', 'Grunt'), ('eslint', 'ESLint'), ('prettier', 'Prettier'), ('sonarqube', 'SonarQube'), ('postman', 'Postman'), ('swagger', 'Swagger'), ('selenium', 'Selenium'), ('cypress', 'Cypress'), ('jest', 'Jest'), ('mocha', 'Mocha'), ('chai', 'Chai'), ('junit', 'JUnit'), ('pytest', 'PyTest'), ('cucumber', 'Cucumber'), ('robotframework', 'Robot Framework'), ('newrelic', 'New Relic'), ('datadog', 'Datadog'), ('prometheus', 'Prometheus'), ('grafana', 'Grafana'), ('splunk', 'Splunk'), ('elk', 'ELK Stack'), ('logstash', 'Logstash'), ('filebeat', 'Filebeat'), ('kibana', 'Kibana'), ('zabbix', 'Zabbix'), ('nagios', 'Nagios'), ('graylog', 'Graylog'), ('honeycomb', 'Honeycomb'), ('jaeger', 'Jaeger'), ('opentelemetry', 'OpenTelemetry'), ('other', 'Other')], max_length=100, null=True)),
                ('level', models.IntegerField(default=0, help_text='Give the third technology used level (1-100)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
    ]
