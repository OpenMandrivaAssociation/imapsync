Summary:	IMAP synchronisation, sync, copy or migration tool
Name:		imapsync
Version:	1.468
Release:	1
License:	WTFPL
Group:		Networking/Mail
URL:		http://ks.lamiral.info/imapsync/
Source0:	http://www.linux-france.org/prj/imapsync/dist/%{name}-%{version}.tgz
Requires:	perl(Date::Manip)
Requires:	perl(Term::ReadKey)
Suggests:	perl(IO::Socket::SSL)
Suggests:	perl(Digest::HMAC_MD5)
BuildArch:	noarch

%description
imapsync is a tool for facilitating incremental recursive IMAP transfers from
one mailbox to another. It is useful for mailbox migration, and reduces the
amount of data transferred by only copying messages that are not present on
both servers. Read, unread, and deleted flags are preserved, and the process
can be stopped and resumed. The original messages can optionally be deleted
after a successful transfer.

%prep

%setup -q

%build

pod2man %{name} > %{name}.1

%install

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 %{name} %{buildroot}%{_bindir}/
install -m0644 %{name}.1 %{buildroot}%{_mandir}/man1/

%files
%defattr(-,root,root)
%doc CREDITS ChangeLog FAQ README TODO
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*

