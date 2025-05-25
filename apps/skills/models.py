from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class ProgrammingLanguage(models.Model):
    PROGRAMMING_LANGUAGE_CHOICES = [
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('Cpp', 'C++'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('Javascript', 'JavaScript'),
        ('Typescript', 'TypeScript'),
        ('Csharp', 'C#'),
        ('Swift', 'Swift'),
        ('Kotlin', 'Kotlin'),
        ('Go', 'Go'),
        ('Rust', 'Rust'),
        ('Dart', 'Dart'),
        ('Ruby', 'Ruby'),
        ('Php', 'PHP'),
        ('R', 'R'),
        ('Julia', 'Julia'),
        ('Sql', 'SQL'),
        ('Plsql', 'PL/SQL'),
        ('Tsql', 'T-SQL'),
        ('Graphql', 'GraphQL'),
        ('Perl', 'Perl'),
        ('Lua', 'Lua'),
        ('Haskell', 'Haskell'),
        ('Clojure', 'Clojure'),
        ('Scala', 'Scala'),
        ('Erlang', 'Erlang'),
        ('Elixir', 'Elixir'),
        ('Fsharp', 'F#'),
        ('Ocaml', 'OCaml'),
        ('Prolog', 'Prolog'),
        ('Lisp', 'Lisp'),
        ('Scheme', 'Scheme'),
        ('Fortran', 'Fortran'),
        ('Cobol', 'COBOL'),
        ('Basic', 'BASIC'),
        ('Smalltalk', 'Smalltalk'),
        ('Ada', 'Ada'),
        ('Algol', 'ALGOL'),
        ('Pascal', 'Pascal'),
        ('Modula2', 'Modula-2'),
        ('Vhdl', 'VHDL'),
        ('Verilog', 'Verilog'),
        ('Jcl', 'JCL'),
        ('Xquery', 'XQuery'),
        ('Postscript', 'PostScript'),
        ('Bash', 'Bash'),
        ('Powershell', 'PowerShell'),
        ('Nim', 'Nim'),
        ('Zig', 'Zig'),
        ('Gams', 'GAMS'),
        ('Idl', 'IDL'),
        ('Latex', 'LaTeX'),
        ('Brainfuck', 'Brainfuck'),
        ('Whitespace', 'Whitespace'),
        ('Intercal', 'INTERCAL'),
        ('Malbolge', 'Malbolge'),
        ('Piet', 'Piet'),
        ('Befunge', 'Befunge'),
        ('Qsharp', 'Q#'),
        ('Qiskit', 'Qiskit'),
        ('Quipper', 'Quipper'),
        ('Silq', 'Silq'),
        ('Cirq', 'Cirq'),
    ]
    name = models.CharField(
        max_length=100, 
        choices=PROGRAMMING_LANGUAGE_CHOICES, 
        null=True, 
        blank=True,
        help_text="Please select either 'select a programming language from the list' or specify a custom entry."
    )
    custom_entry = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Specify a custom programming language"
    )
    custom_icon = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Provide a custom Font Awesome icon for the programming language, e.g., 'fa-brands fa-python'"
    )
    level = models.IntegerField(
        default=0,
        validators=[MinValueValidator(35), MaxValueValidator(100)],
        help_text="Provide the proficiency level of the programming language (35-100)"
    )


    def clean(self):
        if self.name and self.custom_entry:
            raise ValidationError("Please select either 'select the name from the list' or specify a custom entry, not both.")
        if not self.custom_entry and self.custom_icon:
            raise ValidationError("Please specify a custom entry if you are providing a custom icon.")
        if self.custom_entry and not self.custom_icon:
            raise ValidationError("Please specify a custom icon if you are providing a custom entry.")
        if not self.name and not self.custom_entry:
            raise ValidationError("Please select a programming language or specify a custom entry.")

    def __str__(self):
        return self.custom_entry if self.custom_entry else self.name

    
    
    @property
    def icon(self):
        mapping = {
            'Python': 'fab fa-python',  # Font Awesome
            'Java': 'fab fa-java',      # Font Awesome
            'C': 'devicon-c-plain  ',  # Devicon
            'Cpp': 'devicon-cplusplus-plain  ',  # Devicon
            'HTML': 'fab fa-html5',     # Font Awesome
            'CSS': 'fab fa-css3-alt',   # Font Awesome
            'Javascript': 'fab fa-js',  # Font Awesome
            'Typescript': 'devicon-typescript-plain  ',  # Devicon
            'Csharp': 'devicon-csharp-plain  ',  # Devicon
            'Swift': 'devicon-swift-plain  ',  # Devicon
            'Kotlin': 'devicon-kotlin-plain  ',  # Devicon
            'Go': 'devicon-go-plain  ',  # Devicon
            'Rust': 'devicon-rust-plain  ',  # Devicon
            'Dart': 'devicon-dart-plain  ',  # Devicon
            'Ruby': 'devicon-ruby-plain  ',  # Devicon
            'Php': 'fab fa-php',  # Font Awesome
            'R': 'devicon-r-plain  ',  # Devicon
            'Julia': 'devicon-julia-plain  ',  # Devicon
            'Sql': 'fas fa-database',  # Font Awesome
            'Plsql': 'fas fa-database',  # Fallback
            'Tsql': 'fas fa-database',  # Fallback
            'Graphql': 'devicon-graphql-plain  ',  # Devicon
            'Perl': 'devicon-perl-plain  ',  # Devicon
            'Lua': 'devicon-lua-plain  ',  # Devicon
            'Haskell': 'devicon-haskell-plain  ',  # Devicon
            'Clojure': 'devicon-clojure-plain  ',  # Devicon
            'Scala': 'devicon-scala-plain  ',  # Devicon
            'Erlang': 'devicon-erlang-plain  ',  # Devicon
            'Elixir': 'devicon-elixir-plain  ',  # Devicon
            'Fsharp': 'fas fa-code',  # Fallback
            'Ocaml': 'fas fa-code',  # Fallback
            'Prolog': 'fas fa-code',  # Fallback
            'Lisp': 'fas fa-code',  # Fallback
            'Scheme': 'fas fa-code',  # Fallback
            'Fortran': 'devicon-fortran-plain  ',  # Devicon
            'Cobol': 'fas fa-code',  # Fallback
            'Basic': 'fas fa-code',  # Fallback
            'Smalltalk': 'fas fa-code',  # Fallback
            'Ada': 'fas fa-code',  # Fallback
            'Algol': 'fas fa-code',  # Fallback
            'Pascal': 'fas fa-code',  # Fallback
            'Modula2': 'fas fa-code',  # Fallback
            'Vhdl': 'fas fa-microchip',  # Fallback
            'Verilog': 'fas fa-microchip',  # Fallback
            'Jcl': 'fas fa-code',  # Fallback
            'Xquery': 'fas fa-code',  # Fallback
            'Postscript': 'fas fa-code',  # Fallback
            'Bash': 'devicon-bash-plain  ',  # Devicon
            'Powershell': 'fas fa-terminal',  # Font Awesome
            'Nim': 'fas fa-code',  # Fallback
            'Zig': 'fas fa-code',  # Fallback
            'Gams': 'fas fa-code',  # Fallback
            'Idl': 'fas fa-code',  # Fallback
            'Latex': 'devicon-latex-original',  # Devicon
            'Brainfuck': 'fas fa-brain',  # Font Awesome
            'Whitespace': 'fas fa-code',  # Fallback
            'Intercal': 'fas fa-code',  # Fallback
            'Malbolge': 'fas fa-code',  # Fallback
            'Piet': 'fas fa-paint-brush',  # Font Awesome
            'Befunge': 'fas fa-code',  # Fallback
            'Qsharp': 'fas fa-atom',  # Font Awesome
            'Qiskit': 'fas fa-atom',  # Font Awesome
            'Quipper': 'fas fa-atom',  # Font Awesome
            'Silq': 'fas fa-atom',  # Font Awesome
            'Cirq': 'fas fa-atom',  # Font Awesome
            'Other': 'fas fa-code'  # Default
        }
        return mapping.get(self.name, 'fas fa-code')


class Framework(models.Model):
    FRAMEWORK_CHOICES = [
        ('Django', 'Django'),
        ('Flask', 'Flask'),
        ('Fastapi', 'FastAPI'),
        ('Express', 'Express.js'),
        ('Nestjs', 'NestJS'),
        ('Spring', 'Spring Boot'),
        ('Rails', 'Ruby on Rails'),
        ('Laravel', 'Laravel'),
        ('Symfony', 'Symfony'),
        ('Codeigniter', 'CodeIgniter'),
        ('Aspnet', 'ASP.NET'),
        ('Dotnetcore', '.NET Core'),
        ('Phoenix', 'Phoenix'),
        ('Nextjs', 'Next.js'),
        ('Nuxtjs', 'Nuxt.js'),
        ('Sveltekit', 'SvelteKit'),
        ('Quasar', 'Quasar'),
        ('Vue', 'Vue.js'),
        ('Angular', 'Angular'),
        ('React', 'React'),
        ('Blazor', 'Blazor'),
        ('Flutter', 'Flutter'),
        ('Electron', 'Electron'),
        ('Qt', 'Qt'),
        ('Kivy', 'Kivy'),
        ('Tkinter', 'Tkinter'),
        ('Gtk', 'GTK'),
        ('Wxpython', 'wxPython'),
        ('Pyramid', 'Pyramid'),
        ('Bottle', 'Bottle'),
        ('Tornado', 'Tornado'),
        ('Cherrypy', 'CherryPy'),
        ('Falcon', 'Falcon'),
        ('Hanami', 'Hanami'),
        ('Play', 'Play Framework'),
        ('Struts', 'Struts'),
        ('Zend', 'Zend Framework'),
        ('Fuelphp', 'FuelPHP'),
        ('Cakephp', 'CakePHP'),
        ('Adonisjs', 'AdonisJS'),
        ('Feathersjs', 'FeathersJS'),
        ('Meteor', 'Meteor'),
        ('Hapi', 'Hapi.js'),
        ('Backbone', 'Backbone.js'),
        ('Ember', 'Ember.js'),
        ('Mithril', 'Mithril.js'),
        ('Marionette', 'Marionette.js'),
        ('Redwood', 'RedwoodJS'),
        ('Gatsy', 'Gatsby'),
        ('Remix', 'Remix'),
        ('Micro', 'Micro'),
        ('Aurelia', 'Aurelia'),
    ]

    select_framework = models.CharField(max_length=100, choices=FRAMEWORK_CHOICES, null=True, blank=True,
                                        help_text="Please select either 'select a framework from the list' or specify a custom entry.")
    custom_entry = models.CharField(max_length=100, blank=True, null=True,
                                    help_text="Enter a custom framework name")
    custom_icon = models.CharField(max_length=100, blank=True, null=True,
                                   help_text="Enter a custom icon for the framework in Font Awesome format, e.g. 'fa-brands fa-bootstrap'")
    level = models.IntegerField(
        default=0,
        validators=[MinValueValidator(35), MaxValueValidator(100)],
        help_text="Give the third technology used level (35-100)"
    )

    def clean(self):
        if self.select_framework and (self.custom_entry or self.custom_icon):
            raise ValidationError("Please select either 'select a framework from the list' or specify a custom entry.")
        if not self.custom_entry and self.custom_icon:
            raise ValidationError("Please specify both a custom entry and icon.")
        if self.custom_entry and not self.custom_icon:
            raise ValidationError("Please specify both a custom entry and icon.")
        if not self.select_framework and not self.custom_entry:
            raise ValidationError("Please select a framework or specify a custom entry.")

    def __str__(self):
        return self.custom_entry if self.custom_entry else self.select_framework

    @property
    def icon(self):
        mapping = {
            'Django': 'devicon-django-plain  ',           # Devicon
            'Flask': 'devicon-flask-original  ',          # Devicon
            'Fastapi': 'fas fa-bolt',                           # FA (no Devicon yet)
            'Express': 'devicon-express-original  ',      # Devicon
            'Nestjs': 'devicon-nestjs-plain  ',           # Devicon
            'Spring': 'devicon-spring-plain  ',           # Devicon
            'Rails': 'devicon-rails-plain  ',             # Devicon
            'Laravel': 'devicon-laravel-plain  ',         # Devicon
            'Symfony': 'devicon-symfony-original  ',      # Devicon
            'Codeigniter': 'fas fa-fire',                       # FA fallback
            'Aspnet': 'devicon-dot-net-plain  ',          # Devicon (for .NET tech)
            'Dotnetcore': 'devicon-dot-net-plain  ',      # Devicon
            'Phoenix': 'fas fa-fire',                           # FA fallback
            'Nextjs': 'devicon-nextjs-original',                # Devicon (monochrome only)
            'Nuxtjs': 'devicon-nuxtjs-plain  ',           # Devicon
            'Sveltekit': 'devicon-svelte-plain  ',        # Devicon
            'Quasar': 'fas fa-code',                            # FA fallback
            'Vue': 'devicon-vuejs-plain  ',               # Devicon
            'Angular': 'devicon-angularjs-plain  ',       # Devicon
            'React': 'devicon-react-original  ',          # Devicon
            'Blazor': 'devicon-dot-net-plain  ',          # Devicon
            'Flutter': 'devicon-flutter-plain  ',         # Devicon
            'Electron': 'devicon-electron-original  ',    # Devicon
            'Qt': 'devicon-qt-original  ',                # Devicon
            'Kivy': 'fas fa-mobile-alt',                        # FA fallback
            'Tkinter': 'fas fa-window-maximize',                # FA fallback
            'Gtk': 'fas fa-desktop',                            # FA fallback
            'Wxpython': 'fas fa-code',                          # FA fallback
            'Pyramid': 'fas fa-mountain',                       # FA fallback
            'Bottle': 'fas fa-flask',                           # FA fallback
            'Tornado': 'fas fa-wind',                           # FA fallback
            'Cherrypy': 'fas fa-tree',                          # FA fallback
            'Falcon': 'fas fa-feather-alt',                     # FA fallback
            'Hanami': 'fas fa-seedling',                        # FA fallback
            'Play': 'fas fa-play',                              # FA fallback
            'Struts': 'fas fa-code',                            # FA fallback
            'Zend': 'fas fa-code',                              # FA fallback
            'Fuelphp': 'fas fa-gas-pump',                       # FA fallback
            'Cakephp': 'fas fa-birthday-cake',                  # FA fallback
            'Adonisjs': 'fas fa-leaf',                          # FA fallback
            'Feathersjs': 'fas fa-feather',                     # FA fallback
            'Meteor': 'fas fa-meteor',                          # FA fallback
            'Hapi': 'fas fa-smile',                             # FA fallback
            'Backbone': 'devicon-backbonejs-plain  ',     # Devicon
            'Ember': 'devicon-ember-original  ',          # Devicon
            'Mithril': 'fas fa-shield-alt',                     # FA fallback
            'Marionette': 'fas fa-theater-masks',               # FA fallback
            'Redwood': 'fas fa-tree',                           # FA fallback
            'Gatsy': 'fas fa-rocket',                           # Typo? Possibly Gatsby → use below
            'Gatsby': 'devicon-gatsby-plain  ',           # Devicon
            'Remix': 'fas fa-music',                            # FA fallback
            'Micro': 'fas fa-microchip',                        # FA fallback
            'Aurelia': 'fas fa-code',                           # FA fallback
            'Other': 'fas fa-code'                              # Default
        }
        return mapping.get(self.select_framework, 'fas fa-code')



class Tools(models.Model):
    TOOLS_CHOICES = [
        ('Git', 'Git'),
        ('Github', 'GitHub'),
        ('Gitlab', 'GitLab'),
        ('Bitbucket', 'Bitbucket'),
        ('Docker', 'Docker'),
        ('Kubernetes', 'Kubernetes'),
        ('Jenkins', 'Jenkins'),
        ('Ansible', 'Ansible'),
        ('Puppet', 'Puppet'),
        ('Chef', 'Chef'),
        ('Terraform', 'Terraform'),
        ('Vagrant', 'Vagrant'),
        ('Npm', 'NPM'),
        ('Yarn', 'Yarn'),
        ('Pnpm', 'PNPM'),
        ('Webpack', 'Webpack'),
        ('Babel', 'Babel'),
        ('Esbuild', 'ESBuild'),
        ('Rollup', 'Rollup'),
        ('Parcel', 'Parcel'),
        ('Gulp', 'Gulp'),
        ('Grunt', 'Grunt'),
        ('Eslint', 'ESLint'),
        ('Prettier', 'Prettier'),
        ('Sonarqube', 'SonarQube'),
        ('Postman', 'Postman'),
        ('Swagger', 'Swagger'),
        ('Selenium', 'Selenium'),
        ('Cypress', 'Cypress'),
        ('Jest', 'Jest'),
        ('Mocha', 'Mocha'),
        ('Chai', 'Chai'),
        ('Junit', 'JUnit'),
        ('Pytest', 'PyTest'),
        ('Cucumber', 'Cucumber'),
        ('Robotframework', 'Robot Framework'),
        ('Newrelic', 'New Relic'),
        ('Datadog', 'Datadog'),
        ('Prometheus', 'Prometheus'),
        ('Grafana', 'Grafana'),
        ('Splunk', 'Splunk'),
        ('Elk', 'ELK Stack'),
        ('Logstash', 'Logstash'),
        ('Filebeat', 'Filebeat'),
        ('Kibana', 'Kibana'),
        ('Zabbix', 'Zabbix'),
        ('Nagios', 'Nagios'),
        ('Graylog', 'Graylog'),
        ('Honeycomb', 'Honeycomb'),
        ('Jaeger', 'Jaeger'),
        ('Opentelemetry', 'OpenTelemetry'),
    ]

    select_tools = models.CharField(
        max_length=100,
        choices=TOOLS_CHOICES,
        null=True,
        blank=True,
        help_text="Please select either 'select a tool from the list' or specify a custom entry."
    )
    custom_entry = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Please specify a custom tool"
    )
    custom_icon = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Please specify the font awesome icon for the custom tool.eg: fas fa-code"
    )
    level = models.IntegerField(
        default=0,
        validators=[MinValueValidator(35), MaxValueValidator(100)],
        help_text="Give the third technology used level (35-100)"
    )
    def clean(self):
        if self.select_tools and (self.custom_entry or self.custom_icon):
            raise ValidationError("Please select either 'select the name from the list' or specify a custom entry. Do not do both.")
        if not self.custom_entry and self.custom_icon:
            raise ValidationError("Please specify a custom entry when providing an icon.")
        if self.custom_entry and not self.custom_icon:
            raise ValidationError("Please specify a custom icon when providing a custom entry.")
        if not self.select_tools and not self.custom_entry:
            raise ValidationError("Please select a tool or specify a custom entry. Do not leave both blank.")

    def __str__(self):
        return self.custom_entry if self.custom_entry else self.select_tools

    @property
    def icon(self):
        mapping = {
            'Git': 'devicon-git-plain  ',
            'Github': 'devicon-github-original',
            'Gitlab': 'devicon-gitlab-plain',
            'Bitbucket': 'fab fa-bitbucket',
            'Docker': 'devicon-docker-plain  ',
            'Kubernetes': 'devicon-kubernetes-plain  ',
            'Jenkins': 'devicon-jenkins-line  ',
            'Ansible': 'devicon-ansible-plain  ',
            'Puppet': 'devicon-puppet-plain  ',
            'Chef': 'fas fa-utensils',  # no devicon
            'Terraform': 'devicon-terraform-plain  ',
            'Vagrant': 'devicon-vagrant-plain  ',
            'Npm': 'devicon-npm-original-wordmark',
            'Yarn': 'devicon-yarn-plain',
            'Pnpm': 'fas fa-cube',  # no devicon
            'Webpack': 'devicon-webpack-plain  ',
            'Babel': 'devicon-babel-plain  ',
            'Esbuild': 'fas fa-hammer',  # no devicon
            'Rollup': 'fas fa-sync-alt',  # no devicon
            'Parcel': 'fas fa-box-open',  # no devicon
            'Gulp': 'devicon-gulp-plain  ',
            'Grunt': 'devicon-grunt-plain  ',
            'Eslint': 'devicon-eslint-original  ',
            'Prettier': 'devicon-prettier-plain  ',
            'Sonarqube': 'fas fa-water',  # no devicon
            'Postman': 'devicon-postman-plain  ',
            'Swagger': 'fas fa-file-alt',
            'Selenium': 'devicon-selenium-original  ',
            'Cypress': 'devicon-cypress-plain  ',
            'Jest': 'devicon-jest-plain  ',
            'Mocha': 'devicon-mocha-plain  ',
            'Chai': 'fas fa-coffee',  # no devicon
            'Junit': 'fas fa-balance-scale',
            'Pytest': 'fas fa-vial',
            'Cucumber': 'fas fa-seedling',
            'Robotframework': 'fas fa-robot',
            'Newrelic': 'fas fa-chart-line',
            'Datadog': 'fas fa-dog',
            'Prometheus': 'fas fa-fire',
            'Grafana': 'devicon-grafana-original',
            'Splunk': 'fas fa-search',
            'Elk': 'fas fa-layer-group',
            'Logstash': 'fas fa-file-contract',
            'Filebeat': 'fas fa-file-upload',
            'Kibana': 'fas fa-chart-bar',
            'Zabbix': 'fas fa-chart-area',
            'Nagios': 'fas fa-bell',
            'Graylog': 'fas fa-file-signature',
            'Honeycomb': 'fas fa-database',
            'Jaeger': 'fas fa-search-location',
            'Opentelemetry': 'fas fa-project-diagram',
            'Other': 'fas fa-tools'
        }
        return mapping.get(self.select_tools, 'fas fa-tools')



class Database(models.Model):
    DATABASE_CHOICES = [
        ('Mysql', 'MySQL'),
        ('Postgresql', 'PostgreSQL'),
        ('Sqlite', 'SQLite'),
        ('Mongodb', 'MongoDB'),
        ('Redis', 'Redis'),
        ('Mariadb', 'MariaDB'),
        ('Oracle', 'Oracle'),
        ('Sqlserver', 'SQL Server'),
        ('Firebase', 'Firebase'),
        ('Dynamodb', 'DynamoDB'),
        ('Cassandra', 'Cassandra'),
        ('Neo4j', 'Neo4j'),
        ('Couchdb', 'CouchDB'),
        ('Arangodb', 'ArangoDB'),
        ('Cockroachdb', 'CockroachDB'),
        ('Influxdb', 'InfluxDB'),
        ('Timescaledb', 'TimescaleDB'),
        ('Tidb', 'TiDB'),
        ('Clickhouse', 'ClickHouse'),
        ('Voltdb', 'VoltDB'),
        ('Tarantool', 'Tarantool'),
        ('Memcached', 'Memcached'),
        ('Faunadb', 'FaunaDB'),
        ('Supabase', 'Supabase'),
        ('Other', 'Other'),
    ]

    select_database = models.CharField(max_length=100, choices=DATABASE_CHOICES, null=True,blank=True,
                                       help_text="Please select either 'select a database from the list' or specify a custom entry.")
    custom_entry = models.CharField(max_length=100, blank=True, null=True,
                                    help_text="If the database you are looking for is not listed above, please enter a custom entry.e.g. Oracle")
    custom_icon = models.CharField(max_length=100, blank=True, null=True,
                                   help_text="Please enter a custom icon for the custom entry.eg. fas fa-database")
    level = models.IntegerField(
        default=0,
        validators=[MinValueValidator(35), MaxValueValidator(100)],
        help_text="Please give the technology used a level (35-100)"
    )

    def clean(self):
        if self.select_database and (self.custom_entry or self.custom_icon):
            raise ValidationError("Choose either 'select the name from the list' or provide a custom entry. Do not do both.")
        if not self.custom_entry and self.custom_icon:
            raise ValidationError("A custom entry and icon must be specified together.")
        if self.custom_entry and not self.custom_icon:
            raise ValidationError("A custom entry and icon must be specified together.")
        if not self.select_database and not self.custom_entry:
            raise ValidationError("Select a database or specify a custom entry. Do not leave both blank.")

    def __str__(self):
        return self.custom_entry if self.custom_entry else self.select_database

    @property
    def icon(self):
        mapping = {
            'Mysql': 'devicon-mysql-plain  ',               # Devicon
            'Postgresql': 'devicon-postgresql-plain  ',     # Devicon
            'Sqlite': 'devicon-sqlite-plain  ',             # Devicon
            'Mongodb': 'devicon-mongodb-plain  ',           # Devicon
            'Redis': 'devicon-redis-plain  ',               # Devicon
            'Mariadb': 'devicon-mariadb-plain  ',           # Devicon
            'Oracle': 'devicon-oracle-original  ',          # Devicon
            'Sqlserver': 'fas fa-server',                         # FA fallback
            'Firebase': 'devicon-firebase-plain  ',         # Devicon
            'Dynamodb': 'fas fa-server',                          # FA fallback
            'Cassandra': 'devicon-apachecassandra-plain  ', # Devicon
            'Neo4j': 'fas fa-project-diagram',                    # FA fallback
            'Couchdb': 'fas fa-couch',                            # FA fallback
            'Arangodb': 'fas fa-project-diagram',                 # FA fallback
            'Cockroachdb': 'fas fa-bug',                          # FA fallback
            'Influxdb': 'fas fa-chart-line',                      # FA fallback
            'Timescaledb': 'fas fa-clock',                        # FA fallback
            'Tidb': 'fas fa-database',                            # FA fallback
            'Clickhouse': 'fas fa-mouse-pointer',                 # FA fallback
            'Voltdb': 'fas fa-bolt',                              # FA fallback
            'Tarantool': 'fas fa-spider',                         # FA fallback
            'Memcached': 'fas fa-memory',                         # FA fallback
            'Faunadb': 'fas fa-paw',                              # FA fallback
            'Supabase': 'fas fa-cloud',                           # FA fallback
            'Other': 'fas fa-database'                            # Default fallback
        }
        return mapping.get(self.select_database, 'fas fa-database')



class SoftSkills(models.Model):
    SOFT_SKILLS_CHOICES = [
        ('Communication', 'Communication'),
        ('Typewriting', 'Typewriting'),
        ('Teamwork', 'Teamwork'),
        ('Problem solving', 'Problem Solving'),
        ('Critical thinking', 'Critical Thinking'),
        ('Leadership', 'Leadership'),
        ('Adaptability', 'Adaptability'),
        ('Creativity', 'Creativity'),
        ('Time management', 'Time Management'),
        ('Emotional intelligence', 'Emotional Intelligence'),
        ('Conflict resolution', 'Conflict Resolution'),
        ('Decision making', 'Decision Making'),
        ('Work ethic', 'Work Ethic'),
        ('Stress management', 'Stress Management'),
        ('Negotiation', 'Negotiation'),
        ('Self motivation', 'Self-Motivation'),
        ('Attention to detail', 'Attention to Detail'),
        ('Interpersonal skills', 'Interpersonal Skills'),
        ('Active listening', 'Active Listening'),
        ('Collaboration', 'Collaboration'),
        ('Presentation_skills', 'Presentation Skills'),
        ('Customer service', 'Customer Service'),
        ('Other', 'Other'),
    ]

    select_soft_skills = models.CharField(max_length=100, choices=SOFT_SKILLS_CHOICES, null=True,blank=True,help_text="Please select either 'select a soft skill from the list' or specify a custom entry.")
    custom_entry = models.CharField(max_length=100, blank=True, null=True, help_text="You can specify a custom soft skill name")
    custom_icon = models.CharField(max_length=100, blank=True, null=True, help_text="You can specify a custom font awesome icon name.eg. fas fa-database")
    level = models.IntegerField(
        default=0,
        validators=[MinValueValidator(35), MaxValueValidator(100)],
        help_text="Give the third technology used level (35-100)"
    )

    def clean(self):
        if self.select_soft_skills and (self.custom_entry or self.custom_icon):
            raise ValidationError("Please select either 'select the name from the list' or specify a custom entry. Do not do both.")
        if not self.custom_entry and self.custom_icon:
            raise ValidationError("Please specify a custom entry when providing an icon.")
        if self.custom_entry and not self.custom_icon:
            raise ValidationError("Please specify a custom icon when providing a custom entry.")
        if not self.select_soft_skills and not self.custom_entry:
            raise ValidationError("Please select a soft skill or specify a custom entry. Do not leave both blank.")

    def __str__(self):
        return self.custom_entry if self.custom_entry else self.select_soft_skills

    @property
    def icon(self):
        mapping = {
            'Communication': 'fas fa-comments',
            'Typewriting': 'fas fa-keyboard',
            'Teamwork': 'fas fa-users',
            'Problem solving': 'fas fa-lightbulb',
            'Critical thinking': 'fas fa-brain',
            'Leadership': 'fas fa-user-tie',
            'Adaptability': 'fas fa-random',
            'Creativity': 'fas fa-paint-brush',
            'Time management': 'fas fa-clock',
            'Emotional intelligence': 'fas fa-heart',
            'Conflict resolution': 'fas fa-handshake',
            'Decision making': 'fas fa-check-circle',
            'Work ethic': 'fas fa-tasks',
            'Stress management': 'fas fa-smile',
            'Negotiation': 'fas fa-handshake',
            'Self motivation': 'fas fa-fire',
            'Attention to detail': 'fas fa-eye',
            'Interpersonal skills': 'fas fa-user-friends',
            'Active listening': 'fas fa-headphones',
            'Collaboration': 'fas fa-people-arrows',
            'Presentation skills': 'fas fa-chalkboard-teacher',
            'Customer service': 'fas fa-headset',
            'Other': 'fas fa-star',
        }
        return mapping.get(self.select_soft_skills, 'fas fa-user-friends')

