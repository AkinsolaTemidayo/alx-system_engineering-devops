# Define a class to install Flask
class install_flask {
  
  # Install pip3 package
  package { 'python3-pip':
    ensure => installed,
  }

  # Install Flask using pip3
  package { 'Flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3-pip'],
  }
}
