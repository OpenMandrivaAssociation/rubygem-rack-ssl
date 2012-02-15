# Generated from rack-1.2.2.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	rack-ssl

Summary:	A modular Ruby webserver interface
Name:		rubygem-%{rbname}

Version:	1.3.2
Release:	2
Group:		Development/Ruby
License:	MIT
URL:		http://rack.rubyforge.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Requires:	ruby-RubyGems
BuildRequires:	ruby-RubyGems 
BuildArch:	noarch
#rename		ruby-rack

%description
Rack provides minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.

%prep
%setup -q

%build
%gem_build -f '(contrib|example|test)/'

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
