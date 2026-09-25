# Exa Agent Ultra find-all: 2026 self-propagating supply-chain campaigns

Run agent_run_a276b36425794601a5cf324d62f96469 · effort ultra · created 2026-09-25T17:36:18.148Z · completed 2026-09-25T17:56:02.763Z · stop `schema_satisfied` · cost $9.34. Query and schema in `../../research/inputs/` (raw JSON beside this file). Machine output, not yet editorially verified; every record's `disputed` field is the model's own caveat. Grade against file 11.

## GlassWorm — 2026 extension and repository waves — 2026-01-31

- **Ecosystems:** Open VSX, VS Code-compatible IDE extensions, npm, GitHub repositories, MCP developer tooling, Chrome extensions
- **Propagation:** Developer/publishing credentials stolen through extensions enabled further malicious publications. March delivery used extensionPack/extensionDependencies and compromised repositories; the linked ForceMemo operation used stolen GitHub credentials to force-push malware. An April Zig dropper additionally installed its second-stage extension into other compatible IDEs on the same host. A related March payload installed a Chrome-extension RAT; autonomous browser-extension-to-extension replication was not established.
- **Scale:** January: 4 compromised Open VSX extensions. March: at least 72 additional malicious Open VSX extensions. ForceMemo separately reported 240+ compromised Python repositories. These scopes overlap and are not a count of infected machines.
- **Attribution:** No definitive actor attribution in the cited reports.
- **Disputed:** Qualified inclusion under the requested credential-enabled publication criterion. The Eclipse/Open VSX maintainer explicitly disputed traditional autonomous-worm terminology. First_reported is the first identified 2026-wave report; the parent family was publicly reported in October 2025. ForceMemo and cross-IDE installation are related propagation routes, not additional independent families. The Chrome extension was a payload/delivery component, not a separately proven browser-extension worm.
- **Sources:** https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise · https://socket.dev/blog/open-vsx-transitive-glassworm-campaign · https://www.aikido.dev/blog/glassworm-zig-dropper-infects-every-ide-on-your-machine · https://www.stepsecurity.io/blog/forcememo-hundreds-of-github-python-repos-compromised-via-account-takeover-and-force-push

## SANDWORM_MODE — 2026-02-20

- **Ecosystems:** npm, GitHub Actions, AI coding assistants, MCP
- **Propagation:** Install-time malware steals npm/GitHub credentials, republishes poisoned packages, and injects malicious dependencies/workflows into accessible repositories. SSH provides a fallback; malicious MCP registration and prompt injection target coding assistants.
- **Scale:** At least 19 malicious npm packages associated with two publisher aliases; no defensible total of infected hosts or organizations.
- **Attribution:** Unattributed; the name does not establish a connection to the Russian Sandworm group.
- **Disputed:** Socket documented the worm implementation but did not confirm public propagation through its linked GitHub Action. Not all implemented propagation paths were observed succeeding.
- **Sources:** https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning · https://www.helpnetsecurity.com/2026/02/24/npm-worm-sandworm-mode-supply-cain-attack/

## CanisterWorm — Trivy-seeded npm campaign — 2026-03-20

- **Ecosystems:** npm, GitHub Actions, PyPI
- **Propagation:** The Trivy/CI compromise supplied publishing credentials. deploy.js harvests npm tokens, enumerates packages the victim can publish, injects the payload, increments versions, and automatically republishes. An Internet Computer canister supplies command-and-control indirection. Related TeamPCP credential-theft pivots reached LiteLLM and Telnyx on PyPI; those releases are not independently established Python-republishing worms.
- **Scale:** Socket expanded its initial 29+ package report to 135 malicious artifacts across 64+ unique npm packages. Later reporting reached 141 artifacts across 66+ packages. Workflow references/downloads are exposure, not infections. Related PyPI releases were LiteLLM 1.82.7/1.82.8 and Telnyx 4.87.1/4.87.2.
- **Attribution:** TeamPCP, according to Socket/JFrog and the related incident investigations.
- **Disputed:** The 29+, 64+/135 and 66+/141 figures are successive or differently scoped snapshots, not additive totals. The Trivy seed incident predates the March 20 public worm report.
- **Sources:** https://socket.dev/blog/canisterworm-npm-publisher-compromise-deploys-backdoor-across-29-packages · https://research.jfrog.com/post/canister-worm/ · https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-teampcp-supply-chain-campaign/ · https://www.aikido.dev/blog/telnyx-pypi-compromised-teampcp-canisterworm

## roin-orca/skills — reported self-installing skill — 2026-04-13

- **Ecosystems:** AI-agent skills, skills.sh, Vercel skills CLI
- **Propagation:** A public security issue alleges that reading the fun-brainstorming skill directs the agent to install the same skill collection globally without confirmation. The issue also alleges hostname exfiltration and scanner-targeted prompt injection.
- **Scale:** One reported skill repository/collection; no independently established count of downstream installations, agents or organizations.
- **Attribution:** No verified actor attribution; roin-orca is the repository namespace, not an identified threat actor.
- **Disputed:** Unconfirmed/borderline report, not a proven multi-host worm outbreak. The registry/repository establishes distribution, but the retrieved current skill text does not independently corroborate the alleged self-installing revision. Included as a reported candidate rather than treating the allegation as settled.
- **Sources:** https://github.com/vercel-labs/skills/issues/921 · https://github.com/roin-orca/skills · https://www.skills.sh/roin-orca/skills

## CanisterSprawl — 2026-04-21

- **Ecosystems:** npm, PyPI propagation capability
- **Propagation:** Malicious postinstall code steals npm credentials, discovers writable packages, injects itself into tarballs and republishes them. A separate routine constructs Python .pth payloads and uploads packages with Twine when suitable credentials are present.
- **Scale:** Initial Socket inventory: 16 malicious npm versions across 6 package names. Its subsequently expanded tracker lists 22 artifacts.
- **Attribution:** Unresolved. Socket identifies TeamPCP-style tradecraft/code overlap, not a proven common operator.
- **Disputed:** April 21 is the pgserve disclosure; Socket’s campaign-wide report is April 22. Six packages, 16 initial versions and 22 tracker artifacts are different measures. No confirmed PyPI infection count is established by these sources.
- **Sources:** https://www.stepsecurity.io/blog/pgserve-compromised-on-npm-malicious-versions-harvest-credentials · https://socket.dev/blog/namastex-npm-packages-compromised-canisterworm · https://socket.dev/supply-chain-attacks/canistersprawl

## Shai-Hulud: The Third Coming — Bitwarden CLI — 2026-04-23

- **Ecosystems:** npm, GitHub Actions
- **Propagation:** A poisoned @bitwarden/cli release runs an install-time credential stealer and worm. Stolen npm credentials are used to discover writable packages, modify their tarballs, bump versions and republish; the initial intrusion followed compromised CI credentials.
- **Scale:** One confirmed seed package/version: @bitwarden/cli 2026.4.0, exposed on April 22 for roughly 1.5 hours. No attributable downstream infection total was published.
- **Attribution:** Shai-Hulud/Checkmarx-related supply-chain activity; Bitwarden’s incident statement does not establish a definitive individual operator.
- **Disputed:** April 22 is the incident date, not the April 23 public report. The package’s ordinary download volume is not an infection count.
- **Sources:** https://socket.dev/blog/bitwarden-cli-compromised · https://community.bitwarden.com/t/bitwarden-statement-on-checkmarx-supply-chain-incident/96127 · https://www.endorlabs.com/learn/shai-hulud-the-third-coming----inside-the-bitwarden-cli-2026-4-0-supply-chain-attack

## Mini Shai-Hulud — SAP npm wave — 2026-04-29

- **Ecosystems:** npm, GitHub Actions
- **Propagation:** A Bun-based install payload steals developer/CI credentials, uses npm publishing access to inject and release additional malicious package versions, and plants repository/CI persistence.
- **Scale:** Four compromised npm packages: @cap-js/sqlite, @cap-js/postgres, @cap-js/db-service and mbt.
- **Attribution:** Linked to the Mini Shai-Hulud/TeamPCP campaign by vendor research; this is campaign linkage rather than a separately established operator identity.
- **Disputed:** A wave of the broader Mini Shai-Hulud lineage, not an independent family. Do not add later family-wide totals to this four-package seed count.
- **Sources:** https://www.wiz.io/blog/mini-shai-hulud-supply-chain-sap-npm · https://www.stepsecurity.io/blog/a-mini-shai-hulud-has-appeared

## Mini Shai-Hulud — Lightning and Intercom wave — 2026-04-30

- **Ecosystems:** PyPI, npm, GitHub Actions
- **Propagation:** The worm moved into Python through compromised Lightning releases and continued through Intercom’s npm client. Python execution launches the Bun/JavaScript payload, which harvests publishing/CI credentials and propagates by poisoning additional releases and repositories.
- **Scale:** Lightning: one PyPI project with two malicious versions, 2.6.2 and 2.6.3. The related npm seed was intercom-client 7.0.4. No reliable number of infected organizations.
- **Attribution:** Vendor-linked to Mini Shai-Hulud/TeamPCP.
- **Disputed:** Related cross-ecosystem deployments are grouped here. Lightning’s normal download figures are exposure, not confirmed infections.
- **Sources:** https://socket.dev/blog/lightning-pypi-package-compromised · https://www.endorlabs.com/learn/popular-lightning-pypi-package-backdoored-in-latest-shai-hulud-wave · https://www.stepsecurity.io/blog/shai-hulud-worm-pivots-to-multi-cloud-intercom-client-hijacked

## Mini Shai-Hulud — TanStack/Mistral wave — 2026-05-11

- **Ecosystems:** npm, PyPI, GitHub Actions, VS Code extensions, Open VSX
- **Propagation:** CI/cache poisoning and publishing-token/OIDC theft produced malicious releases with legitimate provenance. Their worm steals credentials and republishes additional packages. A downstream infected contributor exposed the token used to publish the malicious Nx Console extension.
- **Scale:** TanStack initial burst: 84 versions across 42 packages. Expanded npm scope: 373 malicious versions across 169 packages. Downstream extension impact included Nx Console 18.95.0.
- **Attribution:** Mini Shai-Hulud, linked to TeamPCP by the cited investigations.
- **Disputed:** Some reporting gives 171 packages when related PyPI projects are included, versus 169 npm packages. Nx Console is a downstream delivery node, not independently demonstrated to be an extension-republishing worm. Family/wave totals overlap.
- **Sources:** https://socket.dev/blog/tanstack-npm-packages-compromised-mini-shai-hulud-supply-chain-attack · https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem · https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w

## Mini Shai-Hulud — actions-cool GitHub Actions compromise — 2026-05-18

- **Ecosystems:** GitHub Actions, npm propagation capability
- **Propagation:** The attacker redirected mutable action tags to malicious commits. Workflows invoking those tags executed Mini Shai-Hulud, exposing CI credentials and enabling its package/repository propagation. Previously disabled repositories were re-enabled with malicious tags intact in September.
- **Scale:** Two Action repositories: actions-cool/issues-helper with 53 compromised tags and actions-cool/maintain-one-comment with 15. About 15,000 repositories depended on issues-helper; that is potential exposure, not confirmed compromise.
- **Attribution:** Mini Shai-Hulud lineage; no separately verified operator for the September reactivation.
- **Disputed:** The September reactivation began September 16 and was reported by Socket September 24; it is not a newly published worm. Dependent-repository counts must not be presented as infected repositories.
- **Sources:** https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials · https://socket.dev/blog/mini-shai-hulud-actions

## Mini Shai-Hulud — AntV/atool and durabletask wave — 2026-05-19

- **Ecosystems:** npm, PyPI, GitHub Actions
- **Propagation:** Stolen maintainer and CI publishing credentials fed automated package injection and republishing across npm namespaces and Python releases, retaining the Mini Shai-Hulud credential-to-publication loop.
- **Scale:** Socket reported 639 malicious versions across 323 unique npm packages in roughly an hour. The associated durabletask PyPI project had three malicious versions, 1.4.1–1.4.3.
- **Attribution:** Vendor-linked to Mini Shai-Hulud/TeamPCP.
- **Disputed:** Package counts differ: Socket reports 323; JFrog’s expanded inventory reports 325. Treat these as distinct source/snapshot scopes, not a reconciled exact total. Broader Mini Shai-Hulud cumulative totals overlap this wave.
- **Sources:** https://socket.dev/blog/antv-packages-compromised · https://research.jfrog.com/post/shai-hulud-here-we-go-again-may19/ · https://www.wiz.io/blog/mini-shai-hulud-teampcp-hits-antv-supply-chain

## TrapDoor — 2026-05-24

- **Ecosystems:** npm, PyPI, crates.io, AI coding assistants, Git repositories
- **Propagation:** The npm trap-core.js payload includes propagation beyond theft: it reuses stolen SSH keys for lateral movement and injects AI instructions, Git hooks and developer configuration that cause secondary payload installation across projects/hosts. Its AI-context payload describes cross-agent replication. Related Python/Rust packages are delivery/stealing branches, not independently self-replicating samples.
- **Scale:** Socket’s body reports more than 34 packages and 384+ versions/artifacts across the three registries; its updated description says 36 packages. Six unique crate names were identified. Successful secondary-host infections were not quantified.
- **Attribution:** Unattributed; infrastructure/publishing accounts include ddjidd564 and npm account asdxzxc.
- **Disputed:** May 22 is earliest observed package activity; Socket’s actual publication timestamp is May 24. The 34+/36 counts differ within the updated report. Inclusion rests on the npm propagation module; Python and Rust samples are one-shot stealers, and cross-ecosystem linkage is not equally strong at code level.
- **Sources:** https://socket.dev/blog/trapdoor-crypto-stealer-npm-pypi-crates · https://slowmist.medium.com/threat-intelligence-trapdoor-analysis-a-cross-ecosystem-supply-chain-credential-theft-operation-a9a4e11616ea

## Miasma — Red Hat Cloud Services wave — 2026-06-01

- **Ecosystems:** npm, GitHub Actions, VS Code/AI-agent configuration
- **Propagation:** A compromised developer account was used to poison npm packages and repository configuration. The Bun-based worm harvests publishing credentials, injects/re-releases other packages, and plants CI/editor/agent execution hooks to infect additional developer environments.
- **Scale:** Red Hat’s completed investigation identified exactly 32 compromised @redhat-cloud-services npm packages. Research reports counted more than 90 malicious versions.
- **Attribution:** Miasma/Mini Shai-Hulud code lineage; operator unresolved. Shared code is not sufficient to assign every deployment to TeamPCP.
- **Disputed:** Early research counted 29 packages; prefer Red Hat’s final 32-package figure. Red Hat states that released Red Hat products were not affected. Later Miasma waves are listed separately and must not be added to cumulative tracker totals.
- **Sources:** https://access.redhat.com/security/vulnerabilities/RHSB-2026-006 · https://research.jfrog.com/post/shai-hulud-miasma-redhat-cloud-services/ · https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages

## Miasma — Phantom Gyp wave — 2026-06-03

- **Ecosystems:** npm, GitHub Actions, AI coding assistants
- **Propagation:** A malicious binding.gyp triggers execution through npm’s implicit native-build path. The resulting Bun worm steals npm/GitHub/CI credentials, republishes packages, poisons accessible workflows and writes editor/AI-agent configuration hooks.
- **Scale:** 57 npm packages and at least 286 malicious versions in the reported burst.
- **Attribution:** Miasma/Mini Shai-Hulud code lineage; no definitive operator attribution.
- **Disputed:** A technical variant/wave of Miasma, not a separate proven actor. The binding.gyp execution path should not be interpreted as a universal bypass of every package-manager script-disable setting.
- **Sources:** https://www.stepsecurity.io/blog/binding-gyp-npm-supply-chain-attack-spreads-like-worm · https://safedep.io/miasma-worm-ai-coding-agent-config-injection/

## IronWorm — June and July jscrambler waves — 2026-06-03

- **Ecosystems:** npm, GitHub repositories, GitHub Actions, AI coding assistants
- **Propagation:** A native Rust worm steals developer credentials, commits malicious changes into accessible repositories and automates npm publication. The July variant enumerates writable npm packages and prioritizes popular ones; it also poisons local project/agent configuration.
- **Scale:** Initial press inventory: 36 npm packages. JFrog documented 57 backdated malicious commits across nine organizations. The July return included five malicious jscrambler versions plus four plugin packages.
- **Attribution:** Unattributed; shared supply-chain techniques do not prove that IronWorm and Shai-Hulud have the same operator.
- **Disputed:** Package lists expanded during reporting; the 36-package figure is the initial public inventory, not a lifetime family total. The July upload wave began July 11 and JFrog reported it July 12.
- **Sources:** https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/ · https://research.jfrog.com/post/ironworm-returns-rustier-than-ever/ · https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/

## Miasma/Hades — PyPI bioinformatics and MCP waves — 2026-06-07

- **Ecosystems:** PyPI, npm propagation capability, RubyGems propagation capability, GitHub Actions, MCP
- **Propagation:** Malicious wheels use Python startup/import execution to launch Bun/native payloads. The worm steals publishing credentials, modifies and republishes packages, abuses GitHub/OIDC release workflows and implements npm, PyPI and RubyGems propagation.
- **Scale:** June 7: 37 malicious wheels across 19 PyPI projects. The follow-up added 23 artifacts, bringing the broader PyPI branch to 60 artifacts across 37 projects in that snapshot.
- **Attribution:** Miasma/Mini Shai-Hulud lineage, with copycat use; individual operator unresolved.
- **Disputed:** Hades was named in the June 8 follow-on analysis. The 19-project initial set, broader 37-project tracker and other vendors’ Hades-specific lists use different scopes. Some elitexp packages below overlap the tracker. RubyGems is an implemented propagation path, not a confirmed infected-gem count.
- **Sources:** https://socket.dev/blog/mini-shai-hulud-miasma-and-hades-worms-target-bioinformatics-and-mcp-developers-via-malicious · https://socket.dev/blog/shai-hulud-descends-to-hades-miasma-pypi-wave · https://www.stepsecurity.io/blog/the-hades-campaign-pypi-packages

## elitexp Shai-Hulud copycat — 2026-06-08

- **Ecosystems:** PyPI, npm propagation capability, RubyGems propagation capability, GitHub Actions
- **Propagation:** Trojanized/typosquatted Python packages launch a Shai-Hulud-derived payload that steals credentials, injects GitHub workflows and publishes further malicious packages through PyPI, npm and RubyGems credentials.
- **Scale:** Five reported PyPI projects: rlask, tlask, rsquests, nhmpy and mflux-streamlit.
- **Attribution:** Copycat associated with the PyPI account elitexp; GitLab did not establish the original Shai-Hulud operator as responsible.
- **Disputed:** Malicious publishing began June 7; public advisory/campaign evidence was available June 8, and GitLab’s detailed report followed June 9. These projects overlap the broader Hades/Miasma tracker; do not double-count them.
- **Sources:** https://about.gitlab.com/blog/shai-hulud-copycat-campaign-targets-python-developers/ · https://socket.dev/blog/shai-hulud-descends-to-hades-miasma-pypi-wave · https://advisories.gitlab.com/pypi/rlask/GMS-2026-572/

## Miasma — codfish/semantic-release-action compromise — 2026-06-24

- **Ecosystems:** GitHub Actions, npm/PyPI/RubyGems propagation capability
- **Propagation:** Compromised action tags run an obfuscated payload in CI, steal GitHub/OIDC and publishing credentials, and attempt to backdoor other accessible repositories. The payload carries Miasma’s multi-ecosystem propagation and public-commit command-channel code.
- **Scale:** One GitHub Action repository with multiple compromised tags; no verified total of infected downstream repositories.
- **Attribution:** Miasma toolkit reuse. Aikido notes the toolkit was public, so its markers do not identify a unique operator.
- **Disputed:** Tag counts are unresolved: StepSecurity describes seven initial tags, Aikido lists sixteen across two malicious commits, and other page passages describe a broader tag set. Use one confirmed Action repository rather than pretending these are reconciled. Propagation attempts are documented; success count is not.
- **Sources:** https://www.stepsecurity.io/blog/supply-chain-compromise-codfish-semantic-release-action · https://www.aikido.dev/blog/compromised-github-action-codfish-steals-secrets · https://sean.dev/2026/06/codfish/semantic-release-action-compromised/

## Miasma — LeoPlatform/Backstage and related June wave — 2026-06-25

- **Ecosystems:** npm, GitHub Actions, VS Code configuration, Go module distribution
- **Propagation:** Stolen npm/GitHub tokens were used for burst publication and malicious Dependabot-disguised workflows. binding.gyp launches the credential-stealing, self-republishing Miasma payload. A related Go archive carried a .vscode folder-open execution hook, rather than a Go compiler exploit.
- **Scale:** SafeDep: 20 LeoPlatform/LeoInsights packages, at least three poisoned repositories; June 26 update added four @immobiliarelabs Backstage packages, for 24 npm packages. Socket’s related inventory counted 23 npm packages plus one Go artifact.
- **Attribution:** Miasma toolkit; actor unresolved.
- **Disputed:** Public report June 25; LeoPlatform malicious publishing occurred June 24. SafeDep’s 24 and Socket’s 23 are differently scoped inventories: the former adds Backstage packages; the latter includes another npm namespace and a Go artifact. They must not be summed.
- **Sources:** https://safedep.io/miasma-worm-hits-leoplatform-20-npm-packages · https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem

## Joyfill npm-CLI worm-loop campaign — 2026-07-28

- **Ecosystems:** npm, Git repositories
- **Propagation:** The compromised packages install an obfuscated RAT and patch the local npm CLI. Subsequent npm commands rerun the loader, and packages built/published from the infected environment can carry it onward, producing the documented worm-like publication loop.
- **Scale:** Two packages, @joyfill/components and @joyfill/layouts, with three malicious beta versions each: six versions total.
- **Attribution:** Payload similarities to DEV#POPPER/PolinRider-style tooling; no definitive actor attribution established for this deployment.
- **Disputed:** Qualified worm-capable inclusion: the analysis documents the npm-CLI propagation loop, but does not quantify independently observed downstream republishing. RAT functionality alone would not qualify.
- **Sources:** https://www.stepsecurity.io/blog/joyfill-npm-supply-chain-compromise · https://socket.dev/blog/polinrider-github-packagist

## ChainDrop — 2026-08-04

- **Ecosystems:** npm, GitHub Actions, VS Code/AI-agent configuration
- **Propagation:** Stolen npm tokens and CI/OIDC credentials enable enumeration of writable packages, injection of preinstall/Bun payloads, version bumps and automatic republishing. Repository/editor/agent hooks provide persistence and additional execution paths.
- **Scale:** Best expanded inventory: 444 package names and 2,234 malicious versions. Microsoft reported more than 400 packages. Earlier published snapshots counted 444 packages with 1,381 or 2,212 versions.
- **Attribution:** Shai-Hulud/Mini Shai-Hulud lineage; not a conclusively identified operator in Microsoft’s technical analysis.
- **Disputed:** Version counts differ by inventory/snapshot. A contemporaneous press report says 868 packages, while the Aikido page it cites says 444; that package-count discrepancy is unresolved and 868 is not adopted. Download totals are exposure, not infections.
- **Sources:** https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/ · https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack · https://github.com/ossf/malicious-packages/pull/1426 · https://www.stepsecurity.io/blog/chaindrop-npm-worm

## Trinitite — 2026-08-28

- **Ecosystems:** npm, PyPI propagation capability, RubyGems propagation capability, GitHub Actions
- **Propagation:** An abused release workflow published a self-replicating payload with valid provenance. The worm harvests and validates publishing credentials and implements package modification/republication for npm, PyPI and RubyGems; binding.gyp provides an execution route.
- **Scale:** One confirmed npm seed package, @7nohe/openapi-react-query-codegen, with ten malicious versions published in roughly 20 minutes.
- **Attribution:** Unresolved; Shai-Hulud/Miasma-derived behavior is not proof of a common operator.
- **Disputed:** Ten versions does not mean ten packages. Reports distinguish bootstrap and full-worm releases. No confirmed downstream PyPI/RubyGems package total was established.
- **Sources:** https://www.endorlabs.com/learn/trojanized-7nohe-openapi-react-query-codegen-adds-pypi-to-a-self-replicating-npm-worm · https://research.jfrog.com/post/shai-hulud-trinitite/ · https://www.socket.dev/blog/openapi-react-query-codegen-npm-compromise

## Mini Shai-Hulud — September payload reactivation — 2026-09-07

- **Ecosystems:** npm, MCP developer tooling
- **Propagation:** Previously observed worm code reappeared in newly published package versions, retaining credential harvesting and automated poisoning/republishing of packages accessible to the infected developer.
- **Scale:** Four malicious versions: feishu-docx-mcp 0.3.2, bmc-i18n-extract-cli 1.1.1, blueai-cli 0.7.0 and bmc-translate-utils 1.1.1.
- **Attribution:** Shai-Hulud code reuse; no new actor attribution.
- **Disputed:** A reactivation/new publication wave, not a new malware family. The 319 older versions sharing the payload hash and 639 versions in a broader May wave are historical, non-additive measures.
- **Sources:** https://www.aikido.dev/blog/shai-hulud-npm-resurfaces · https://www.itpro.com/security/malware/is-shai-hulud-back-researchers-spot-wormy-boy-slipping-past-npm-malware-scanning-features

## XCSSET — Flutter/pub.dev build-hook propagation — 2026-09-08

- **Ecosystems:** Dart/pub.dev, Git repositories, Xcode projects, Android Gradle projects
- **Propagation:** An infected maintainer machine caused malicious build hooks to ship in a Flutter package. XCSSET infects Android Gradle and Xcode projects and Git hooks; another developer who clones/builds an infected example/project executes the worm, which can seed further projects and publications.
- **Scale:** One confirmed pub.dev project, universal_file_viewer. Aikido analyzed 0.1.5; Corgea identified retracted 0.1.5 and 0.1.6 releases. No reliable infected-machine total.
- **Attribution:** XCSSET malware family; operator not identified in these reports.
- **Disputed:** Included as an additional software-supply-chain/IDE-project ecosystem beyond the named registries. This is a new 2026 distribution wave of an older family. Ordinary dependency use does not execute the infected example build files; building the example/project is required.
- **Sources:** https://www.aikido.dev/blog/compromised-flutter-package-on-pub-dev-contains-xcsset-malware · https://corgea.com/research/universal-file-viewer-pub-dev-xcsset-september-2026

## Shai-Hulud — AI coding-session hijack at an unnamed SaaS provider — 2026-09-16

- **Ecosystems:** AI coding assistants, PyPI, GitHub repositories
- **Propagation:** An attacker-controlled package recommendation in a hijacked active coding-assistant session led to a poisoned PyPI installation and GitHub OAuth-token theft. The attacker deployed Shai-Hulud across internal repositories, then poisoned a package in the victim’s own namespace, causing another employee’s downstream infection.
- **Scale:** Approximately 100 internal code repositories at one unnamed SaaS provider; a secondary package-mediated employee infection is explicitly described.
- **Attribution:** Unidentified actor in Mandiant’s incident-response case study.
- **Disputed:** September 16 is the public report date. The intrusion date, package names and assistant-session hijack method were not disclosed. This is a separately reported deployment of an existing worm, not a newly named family.
- **Sources:** https://cloud.google.com/security/resources/ai-risk-and-resilience-2026 · https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html

## supplychain.local / sckit — MemTensor cross-ecosystem worm — 2026-09-23

- **Ecosystems:** npm, PyPI, GitHub Actions, OpenClaw/AI-agent plugins
- **Propagation:** Compromised MemTensor packages deliver native Go payloads that steal CI/publishing credentials and implement direct npm/PyPI republishing plus GitHub workflow injection, allowing infected publishing environments to seed additional releases.
- **Scale:** Two package projects: three npm versions of @memtensor/memos-cloud-openclaw-plugin (0.1.21, 0.1.23, 0.1.25) and PyPI MemoryOS 2.0.34. Six platform-specific native binaries are payload builds, not six victims.
- **Attribution:** No definitive operator attribution.
- **Disputed:** Worm-capable deployed malware, but Aikido explicitly did not observe public downstream republished victims or successful injected-workflow propagation. No organization/infection total is established.
- **Sources:** https://www.aikido.dev/blog/supplychain-local-memtensor-npm-pypi · https://socket.dev/blog/memtensor-compromise

---
26 campaign/wave records, including one explicitly unconfirmed skills report. Related waves are identified rather than presented as independent malware families. Counts are not additive; conflicting figures, exposure versus infection, and implemented propagation versus observed downstream spread are flagged in each record’s disputed field.