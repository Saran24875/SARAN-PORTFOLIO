from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class ProgrammingLanguage(models.Model):
    PROGRAMMING_LANGUAGE_CHOICES = [
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('Cpp', 'C++'),
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
            'Python': 'fab fa-python',
            'Java': 'fab fa-java',
            'C': 'fas fa-code',
            'Cpp': 'fas fa-code',
            'Javascript': 'fab fa-js',
            'Typescript': 'fab fa-js',
            'Csharp': 'fab fa-microsoft',
            'Swift': 'fab fa-swift',
            'Kotlin': 'fas fa-code',
            'Go': 'fas fa-code',
            'Rust': 'fas fa-code',
            'Dart': 'fas fa-code',
            'Ruby': 'fa-solid fa-gem',
            'Php': 'fab fa-php',
            'R': 'fas fa-code',
            'Julia': 'fas fa-code',
            'Sql': 'fas fa-database',
            'Plsql': 'fas fa-database',
            'Tsql': 'fas fa-database',
            'Graphql': 'fas fa-project-diagram',
            'Perl': 'fas fa-code',
            'Lua': 'fas fa-code',
            'Haskell': 'fas fa-code',
            'Clojure': 'fas fa-code',
            'Scala': 'fab fa-scala',
            'Erlang': 'fas fa-code',
            'Elixir': 'fas fa-code',
            'Fsharp': 'fas fa-code',
            'Ocaml': 'fas fa-code',
            'Prolog': 'fas fa-code',
            'Lisp': 'fas fa-code',
            'Scheme': 'fas fa-code',
            'Fortran': 'fas fa-code',
            'Cobol': 'fas fa-code',
            'Basic': 'fas fa-code',
            'Smalltalk': 'fas fa-code',
            'Ada': 'fas fa-code',
            'Algol': 'fas fa-code',
            'Pascal': 'fas fa-code',
            'Modula2': 'fas fa-code',
            'Vhdl': 'fas fa-microchip',
            'Verilog': 'fas fa-microchip',
            'Jcl': 'fas fa-code',
            'Xquery': 'fas fa-code',
            'Postscript': 'fas fa-code',
            'Bash': 'fas fa-terminal',
            'Powershell': 'fas fa-terminal',
            'Nim': 'fas fa-code',
            'Zig': 'fas fa-code',
            'Gams': 'fas fa-code',
            'Idl': 'fas fa-code',
            'Latex': 'fas fa-file-alt',
            'Brainfuck': 'fas fa-brain',
            'Whitespace': 'fas fa-code',
            'Intercal': 'fas fa-code',
            'Malbolge': 'fas fa-code',
            'Piet': 'fas fa-paint-brush',
            'Befunge': 'fas fa-code',
            'Qsharp': 'fas fa-atom',
            'Qiskit': 'fas fa-atom',
            'Quipper': 'fas fa-atom',
            'Silq': 'fas fa-atom',
            'Cirq': 'fas fa-atom',
            'Other': 'fas fa-code'
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
        ('Other', 'Other'),
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
            'Django': 'fab fa-python',
            'Flask': 'fab fa-python',
            'Fastapi': 'fas fa-bolt',
            'Express': 'fab fa-node-js',
            'Nestjs': 'fas fa-server',
            'Spring': 'fab fa-java',
            'Rails': 'fas fa-gem',
            'Laravel': 'fab fa-laravel',
            'Symfony': 'fab fa-symfony',
            'Codeigniter': 'fas fa-fire',
            'Aspnet': 'fab fa-microsoft',
            'Dotnetcore': 'fab fa-microsoft',
            'Phoenix': 'fas fa-fire',
            'Nextjs': 'fas fa-code',
            'Nuxtjs': 'fab fa-vuejs',
            'Sveltekit': 'fas fa-code',
            'Quasar': 'fas fa-code',
            'Vue': 'fab fa-vuejs',
            'Angular': 'fab fa-angular',
            'React': 'fab fa-react',
            'Blazor': 'fas fa-code',
            'Flutter': 'fas fa-mobile-alt',
            'Electron': 'fas fa-desktop',
            'Qt': 'fas fa-desktop',
            'Kivy': 'fas fa-mobile-alt',
            'Tkinter': 'fas fa-window-maximize',
            'Gtk': 'fas fa-desktop',
            'Wxpython': 'fas fa-code',
            'Pyramid': 'fas fa-mountain',
            'Bottle': 'fas fa-flask',
            'Tornado': 'fas fa-wind',
            'Cherrypy': 'fas fa-tree',
            'Falcon': 'fas fa-feather-alt',
            'Hanami': 'fas fa-seedling',
            'Play': 'fas fa-play',
            'Struts': 'fas fa-code',
            'Zend': 'fas fa-code',
            'Fuelphp': 'fas fa-gas-pump',
            'Cakephp': 'fas fa-birthday-cake',
            'Adonisjs': 'fas fa-leaf',
            'Feathersjs': 'fas fa-feather',
            'Meteor': 'fas fa-meteor',
            'Hapi': 'fas fa-smile',
            'Backbone': 'fas fa-bone',
            'Ember': 'fas fa-fire',
            'Mithril': 'fas fa-shield-alt',
            'Marionette': 'fas fa-theater-masks',
            'Redwood': 'fas fa-tree',
            'Gatsy': 'fas fa-rocket',
            'Remix': 'fas fa-music',
            'Micro': 'fas fa-microchip',
            'Aurelia': 'fas fa-code',
            'Other': 'fas fa-code',
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
        ('Other', 'Other'),
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
            'Git': 'fab fa-git-alt',
            'Github': 'fab fa-github',
            'Gitlab': 'fab fa-gitlab',
            'Bitbucket': 'fab fa-bitbucket',
            'Docker': 'fab fa-docker',
            'Kubernetes': 'fas fa-network-wired',
            'Jenkins': 'fab fa-jenkins',
            'Ansible': 'fas fa-cogs',
            'Puppet': 'fas fa-code-branch',
            'Chef': 'fas fa-utensils',
            'Terraform': 'fas fa-cubes',
            'Vagrant': 'fas fa-box',
            'Npm': 'fab fa-npm',
            'Yarn': 'fab fa-yarn',
            'Pnpm': 'fas fa-cube',
            'Webpack': 'fas fa-cogs',
            'Babel': 'fas fa-language',
            'Esbuild': 'fas fa-hammer',
            'Rollup': 'fas fa-sync-alt',
            'Parcel': 'fas fa-box-open',
            'Gulp': 'fas fa-coffee',
            'Grunt': 'fas fa-bug',
            'Eslint': 'fas fa-exclamation-circle',
            'Prettier': 'fas fa-paint-brush',
            'Sonarqube': 'fas fa-water',
            'Postman': 'fas fa-envelope',
            'Swagger': 'fas fa-file-alt',
            'Selenium': 'fas fa-robot',
            'Cypress': 'fas fa-spider',
            'Jest': 'fas fa-vial',
            'Mocha': 'fas fa-mug-hot',
            'Chai': 'fas fa-coffee',
            'Junit': 'fas fa-balance-scale',
            'Pytest': 'fas fa-vial',
            'Cucumber': 'fas fa-seedling',
            'Robotframework': 'fas fa-robot',
            'Newrelic': 'fas fa-chart-line',
            'Datadog': 'fas fa-dog',
            'Prometheus': 'fas fa-fire',
            'Grafana': 'fas fa-chart-pie',
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
            'Opentelemetry': 'fas fa-chart-network',
            'Other': 'fas fa-tools',
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
            'Mysql': 'fas fa-database',
            'Postgresql': 'fas fa-database',
            'Sqlite': 'fas fa-table',
            'Mongodb': 'fab fa-envira',
            'Redis': 'fas fa-memory',
            'Mariadb': 'fas fa-database',
            'Oracle': 'fas fa-server',
            'Sqlserver': 'fas fa-server',
            'Firebase': 'fab fa-google',
            'Dynamodb': 'fas fa-server',
            'Cassandra': 'fas fa-cloud',
            'Neo4j': 'fas fa-project-diagram',
            'Couchdb': 'fas fa-couch',
            'Arangodb': 'fas fa-project-diagram',
            'Cockroachdb': 'fas fa-bug',
            'Influxdb': 'fas fa-chart-line',
            'Timescaledb': 'fas fa-clock',
            'Tidb': 'fas fa-database',
            'Clickhouse': 'fas fa-mouse-pointer',
            'Voltdb': 'fas fa-bolt',
            'Tarantool': 'fas fa-spider',
            'Memcached': 'fas fa-memory',
            'Faunadb': 'fas fa-paw',
            'Supabase': 'fas fa-cloud',
            'Other': 'fas fa-database',
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
            'Negotiation': 'fas fa-handshake-alt',
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

