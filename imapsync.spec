Summary:	IMAP synchronisation, sync, copy or migration tool
Name:		imapsync
Version:	1.945
Release:	1
License:	WTFPL
Group:		Networking/Mail
URL:		https://ks.lamiral.info/imapsync/
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



%changelog
* Tue Feb 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.480-1
+ Revision: 771610
- version update 1.480

* Fri Dec 23 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.476-1
+ Revision: 744783
- tgz archive added
- version update 1.476

* Mon Nov 28 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.468-1
+ Revision: 734994
- version update 1.468

* Sat Oct 15 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.456-2
+ Revision: 704765
- new suggetions

* Fri Oct 14 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.456-1
+ Revision: 704710
- 1.456

* Sun Jun 19 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.446-2
+ Revision: 686066
- New requires

* Fri Jun 17 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.446-1
+ Revision: 685737
- 1.446 do what the f**k to it accordidng license

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.315-2mdv2011.0
+ Revision: 611181
- rebuild

* Mon Jun 14 2010 Frederic Crozat <fcrozat@mandriva.com> 1.315-1mdv2010.1
+ Revision: 548022
- Release 1.315

* Mon Jun 07 2010 Frederic Crozat <fcrozat@mandriva.com> 1.311-1mdv2010.1
+ Revision: 547204
- Release 1.311
- Change license to WTFPL

* Wed Aug 05 2009 Frederik Himpe <fhimpe@mandriva.org> 1.286-1mdv2010.0
+ Revision: 410346
- Update to new verison 1.286
- Remove authuser patch: not needed anymomre

* Sun Mar 08 2009 Frederik Himpe <fhimpe@mandriva.org> 1.267-2mdv2009.1
+ Revision: 352933
- Add authuser patch from Fedora to make it play more nicely with
  Mail::IMAPClient 3 (might fix bug #48018)

* Thu Feb 19 2009 Frederik Himpe <fhimpe@mandriva.org> 1.267-1mdv2009.1
+ Revision: 343008
- update to new version 1.267

* Sat Aug 16 2008 Frederik Himpe <fhimpe@mandriva.org> 1.260-1mdv2009.0
+ Revision: 272541
- Update to new version 1.260
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.252-2mdv2009.0
+ Revision: 267121
- rebuild early 2009.0 package (before pixel changes)

* Sun May 11 2008 Frederik Himpe <fhimpe@mandriva.org> 1.252-1mdv2009.0
+ Revision: 205953
- New version
- Adapt to new license policy

  + Erwan Velu <erwan@mandriva.org>
    - 1.249
    - 1.249

* Sun Feb 10 2008 Frederic Crozat <fcrozat@mandriva.com> 1.241-1mdv2008.1
+ Revision: 164755
- Release 1.241

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 04 2007 Frederic Crozat <fcrozat@mandriva.com> 1.233-1mdv2008.1
+ Revision: 105714
- Release 1.233
- Add explicit requires on perl-DateManip
- import imapsync

