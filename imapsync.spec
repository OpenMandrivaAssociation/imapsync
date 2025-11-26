Summary:	IMAP synchronisation, sync, copy or migration tool
Name:		imapsync
Version:	2.314
Release:	1
License:	WTFPL
Group:		Networking/Mail
URL:		https://imapsync.lamiral.info/
# git backup (seems out of date): https://github.com/imapsync/imapsync
Source0:	https://imapsync.lamiral.info/dist2/imapsync-%{version}.tgz
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
%autosetup -p1
# Don't run the dependency check during "make install", rpm dependencies handle it at
# install time, we don't want to depend on all install time deps at build time
sed -i -e 's,install: testp,install:,' Makefile

%build
%make_build man

%install
%make_install

%files
%defattr(-,root,root)
%doc CREDITS ChangeLog FAQ README TODO
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*
