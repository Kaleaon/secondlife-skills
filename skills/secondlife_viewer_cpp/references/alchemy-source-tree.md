# Alchemy Source Tree (generated from AlchemyViewer/Alchemy @develop)

Complete file index of https://github.com/AlchemyViewer/Alchemy (12338 files). Use it to locate the exact file for a subsystem before fetching or cloning it. Paths are grouped by directory.


## ./ (14 files)

- `.clang-format`

- `.editorconfig`

- `.gersemirc`

- `.git-blame-ignore-revs`

- `.gitattributes`

- `.gitignore`

- `.gitmodules`

- `.pre-commit-config.yaml`

- `CLAUDE.md`

- `CONTRIBUTING.md`

- `LICENSE`

- `README.md`

- `dotnet-tools.json`

- `requirements.txt`


## .github/ (5 files)

- `actionlint.yaml`

- `dependabot.yaml`

- `labeler.yaml`

- `pull_request_template.md`

- `release.yaml`


## .github/ISSUE_TEMPLATE/ (4 files)

- `10-bug.yaml`

- `20-enhancement.yaml`

- `30-blank.yaml`

- `config.yml`


## .github/actions/python-tools/ (1 files)

- `action.yaml`


## .github/actions/setup-build/ (1 files)

- `action.yaml`


## .github/codeql/ (1 files)

- `codeql-config.yaml`


## .github/workflows/ (7 files)

- `build.yaml`

- `check-pr.yaml`

- `codeql.yaml`

- `label.yaml`

- `lint-workflows.yaml`

- `sanitizers.yaml`

- `tag-release.yaml`


## doc/ (14 files)

- `ARCHITECTURE.md`

- `BUILD.md`

- `LGPL-license.txt`

- `LICENSE-logos.txt`

- `LICENSE-source.txt`

- `LIGHTBOX.md`

- `TESTING.md`

- `VCPKG-R2.md`

- `alchemy_logo.png`

- `contributions.txt`

- `external-editor-json-rpc.md`

- `releasenotes-where.txt`

- `supporters.txt`

- `translations.txt`


## doc/mesh/ (1 files)

- `object-origins.md`


## doc/mesh/images/ (1 files)

- `uploader-pivot.png`


## doc/testplans/ (10 files)

- `PRIM_MEDIA_FIRST_CLICK_INTERACT.md`

- `RenderMaxTextureResolution.md`

- `hdri_local_preview.md`

- `material_preview.md`

- `optimize_away_alpha.md`

- `pbr_materials.md`

- `pbr_terrain_appearance.md`

- `pbr_terrain_composition.md`

- `pbr_terrain_paintmap.md`

- `terrain_loading.md`


## indra/ (4 files)

- `CMakeLists.txt`

- `CMakePresets.json`

- `vcpkg-configuration.json`

- `vcpkg.json`


## indra/aloracle/ (14 files)

- `CMakeLists.txt`

- `aloracle.cpp`

- `aloracle.h`

- `aloracle_lldate.cpp`

- `aloracle_llmessage.cpp`

- `aloracle_llnamevalue.cpp`

- `aloracle_llpartdata.cpp`

- `aloracle_llprimitive.cpp`

- `aloracle_llquantize.cpp`

- `aloracle_llsd.cpp`

- `aloracle_lluri.cpp`

- `aloracle_patch.cpp`

- `aloracle_tinygltf.cpp`

- `aloracleboundary.h`


## indra/aloracle/tests/ (1 files)

- `aloracle_test.cpp`


## indra/alrender/ (41 files)

- `CMakeLists.txt`

- `alcutoutimage.cpp`

- `alcutoutimage.h`

- `aldepthpyramid.cpp`

- `aldepthpyramid.h`

- `alfarplane.cpp`

- `alfarplane.h`

- `alframeend.h`

- `alhexlattice.h`

- `alhuddepth.h`

- `allightmapblur.cpp`

- `allightmapblur.h`

- `alondemandtarget.cpp`

- `alondemandtarget.h`

- `alprobeeclipse.cpp`

- `alprobeeclipse.h`

- `alrenderinputrequests.cpp`

- `alrenderinputrequests.h`

- `alrenderresourceinputs.h`

- `alrenderresourceplan.cpp`

- `alrenderresourceplan.h`

- `alshaderinputs.cpp`

- `alshaderinputs.h`

- `alskycube.cpp`

- `alskycube.h`

- `alskylayers.cpp`

- `alskylayers.h`

- `alspotshadowcache.cpp`

- `alspotshadowcache.h`

- `alstarfield.cpp`

- `alstarfield.h`

- `alstarfieldgenerate.h`

- `altransienttargetpool.cpp`

- `altransienttargetpool.h`

- `altransienttargets.cpp`

- `altransienttargets.h`

- `alwaterfield.cpp`

- `alwaterfield.h`

- `alwaterheightbake.cpp`

- `alwaterheightbake.h`

- `alwaterstencil.h`


## indra/alrender/tests/ (37 files)

- `alcompute_gl_bench.cpp`

- `alcutoutimage_test.cpp`

- `alfarplane_test.cpp`

- `alframeend_test.cpp`

- `alhuddepth_gl_test.cpp`

- `allightmapblur_gl_scene.h`

- `allightmapblur_gl_test.cpp`

- `alondemandtarget_bench.cpp`

- `alondemandtarget_gl_test.cpp`

- `alprobeeclipse_test.cpp`

- `alrenderinputrequests_test.cpp`

- `alrenderresourceplan_test.cpp`

- `alshaderinputs_test.cpp`

- `alskycomposite_gl_test.cpp`

- `alskycube_gl_test.cpp`

- `alskycube_test.cpp`

- `alskydome_gl_test.cpp`

- `alskylayers_gl_test.cpp`

- `alskylayers_test.cpp`

- `alskyraster_gl.h`

- `alspotshadowcache_gl_test.cpp`

- `alspotshadowcache_test.cpp`

- `alstarfield_bench.cpp`

- `alstarfield_draws.h`

- `alstarfield_gl_bench.cpp`

- `alstarfield_gl_test.cpp`

- `alstarfield_test.cpp`

- `altransienttargetpool_gl_test.cpp`

- `altransienttargetpool_test.cpp`

- `alwaterfield_test.cpp`

- `alwaterheightbake_test.cpp`

- `alwatersurface_gl_test.cpp`

- `alwatertargets_bench.cpp`

- `fxaa_gl_test.cpp`

- `reflectionprobe_gl_bench.cpp`

- `reflectionprobe_gl_scene.h`

- `reflectionprobe_gl_test.cpp`


## indra/alrender/tests/skyraster/deferred/ (13 files)

- `auroraF.glsl`

- `auroraV.glsl`

- `cloudsF.glsl`

- `cloudsV.glsl`

- `ditherEmissiveF.glsl`

- `meteorsF.glsl`

- `meteorsV.glsl`

- `moonF.glsl`

- `moonV.glsl`

- `skyF.glsl`

- `skyV.glsl`

- `sunDiscF.glsl`

- `sunDiscV.glsl`


## indra/alscript/ (1 files)

- `CMakeLists.txt`


## indra/alscript/core/ (24 files)

- `almessagemap.cpp`

- `almessagemap.h`

- `alnotecardformat.cpp`

- `alnotecardformat.h`

- `alscriptengine.h`

- `alscriptformatter.cpp`

- `alscriptformatter.h`

- `alscriptlexicon.cpp`

- `alscriptlexicon.h`

- `alscriptmessages.cpp`

- `alscriptmessages.h`

- `alscriptnameindex.cpp`

- `alscriptnameindex.h`

- `alscriptoutlinepairs.cpp`

- `alscriptoutlinepairs.h`

- `alscriptproblem.h`

- `alscriptspan.h`

- `alscriptstack.cpp`

- `alscriptstack.h`

- `alscriptsymbol.h`

- `alscripttempfiles.cpp`

- `alscripttempfiles.h`

- `alscriptweight.cpp`

- `alscriptweight.h`


## indra/alscript/fuzz/ (2 files)

- `alscriptfuzzformat.cpp`

- `alscriptfuzzlsl.cpp`


## indra/alscript/lint/ (8 files)

- `allsllintpass.cpp`

- `allsllintpass.h`

- `alscriptfixes.cpp`

- `alscriptfixes.h`

- `alscriptlintpass.cpp`

- `alscriptlintpass.h`

- `alselenefilters.cpp`

- `alselenefilters.h`


## indra/alscript/lsl/ (24 files)

- `allslcommentcode.cpp`

- `allslcommentcode.h`

- `allslcomments.cpp`

- `allslcomments.h`

- `allslconsts.cpp`

- `allslconsts.h`

- `allsldepth.cpp`

- `allsldepth.h`

- `allsleffects.cpp`

- `allsleffects.h`

- `allsleventtext.inc`

- `allslexports.cpp`

- `allslexports.h`

- `allslitemargs.inc`

- `allslservice.cpp`

- `allslservice.h`

- `allsltoslua.cpp`

- `allsltoslua.h`

- `allsltraits.cpp`

- `allsltraits.h`

- `allsltraits.inc`

- `allsluuids.inc`

- `allslvalues.cpp`

- `allslvalues.h`


## indra/alscript/lsl/optimizer/ (34 files)

- `allslbranches.cpp`

- `allslbranches.h`

- `allslconstantglobals.cpp`

- `allslconstantglobals.h`

- `allslcosts.cpp`

- `allslcosts.h`

- `allsldeadcode.cpp`

- `allsldeadcode.h`

- `allslflowvalues.cpp`

- `allslflowvalues.h`

- `allslfolder.cpp`

- `allslfolder.h`

- `allslglobals.cpp`

- `allslglobals.h`

- `allslinliner.cpp`

- `allslinliner.h`

- `allsllibraryfold.cpp`

- `allsllibraryfold.h`

- `allslnames.cpp`

- `allslnames.h`

- `allsloptimizer.cpp`

- `allsloptimizer.h`

- `allsloptimizerpass.cpp`

- `allsloptimizerpass.h`

- `allslprinter.cpp`

- `allslprinter.h`

- `allslrepeatedcalls.cpp`

- `allslrepeatedcalls.h`

- `allslshapes.cpp`

- `allslshapes.h`

- `allslsignatures.cpp`

- `allslsignatures.h`

- `allslsimplifier.cpp`

- `allslsimplifier.h`


## indra/alscript/luau/ (22 files)

- `alluaucompletion.cpp`

- `alluaucompletion.h`

- `alluauconfig.cpp`

- `alluauconfig.h`

- `alluauconfigscript.cpp`

- `alluauconfigscript.h`

- `alluauexports.cpp`

- `alluauexports.h`

- `alluaufragment.cpp`

- `alluaufragment.h`

- `alluaufrontend.cpp`

- `alluaufrontend.h`

- `alluaunavigation.cpp`

- `alluaunavigation.h`

- `alluauservice.cpp`

- `alluauservice.h`

- `alluaushadowed.cpp`

- `alluaushadowed.h`

- `alluausharedstart.cpp`

- `alluausharedstart.h`

- `alluautypes.cpp`

- `alluautypes.h`


## indra/alscript/masters/ (18 files)

- `almasterburst.cpp`

- `almasterburst.h`

- `almasterclock.cpp`

- `almasterclock.h`

- `almasterdeletes.cpp`

- `almasterdeletes.h`

- `almasterindex.cpp`

- `almasterindex.h`

- `almasterlinks.cpp`

- `almasterlinks.h`

- `almastermatch.cpp`

- `almastermatch.h`

- `almasterplan.cpp`

- `almasterplan.h`

- `almasterqueue.cpp`

- `almasterqueue.h`

- `almasterwatch.cpp`

- `almasterwatch.h`


## indra/alscript/preprocessor/ (27 files)

- `aldiskcache.cpp`

- `aldiskcache.h`

- `aldiskincludes.cpp`

- `aldiskincludes.h`

- `alincludeidentity.cpp`

- `alincludeidentity.h`

- `alincludesearch.cpp`

- `alincludesearch.h`

- `allinelabel.cpp`

- `allinelabel.h`

- `almodulelook.cpp`

- `almodulelook.h`

- `alpreprocessor.cpp`

- `alpreprocessor.h`

- `alrequirenavigation.cpp`

- `alrequirenavigation.h`

- `alscriptenvelope.cpp`

- `alscriptenvelope.h`

- `alscriptjoblane.h`

- `alscriptsnapshot.cpp`

- `alscriptsnapshot.h`

- `alscripttextcache.cpp`

- `alscripttextcache.h`

- `alsourcemap.cpp`

- `alsourcemap.h`

- `aluploadheader.cpp`

- `aluploadheader.h`


## indra/alscript/tests/ (49 files)

- `aldiskcache_test.cpp`

- `aldiskincludes_test.cpp`

- `alincludeidentity_test.cpp`

- `alincludesearch_test.cpp`

- `allinelabel_test.cpp`

- `allslcommentcode_test.cpp`

- `allslcomments_test.cpp`

- `allslconsts_test.cpp`

- `allslcosts_test.cpp`

- `allsleffects_test.cpp`

- `allsloptimizer_test.cpp`

- `allslservice_test.cpp`

- `allsltoslua_test.cpp`

- `alluauconfig_test.cpp`

- `alluaufragment_test.cpp`

- `alluaunavigation_test.cpp`

- `alluauservice_test.cpp`

- `almasterburst_test.cpp`

- `almasterdeletes_test.cpp`

- `almasterindex_test.cpp`

- `almasterlinks_test.cpp`

- `almastermatch_test.cpp`

- `almasterplan_test.cpp`

- `almasterqueue_test.cpp`

- `almasterwatch_test.cpp`

- `almessagemap_test.cpp`

- `almodulelook_test.cpp`

- `alnotecardformat_test.cpp`

- `alpreprocessor_test.cpp`

- `alpreprocessorc11_test.cpp`

- `alscript_bench.cpp`

- `alscript_test_checks.cpp`

- `alscriptenvelope_test.cpp`

- `alscriptfixes_test.cpp`

- `alscriptformatter_test.cpp`

- `alscripthostile_test.cpp`

- `alscriptjoblane_test.cpp`

- `alscriptlexicon_test.cpp`

- `alscriptlintpass_test.cpp`

- `alscriptmessages_test.cpp`

- `alscriptnameindex_test.cpp`

- `alscriptoutlinepairs_test.cpp`

- `alscriptsnapshot_test.cpp`

- `alscriptstack_test.cpp`

- `alscripttempfiles_test.cpp`

- `alscripttextcache_test.cpp`

- `alscriptweight_test.cpp`

- `alsourcemap_test.cpp`

- `aluploadheader_test.cpp`


## indra/alscript/tests/optimizer/ (6 files)

- `test_lso.lsl`

- `test_lso_expected.lsl`

- `test_shrink.lsl`

- `test_shrink_expected.lsl`

- `test_vendor.lsl`

- `test_vendor_expected.lsl`


## indra/alscript/tests/preprocessor/ (42 files)

- `test_compress.lsl`

- `test_compress_expected.lsl`

- `test_conditionals.lsl`

- `test_conditionals_expected.lsl`

- `test_include.lsl`

- `test_include_expected.lsl`

- `test_lazy_lists.lsl`

- `test_lazy_lists_expected.lsl`

- `test_linkset.lsl`

- `test_linkset_expected.lsl`

- `test_macros.lsl`

- `test_macros_expected.lsl`

- `test_nexiilsl_app_uri.lsl`

- `test_nexiilsl_app_uri_expected.lsl`

- `test_nexiilsl_damage_types.lsl`

- `test_nexiilsl_damage_types_expected.lsl`

- `test_nexiilsl_inverse_kinematics.lsl`

- `test_nexiilsl_inverse_kinematics_expected.lsl`

- `test_nexiilsl_linkset.lsl`

- `test_nexiilsl_linkset_expected.lsl`

- `test_nexiilsl_remote_linkset_data.lsl`

- `test_nexiilsl_remote_linkset_data_bare.lsl`

- `test_nexiilsl_remote_linkset_data_bare_expected.lsl`

- `test_nexiilsl_remote_linkset_data_expected.lsl`

- `test_nexiilsl_rez_queue_check.lsl`

- `test_nexiilsl_rez_queue_check_expected.lsl`

- `test_nexiilsl_roundabout.lsl`

- `test_nexiilsl_roundabout_expected.lsl`

- `test_nexiilsl_string_compression.lsl`

- `test_nexiilsl_string_compression_expected.lsl`

- `test_nexiilsl_sync_lsd.lsl`

- `test_nexiilsl_sync_lsd_expected.lsl`

- `test_nexiilsl_texture.lsl`

- `test_nexiilsl_texture_expected.lsl`

- `test_nexiilsl_utilities.lsl`

- `test_nexiilsl_utilities_expected.lsl`

- `test_require.luau`

- `test_require_expected.luau`

- `test_strings.lsl`

- `test_strings_expected.lsl`

- `test_switch.lsl`

- `test_switch_expected.lsl`


## indra/alscript/tests/preprocessor/include/ (6 files)

- `common.lsl`

- `config.lsl`

- `deep.luau`

- `linkset.LICENSE`

- `linkset.lsl`

- `util.luau`


## indra/alscript/tests/preprocessor/include/NexiiLSL/ (10 files)

- `LICENSE`

- `app-uri.lsl`

- `damage-types.lsl`

- `inverse-kinematics.lsl`

- `linkset.lsl`

- `remote-linkset-data.lsl`

- `string-compression.lsl`

- `texture.lsl`

- `time.lsl`

- `utilities.lsl`


## indra/alscript/tests/preprocessor/include/NexiiLSL/scripts/ (3 files)

- `rez-queue-check.lsl`

- `roundabout.lsl`

- `sync-lsd.lsl`


## indra/alscript/tests/regressions/ (4 files)

- `deep_braces.lsl`

- `deep_call_line.lsl`

- `deep_do_blocks.luau`

- `deep_parentheses.lsl`


## indra/alscript/tests/tailslide/ (2 files)

- `LICENSE`

- `README.md`


## indra/alscript/tests/tailslide/scripts/ (92 files)

- `assignments.lsl`

- `bad_globals.lsl`

- `binary_expressions.lsl`

- `branching.lsl`

- `camera_demo.lsl`

- `casts.lsl`

- `check_all_return.lsl`

- `color-change.lsl`

- `compound_assignment.lsl`

- `constant_expressions.lsl`

- `constant_simplifier_test.lsl`

- `constants.lsl`

- `constprop.lsl`

- `declaration_expressions.lsl`

- `deprecated_function.lsl`

- `desugaring.lsl`

- `duplicate_labels.lsl`

- `error1.lsl`

- `event_handler_order.lsl`

- `event_handlers.lsl`

- `events.lsl`

- `fancy_expr_replacement.lsl`

- `forloops.lsl`

- `fpinc.lsl`

- `function_calls.lsl`

- `fwcheck1.lsl`

- `global_list_refs.lsl`

- `global_negation.lsl`

- `hex.lsl`

- `illegal_cast.lsl`

- `implied_return.lsl`

- `infinity_repr.lsl`

- `invalid_decl.lsl`

- `irc-4.lsl`

- `jump_annotations.lsl`

- `jump_kinds.lsl`

- `key_inlining.lsl`

- `label_shadowing.lsl`

- `lenient_salist.lsl`

- `libhttpdb.lsl`

- `list_append_void.lsl`

- `ll_global_rules.lsl`

- `logmessage_test.lsl`

- `lsl_conformance.lsl`

- `lsl_conformance2.lsl`

- `lso_jump_behavior.lsl`

- `lvalue.lsl`

- `many_statements.lsl`

- `mms_player.lsl`

- `more_expressions.lsl`

- `nested_lists.lsl`

- `num_literals.lsl`

- `parser_abuse.lsl`

- `parserstackdepth.lsl`

- `parserstackdepth2.lsl`

- `parserstackdepth3.lsl`

- `pathological_expression.lsl`

- `precluded_globals.lsl`

- `print_expression.lsl`

- `print_no_shadowing.lsl`

- `print_type_bug.lsl`

- `push_omission.lsl`

- `retval.lsl`

- `rvalue_assignments.lsl`

- `scope1.lsl`

- `scope2.lsl`

- `scope3.lsl`

- `scope4.lsl`

- `simple_binops.lsl`

- `simple_declarations.lsl`

- `simple_expr_replacement.lsl`

- `simple_function_defs.lsl`

- `stack_heap_collide.lsl`

- `state_change.lsl`

- `streamcomment.lsl`

- `strict_salist.lsl`

- `sub_replacement.lsl`

- `test1.lsl`

- `test2.lsl`

- `two_states.lsl`

- `type_error_no_assert.lsl`

- `unixtime.lsl`

- `various_globals.lsl`

- `vconst.lsl`

- `vector_ambiguity.lsl`

- `vector_products.lsl`

- `void_return.lsl`

- `warning1.lsl`

- `warning2.lsl`

- `weirdscope-jump.lsl`

- `xnary_expressions.lsl`

- `xytext1.2.lsl`


## indra/alscript/tests/tailslide/scripts/apotheus_vendor/ (1 files)

- `main.lsl`


## indra/alscript/tests/tailslide/scripts/bugs/ (26 files)

- `0001.lsl`

- `0002.lsl`

- `0003.lsl`

- `0004.lsl`

- `0005.lsl`

- `0006.lsl`

- `0007.lsl`

- `0008.lsl`

- `0009.lsl`

- `0010.lsl`

- `0011.lsl`

- `0012.lsl`

- `0013.lsl`

- `0014.lsl`

- `0015.lsl`

- `0016.lsl`

- `0017.lsl`

- `0018.lsl`

- `0019.lsl`

- `0020.lsl`

- `0021.lsl`

- `0022.lsl`

- `bad-for-exprs.lsl`

- `mutable_global_rvalue.lsl`

- `typecast_builtin.lsl`

- `unary_minus_glob_bad_sym.lsl`


## indra/alscript/tests/tailslide/scripts/tltp/ (3 files)

- `browser.lsl`

- `exporter.lsl`

- `server.lsl`


## indra/cmake/ (54 files)

- `00-COMPILE-LINK-RUN.txt`

- `00-Common.cmake`

- `ALAddTestBinary.cmake`

- `APR.cmake`

- `AlIntrinsicCheck.cmake`

- `AlSimdAsmCheck.cmake`

- `AlchemyTarget.cmake`

- `Attribution.cmake`

- `Boost.cmake`

- `BootstrapVcpkg.cmake`

- `BuildVersion.cmake`

- `CEFPlugin.cmake`

- `CMakeLists.txt`

- `CURL.cmake`

- `ConfigurationReport.cmake`

- `ContributorNames.cmake`

- `DBUS.cmake`

- `Dependencies.cmake`

- `Discord.cmake`

- `FMODSTUDIO.cmake`

- `FindPipeWire.cmake`

- `GLIB.cmake`

- `GStreamer10Plugin.cmake`

- `Harfbuzz.cmake`

- `Hunspell.cmake`

- `ICU.cmake`

- `LibVLCPlugin.cmake`

- `Linking.cmake`

- `NDOF.cmake`

- `PluginAPI.cmake`

- `Pnj2k.cmake`

- `Pnj2kAudit.cmake`

- `Python.cmake`

- `RetiredOptions.cmake`

- `SDL3.cmake`

- `Sentry.cmake`

- `TemplateCheck.cmake`

- `Tracy.cmake`

- `UI.cmake`

- `Variables.cmake`

- `Velopack.cmake`

- `VerifyTemplate.cmake`

- `ViewerAppDir.cmake`

- `ViewerCodeSign.cmake`

- `ViewerInstall.cmake`

- `ViewerPackage.cmake`

- `ViewerPackageConfig.cmake`

- `ViewerPackageLinux.cmake`

- `ViewerSource.cmake`

- `ViewerStrip.cmake`

- `ViewerSymbols.cmake`

- `ViewerSystemPackage.cmake`

- `WebRTC.cmake`

- `attribution.json`


## indra/cmake/presets/ (5 files)

- `base.json`

- `generate.py`

- `ninja.json`

- `vs2026.json`

- `xcode.json`


## indra/cmake/toolchains/ (1 files)

- `linux-clang.cmake`


## indra/cmake/triplets/ (32 files)

- `alchemy-base.cmake`

- `alchemy-sanitizer.cmake`

- `arm64-linux-alchemy-clang-release.cmake`

- `arm64-linux-alchemy-clang.cmake`

- `arm64-linux-alchemy-release.cmake`

- `arm64-linux-alchemy.cmake`

- `arm64-osx-alchemy-release.cmake`

- `arm64-osx-alchemy.cmake`

- `arm64-windows-alchemy-release.cmake`

- `arm64-windows-alchemy.cmake`

- `x64-linux-alchemy-avx2-release.cmake`

- `x64-linux-alchemy-avx2.cmake`

- `x64-linux-alchemy-avx512-release.cmake`

- `x64-linux-alchemy-avx512.cmake`

- `x64-linux-alchemy-clang-avx2-asan.cmake`

- `x64-linux-alchemy-clang-avx2-release.cmake`

- `x64-linux-alchemy-clang-avx2-tsan.cmake`

- `x64-linux-alchemy-clang-avx2.cmake`

- `x64-linux-alchemy-clang-avx512-release.cmake`

- `x64-linux-alchemy-clang-avx512.cmake`

- `x64-linux-alchemy-clang-release.cmake`

- `x64-linux-alchemy-clang.cmake`

- `x64-linux-alchemy-release.cmake`

- `x64-linux-alchemy.cmake`

- `x64-osx-alchemy-release.cmake`

- `x64-osx-alchemy.cmake`

- `x64-windows-alchemy-avx2-release.cmake`

- `x64-windows-alchemy-avx2.cmake`

- `x64-windows-alchemy-avx512-release.cmake`

- `x64-windows-alchemy-avx512.cmake`

- `x64-windows-alchemy-release.cmake`

- `x64-windows-alchemy.cmake`


## indra/doxygen/ (2 files)

- `CMakeLists.txt`

- `Doxyfile.in`


## indra/externals/ (1 files)

- `README.md`


## indra/externals/ca-certificates/ (3 files)

- `ca-bundle.crt`

- `mk-ca-bundle.pl`

- `update-certs.sh`


## indra/externals/js/ (7 files)

- `CUBEMAPTOEQUIRECTANGULAR_LICENSE.txt`

- `CubemapToEquirectangular.js`

- `JPEG_ENCODER_BASIC_LICENSE.txt`

- `OrbitControls.js`

- `THREEJS_LICENSE.txt`

- `jpeg_encoder_basic.js`

- `three.min.js`


## indra/integration_tests/ (1 files)

- `CMakeLists.txt`


## indra/integration_tests/llimage_libtest/ (3 files)

- `CMakeLists.txt`

- `llimage_libtest.cpp`

- `llimage_libtest.h`


## indra/integration_tests/llimage_libtest/filters/ (41 files)

- `1970colorize.xml`

- `autocontrast.xml`

- `badtrip.xml`

- `blowhighlights.xml`

- `blur.xml`

- `brighten.xml`

- `colorize.xml`

- `colortransform.xml`

- `contrast.xml`

- `convolve.xml`

- `darken.xml`

- `dodgeandburn.xml`

- `edges.xml`

- `focus.xml`

- `gamma.xml`

- `grayscale.xml`

- `heatwave.xml`

- `horizontalscreen.xml`

- `julesverne.xml`

- `lensflare.xml`

- `lightleak.xml`

- `linearize.xml`

- `miniature.xml`

- `newsscreen.xml`

- `overcast.xml`

- `pixelate.xml`

- `posterize.xml`

- `rotatecolors180.xml`

- `saturate.xml`

- `sepia.xml`

- `sharpen.xml`

- `slantedscreen.xml`

- `spotlight.xml`

- `stencilgradient.xml`

- `stencilscanlines.xml`

- `stenciluniform.xml`

- `stencilvignette.xml`

- `thematrix.xml`

- `toycamera.xml`

- `verticalscreen.xml`

- `video.xml`


## indra/llappearance/ (35 files)

- `CMakeLists.txt`

- `llavatarappearance.cpp`

- `llavatarappearance.h`

- `llavatarappearancedefines.cpp`

- `llavatarappearancedefines.h`

- `llavatarjoint.cpp`

- `llavatarjoint.h`

- `llavatarjointmesh.cpp`

- `llavatarjointmesh.h`

- `lldriverparam.cpp`

- `lldriverparam.h`

- `lljointdata.h`

- `lljointpickname.h`

- `lllocaltextureobject.cpp`

- `lllocaltextureobject.h`

- `llpolymesh.cpp`

- `llpolymesh.h`

- `llpolymorph.cpp`

- `llpolymorph.h`

- `llpolyskeletaldistortion.cpp`

- `llpolyskeletaldistortion.h`

- `lltexglobalcolor.cpp`

- `lltexglobalcolor.h`

- `lltexlayer.cpp`

- `lltexlayer.h`

- `lltexlayerparams.cpp`

- `lltexlayerparams.h`

- `llviewervisualparam.cpp`

- `llviewervisualparam.h`

- `llwearable.cpp`

- `llwearable.h`

- `llwearabledata.cpp`

- `llwearabledata.h`

- `llwearabletype.cpp`

- `llwearabletype.h`


## indra/llappearance/tests/ (5 files)

- `llappearance_test_fakes.cpp`

- `llavatarappearancedefines_bench.cpp`

- `llavatarappearancedefines_test.cpp`

- `lltexlayer_gl_test.cpp`

- `llwearabletype_test.cpp`


## indra/llappearanceutility/ (31 files)

- `CMakeLists.txt`

- `README.md`

- `appearance_utility.cpp`

- `llappappearanceutility.cpp`

- `llappappearanceutility.h`

- `llbakingavatar.cpp`

- `llbakingavatar.h`

- `llbakingjoint.cpp`

- `llbakingjoint.h`

- `llbakingjointmesh.cpp`

- `llbakingjointmesh.h`

- `llbakingprocess.cpp`

- `llbakingprocess.h`

- `llbakingshadermgr.cpp`

- `llbakingshadermgr.h`

- `llbakingtexlayer.cpp`

- `llbakingtexlayer.h`

- `llbakingtexture.cpp`

- `llbakingtexture.h`

- `llbakingwearable.cpp`

- `llbakingwearable.h`

- `llbakingwearablesdata.cpp`

- `llbakingwearablesdata.h`

- `llbakingwindow.cpp`

- `llbakingwindow.h`

- `llprocessparams.cpp`

- `llprocessparams.h`

- `llprocessskin.cpp`

- `llprocessskin.h`

- `llprocesstexture.cpp`

- `llprocesstexture.h`


## indra/llappearanceutility/tests/ (6 files)

- `joint-offsets.xml`

- `joint-offsets.xml.output`

- `params.xml`

- `params.xml.output`

- `texture.llsd.binary`

- `texture.llsd.output`


## indra/llaudio/ (28 files)

- `CMakeLists.txt`

- `llaudiodecodemgr.cpp`

- `llaudiodecodemgr.h`

- `llaudioengine.cpp`

- `llaudioengine.h`

- `llaudioengine_faudio.cpp`

- `llaudioengine_faudio.h`

- `llaudioengine_fmodstudio.cpp`

- `llaudioengine_fmodstudio.h`

- `llaudioengine_openal.cpp`

- `llaudioengine_openal.h`

- `lllistener.cpp`

- `lllistener.h`

- `lllistener_ds3d.h`

- `lllistener_faudio.cpp`

- `lllistener_faudio.h`

- `lllistener_fmodstudio.cpp`

- `lllistener_fmodstudio.h`

- `lllistener_openal.cpp`

- `lllistener_openal.h`

- `llstreamingaudio.h`

- `llstreamingaudio_fmodstudio.cpp`

- `llstreamingaudio_fmodstudio.h`

- `llvorbisencode.cpp`

- `llvorbisencode.h`

- `llwavfile.cpp`

- `llwavfile.h`

- `llwindgen.h`


## indra/llcharacter/ (41 files)

- `CMakeLists.txt`

- `llanimationstates.cpp`

- `llanimationstates.h`

- `llbvhconsts.h`

- `llbvhloader.cpp`

- `llbvhloader.h`

- `llcharacter.cpp`

- `llcharacter.h`

- `lleditingmotion.cpp`

- `lleditingmotion.h`

- `llgesture.cpp`

- `llgesture.h`

- `llhandmotion.cpp`

- `llhandmotion.h`

- `llheadrotmotion.cpp`

- `llheadrotmotion.h`

- `lljoint.cpp`

- `lljoint.h`

- `lljointsolverrp3.cpp`

- `lljointsolverrp3.h`

- `lljointstate.h`

- `llkeyframefallmotion.cpp`

- `llkeyframefallmotion.h`

- `llkeyframemotion.cpp`

- `llkeyframemotion.h`

- `llkeyframestandmotion.cpp`

- `llkeyframestandmotion.h`

- `llkeyframewalkmotion.cpp`

- `llkeyframewalkmotion.h`

- `llmotion.cpp`

- `llmotion.h`

- `llmotioncontroller.cpp`

- `llmotioncontroller.h`

- `llmultigesture.cpp`

- `llmultigesture.h`

- `llpose.cpp`

- `llpose.h`

- `lltargetingmotion.cpp`

- `lltargetingmotion.h`

- `llvisualparam.cpp`

- `llvisualparam.h`


## indra/llcharacter/tests/ (10 files)

- `altestcharacter.h`

- `altestmotion.h`

- `llbvhloader_test.cpp`

- `llcharacter_test.cpp`

- `llcharacter_test_checks.cpp`

- `lljoint_test.cpp`

- `llkeyframemotion_test.cpp`

- `llmotioncontroller_test.cpp`

- `llmultigesture_test.cpp`

- `llpose_test.cpp`


## indra/llcommon/ (265 files)

- `CMakeLists.txt`

- `alcompact.h`

- `alenumtable.h`

- `alfilewrite.cpp`

- `alfilewrite.h`

- `allinebreaks.h`

- `almainloop.cpp`

- `almainloop.h`

- `alparamtype.cpp`

- `alparamtype.h`

- `alprecisewaiter.cpp`

- `alprecisewaiter.h`

- `alrandmap.h`

- `alrecoverystore.cpp`

- `alrecoverystore.h`

- `alregex.cpp`

- `alregex.h`

- `alsanitizer.cpp`

- `alsanitizer.h`

- `alsavehistory.cpp`

- `alsavehistory.h`

- `alscratcharena.cpp`

- `alscratcharena.h`

- `alserialworker.cpp`

- `alserialworker.h`

- `alsharedmutex.h`

- `alsimd.h`

- `altimerresolutionscope.cpp`

- `altimerresolutionscope.h`

- `alunitconversion.h`

- `alwatchedfile.cpp`

- `alwatchedfile.h`

- `always_return.h`

- `apply.cpp`

- `apply.h`

- `chrono.h`

- `classic_callback.cpp`

- `classic_callback.h`

- `commoncontrol.cpp`

- `commoncontrol.h`

- `fsyspath.h`

- `function_types.h`

- `hbxxh.cpp`

- `hbxxh.h`

- `hexdump.h`

- `indra_constants.cpp`

- `indra_constants.h`

- `is_approx_equal_fraction.h`

- `lazyeventapi.cpp`

- `lazyeventapi.h`

- `linden_common.h`

- `llalignedarray.h`

- `llapp.cpp`

- `llapp.h`

- `llapr.cpp`

- `llapr.h`

- `llassettype.cpp`

- `llassettype.h`

- `llatomic.cpp`

- `llatomic.h`

- `llbase64.cpp`

- `llbase64.h`

- `llbitpack.cpp`

- `llbitpack.h`

- `llboost.h`

- `llcallbacklist.cpp`

- `llcallbacklist.h`

- `llcleanup.cpp`

- `llcleanup.h`

- `llclickaction.h`

- `llcommon.cpp`

- `llcommon.h`

- `llcommonutils.cpp`

- `llcommonutils.h`

- `llcond.h`

- `llcoros.cpp`

- `llcoros.h`

- `llcrc.cpp`

- `llcrc.h`

- `llcriticaldamp.cpp`

- `llcriticaldamp.h`

- `lldate.cpp`

- `lldate.h`

- `lldeadmantimer.cpp`

- `lldeadmantimer.h`

- `lldefs.h`

- `lldependencies.cpp`

- `lldependencies.h`

- `lldepthstack.h`

- `lldoubledispatch.h`

- `llendianswizzle.h`

- `llerror.cpp`

- `llerror.h`

- `llerrorcontrol.h`

- `llerrorlegacy.h`

- `llevent.cpp`

- `llevent.h`

- `lleventapi.cpp`

- `lleventapi.h`

- `lleventcoro.cpp`

- `lleventcoro.h`

- `lleventdispatcher.cpp`

- `lleventdispatcher.h`

- `lleventemitter.h`

- `lleventfilter.cpp`

- `lleventfilter.h`

- `llevents.cpp`

- `llevents.h`

- `lleventtimer.cpp`

- `lleventtimer.h`

- `llexception.cpp`

- `llexception.h`

- `llfile.cpp`

- `llfile.h`

- `llfindlocale.cpp`

- `llfindlocale.h`

- `llfixedbuffer.cpp`

- `llfixedbuffer.h`

- `llformat.cpp`

- `llformat.h`

- `llframetimer.cpp`

- `llframetimer.h`

- `llhandle.h`

- `llhash.h`

- `llheartbeat.cpp`

- `llheartbeat.h`

- `llheteromap.cpp`

- `llheteromap.h`

- `llindexedvector.h`

- `llinitdestroyclass.cpp`

- `llinitdestroyclass.h`

- `llinitparam.cpp`

- `llinitparam.h`

- `llinstancetracker.cpp`

- `llinstancetracker.h`

- `llinstancetrackersubclass.h`

- `llkeybind.cpp`

- `llkeybind.h`

- `llkeythrottle.h`

- `llkeyusetracker.h`

- `llleap.cpp`

- `llleap.h`

- `llleaplistener.cpp`

- `llleaplistener.h`

- `llliveappconfig.cpp`

- `llliveappconfig.h`

- `lllivefile.cpp`

- `lllivefile.h`

- `llmainthreadtask.cpp`

- `llmainthreadtask.h`

- `llmake.h`

- `llmd5.cpp`

- `llmd5.h`

- `llmemory.cpp`

- `llmemory.h`

- `llmemorystream.cpp`

- `llmemorystream.h`

- `llmetrics.cpp`

- `llmetrics.h`

- `llmortician.cpp`

- `llmortician.h`

- `llmutex.cpp`

- `llmutex.h`

- `llnametable.h`

- `llpointer.cpp`

- `llpointer.h`

- `llpounceable.h`

- `llpredicate.cpp`

- `llpredicate.h`

- `llpreprocessor.h`

- `llpriqueuemap.h`

- `llprocess.cpp`

- `llprocess.h`

- `llprocessor.cpp`

- `llprocessor.h`

- `llprocinfo.cpp`

- `llprocinfo.h`

- `llprofiler.h`

- `llprofilercategories.h`

- `llptrto.h`

- `llqueuedthread.cpp`

- `llqueuedthread.h`

- `llrand.cpp`

- `llrand.h`

- `llrefcount.cpp`

- `llrefcount.h`

- `llregistry.h`

- `llrun.cpp`

- `llrun.h`

- `llsafehandle.h`

- `llsd.cpp`

- `llsd.h`

- `llsdjson.cpp`

- `llsdjson.h`

- `llsdparam.cpp`

- `llsdparam.h`

- `llsdserialize.cpp`

- `llsdserialize.h`

- `llsdserialize_xml.cpp`

- `llsdserialize_xml.h`

- `llsdutil.cpp`

- `llsdutil.h`

- `llsimplehash.h`

- `llsingleton.cpp`

- `llsingleton.h`

- `llsmoothstep.h`

- `llstatenums.h`

- `llstaticstringtable.h`

- `llstatsaccumulator.h`

- `llstl.h`

- `llstreamtools.cpp`

- `llstreamtools.h`

- `llstrider.h`

- `llstring.cpp`

- `llstring.h`

- `llstringtable.cpp`

- `llstringtable.h`

- `llsys.cpp`

- `llsys.h`

- `llsys_objc.h`

- `llsys_objc.mm`

- `lltempredirect.cpp`

- `lltempredirect.h`

- `llthread.cpp`

- `llthread.h`

- `llthreadlocalstorage.h`

- `llthreadsafequeue.cpp`

- `llthreadsafequeue.h`

- `lltimer.cpp`

- `lltimer.h`

- `lltrace.cpp`

- `lltrace.h`

- `lltraceaccumulators.cpp`

- `lltraceaccumulators.h`

- `lltracerecording.cpp`

- `lltracerecording.h`

- `lltracethreadrecorder.cpp`

- `lltracethreadrecorder.h`

- `lltreeiterators.h`

- `llunits.h`

- `llunittype.h`

- `lluri.cpp`

- `lluri.h`

- `lluriparser.cpp`

- `lluriparser.h`

- `lluuid.cpp`

- `lluuid.h`

- `llwatchdog.cpp`

- `llwatchdog.h`

- `llwin32headers.h`

- `llworkerthread.cpp`

- `llworkerthread.h`

- `lockstatic.h`

- `stdtypes.h`

- `string_table.h`

- `stringize.h`

- `threadpool.cpp`

- `threadpool.h`

- `threadpool_fwd.h`

- `threadsafeschedule.h`

- `tuple.h`

- `u64.cpp`

- `u64.h`

- `workqueue.cpp`

- `workqueue.h`


## indra/llcommon/tests/ (78 files)

- `StringVec.h`

- `alcompact_test.cpp`

- `alenumtable_test.cpp`

- `alfilewrite_test.cpp`

- `alprecisewaiter_test.cpp`

- `alrecoverystore_test.cpp`

- `alregex_bench.cpp`

- `alregex_test.cpp`

- `alsavehistory_test.cpp`

- `alscratcharena_test.cpp`

- `alserialworker_test.cpp`

- `alsharedmutex_test.cpp`

- `alsimd_asm_probe.cpp`

- `alsimd_test.cpp`

- `altimerresolutionscope_test.cpp`

- `alunitconversion_test.cpp`

- `alwatchedfile_test.cpp`

- `apply_test.cpp`

- `bitpack_test.cpp`

- `classic_callback_test.cpp`

- `commonmisc_test.cpp`

- `lazyeventapi_test.cpp`

- `listener.h`

- `llapp_test.cpp`

- `llassettype_test.cpp`

- `llbase64_test.cpp`

- `llcallbacklist_test.cpp`

- `llcommon_test_checks.cpp`

- `llcond_test.cpp`

- `lldate_test.cpp`

- `lldeadmantimer_test.cpp`

- `lldependencies_test.cpp`

- `lldoubledispatch_test.cpp`

- `llerror_test.cpp`

- `lleventcoro_test.cpp`

- `lleventdispatcher_test.cpp`

- `lleventfilter_test.cpp`

- `llevents_test.cpp`

- `llfile_test.cpp`

- `llframetimer_test.cpp`

- `llheteromap_test.cpp`

- `llhttpdate_test.cpp`

- `llinitparam_test.cpp`

- `llinstancetracker_test.cpp`

- `llleap_test.cpp`

- `llmainthreadtask_test.cpp`

- `llmutex_bench.cpp`

- `llmutex_test.cpp`

- `llpounceable_test.cpp`

- `llprocess_test.cpp`

- `llprocessor_test.cpp`

- `llprocinfo_test.cpp`

- `llptrto_test.cpp`

- `llqueuedthread_test.cpp`

- `llrand_test.cpp`

- `llsd_test.cpp`

- `llsdjson_test.cpp`

- `llsdserialize_python_test.cpp`

- `llsdserialize_test.cpp`

- `llsdutil_test.cpp`

- `llsingleton_test.cpp`

- `llstreamtools_test.cpp`

- `llstring_test.cpp`

- `llstring_utf_test.cpp`

- `llthread_test.cpp`

- `lltimer_test.cpp`

- `lltrace_test.cpp`

- `lltreeiterators_test.cpp`

- `llunits_test.cpp`

- `lluri_test.cpp`

- `lluuid_test.cpp`

- `oversleep_bench.cpp`

- `stringize_test.cpp`

- `threadpool_test.cpp`

- `threadsafeschedule_test.cpp`

- `tuple_test.cpp`

- `workqueue_test.cpp`

- `wrapllerrs.h`


## indra/llcorehttp/ (58 files)

- `CMakeLists.txt`

- `README.Linden`

- `_httpinternal.h`

- `_httplibcurl.cpp`

- `_httplibcurl.h`

- `_httpopcancel.cpp`

- `_httpopcancel.h`

- `_httpoperation.cpp`

- `_httpoperation.h`

- `_httpoprequest.cpp`

- `_httpoprequest.h`

- `_httpopsetget.cpp`

- `_httpopsetget.h`

- `_httpopsetpriority.cpp`

- `_httpopsetpriority.h`

- `_httppolicy.cpp`

- `_httppolicy.h`

- `_httppolicyclass.cpp`

- `_httppolicyclass.h`

- `_httppolicyglobal.cpp`

- `_httppolicyglobal.h`

- `_httpreadyqueue.h`

- `_httpreplyqueue.cpp`

- `_httpreplyqueue.h`

- `_httprequestqueue.cpp`

- `_httprequestqueue.h`

- `_httpretryqueue.h`

- `_httpservice.cpp`

- `_httpservice.h`

- `_mutex.h`

- `_refcounted.cpp`

- `_refcounted.h`

- `_thread.h`

- `alhttpwake.cpp`

- `alhttpwake.h`

- `bufferarray.cpp`

- `bufferarray.h`

- `bufferstream.cpp`

- `bufferstream.h`

- `httpcommon.cpp`

- `httpcommon.h`

- `httphandler.h`

- `httpheaders.cpp`

- `httpheaders.h`

- `httpoptions.cpp`

- `httpoptions.h`

- `httprequest.cpp`

- `httprequest.h`

- `httpresponse.cpp`

- `httpresponse.h`

- `httpstats.cpp`

- `httpstats.h`

- `llhttpconstants.cpp`

- `llhttpconstants.h`

- `lljsonrpcws.cpp`

- `lljsonrpcws.h`

- `llwebsocketmgr.cpp`

- `llwebsocketmgr.h`


## indra/llcorehttp/examples/ (1 files)

- `http_texture_load.cpp`


## indra/llcorehttp/tests/ (14 files)

- `alhttpwake_test.cpp`

- `bufferarray_test.cpp`

- `bufferstream_test.cpp`

- `httpheaders_test.cpp`

- `httpoperation_test.cpp`

- `httprequest_test.cpp`

- `httprequestqueue_test.cpp`

- `httpretryqueue_test.cpp`

- `httpstatus_test.cpp`

- `jsonrpcws_test.cpp`

- `llcorehttp_test_checks.cpp`

- `refcounted_test.cpp`

- `test_llcorehttp_peer.py`

- `websocketmgr_test.cpp`


## indra/llfilesystem/ (18 files)

- `CMakeLists.txt`

- `lldir.cpp`

- `lldir.h`

- `lldir_linux.cpp`

- `lldir_linux.h`

- `lldir_mac.h`

- `lldir_mac.mm`

- `lldir_win32.cpp`

- `lldir_win32.h`

- `lldirguard.h`

- `lldiriterator.cpp`

- `lldiriterator.h`

- `lldiskcache.cpp`

- `lldiskcache.h`

- `llfilesystem.cpp`

- `llfilesystem.h`

- `lllfsthread.cpp`

- `lllfsthread.h`


## indra/llfilesystem/tests/ (2 files)

- `lldir_test.cpp`

- `lldiriterator_test.cpp`


## indra/llimage/ (30 files)

- `CMakeLists.txt`

- `alj2clayout.cpp`

- `alj2clayout.h`

- `llimage.cpp`

- `llimage.h`

- `llimageavif.cpp`

- `llimageavif.h`

- `llimagebmp.cpp`

- `llimagebmp.h`

- `llimagedimensionsinfo.cpp`

- `llimagedimensionsinfo.h`

- `llimagedxt.cpp`

- `llimagedxt.h`

- `llimagefilter.cpp`

- `llimagefilter.h`

- `llimagej2c.cpp`

- `llimagej2c.h`

- `llimagejpeg.cpp`

- `llimagejpeg.h`

- `llimagepng.cpp`

- `llimagepng.h`

- `llimagetga.cpp`

- `llimagetga.h`

- `llimagewebp.cpp`

- `llimagewebp.h`

- `llimageworker.cpp`

- `llimageworker.h`

- `llmapimagetype.h`

- `llpngwrapper.cpp`

- `llpngwrapper.h`


## indra/llimage/tests/ (4 files)

- `alj2clayout_test.cpp`

- `llimage_test.cpp`

- `llimagej2c_test.cpp`

- `llimageworker_test.cpp`


## indra/llimagej2coj/ (3 files)

- `CMakeLists.txt`

- `llimagej2coj.cpp`

- `llimagej2coj.h`


## indra/llimagej2crs/ (3 files)

- `CMakeLists.txt`

- `alimagej2crs.cpp`

- `alimagej2crs.h`


## indra/llimagej2crs/tests/ (1 files)

- `alimagej2crs_test.cpp`


## indra/llinventory/ (41 files)

- `CMakeLists.txt`

- `alparcelupdate.cpp`

- `alparcelupdate.h`

- `llcategory.cpp`

- `llcategory.h`

- `llfoldertype.cpp`

- `llfoldertype.h`

- `llinventory.cpp`

- `llinventory.h`

- `llinventorydefines.cpp`

- `llinventorydefines.h`

- `llinventorysettings.cpp`

- `llinventorysettings.h`

- `llinventorytype.cpp`

- `llinventorytype.h`

- `llinvtranslationbrdg.h`

- `lllandmark.cpp`

- `lllandmark.h`

- `llnotecard.cpp`

- `llnotecard.h`

- `llparcel.cpp`

- `llparcel.h`

- `llparcelflags.h`

- `llpermissions.cpp`

- `llpermissions.h`

- `llpermissionsflags.h`

- `llsaleinfo.cpp`

- `llsaleinfo.h`

- `llsettingsbase.cpp`

- `llsettingsbase.h`

- `llsettingsdaycycle.cpp`

- `llsettingsdaycycle.h`

- `llsettingssky.cpp`

- `llsettingssky.h`

- `llsettingswater.cpp`

- `llsettingswater.h`

- `lltransactionflags.cpp`

- `lltransactionflags.h`

- `lltransactiontypes.h`

- `lluserrelations.cpp`

- `lluserrelations.h`


## indra/llinventory/tests/ (9 files)

- `alparcelupdate_test.cpp`

- `inventorymisc_test.cpp`

- `llnotecard_test.cpp`

- `llparcel_test.cpp`

- `llpermissions_test.cpp`

- `llsaleinfo_test.cpp`

- `llsettingssky_test.cpp`

- `lluserrelations_test.cpp`

- `typenames_bench.cpp`


## indra/llmath/ (88 files)

- `CMakeLists.txt`

- `almeshfacepack.cpp`

- `almeshfacepack.h`

- `almeshsimplifier.cpp`

- `almeshsimplifier.h`

- `alplaneset.cpp`

- `alplaneset.h`

- `alprojection.cpp`

- `alprojection.h`

- `alsimdkernels.cpp`

- `alsimdkernels.h`

- `alsimdkernels.inl`

- `alsimdplanar.cpp`

- `llbbox.cpp`

- `llbbox.h`

- `llbboxlocal.cpp`

- `llbboxlocal.h`

- `llcalc.cpp`

- `llcalc.h`

- `llcalcparser.cpp`

- `llcalcparser.h`

- `llcamera.cpp`

- `llcamera.h`

- `llcoord.h`

- `llcoordframe.cpp`

- `llcoordframe.h`

- `llinterp.h`

- `llline.cpp`

- `llline.h`

- `llmath.h`

- `llmatrix3a.cpp`

- `llmatrix3a.h`

- `llmatrix3a.inl`

- `llmatrix4a.cpp`

- `llmatrix4a.h`

- `llmodularmath.cpp`

- `llmodularmath.h`

- `lloctree.cpp`

- `lloctree.h`

- `llplane.h`

- `llquantize.h`

- `llquaternion.cpp`

- `llquaternion.h`

- `llquaternion2.h`

- `llquaternion2.inl`

- `llrect.cpp`

- `llrect.h`

- `llrigginginfo.cpp`

- `llrigginginfo.h`

- `llsdutil_math.cpp`

- `llsdutil_math.h`

- `llsimdmath.h`

- `llsimdtypes.h`

- `llsimdtypes.inl`

- `lltreenode.h`

- `llvector4a.cpp`

- `llvector4a.h`

- `llvector4a.inl`

- `llvector4logical.h`

- `llvolume.cpp`

- `llvolume.h`

- `llvolumemgr.cpp`

- `llvolumemgr.h`

- `llvolumeoctree.cpp`

- `llvolumeoctree.h`

- `m3math.cpp`

- `m3math.h`

- `m4math.cpp`

- `m4math.h`

- `raytrace.cpp`

- `raytrace.h`

- `v2math.cpp`

- `v2math.h`

- `v3color.cpp`

- `v3color.h`

- `v3colorutil.h`

- `v3dmath.cpp`

- `v3dmath.h`

- `v3math.cpp`

- `v3math.h`

- `v4color.cpp`

- `v4color.h`

- `v4coloru.cpp`

- `v4coloru.h`

- `v4math.cpp`

- `v4math.h`

- `xform.cpp`

- `xform.h`


## indra/llmath/tests/ (32 files)

- `alignment_test.cpp`

- `almeshcorpus.h`

- `almeshfacepack_test.cpp`

- `almeshrepack_bench.cpp`

- `almeshsimplifier_test.cpp`

- `almeshzip_bench.cpp`

- `alplaneset_test.cpp`

- `alsimdkernels_test.cpp`

- `llbbox_test.cpp`

- `llbboxlocal_test.cpp`

- `llmatrix3a_test.cpp`

- `llmatrix4a_test.cpp`

- `llmodularmath_test.cpp`

- `lloctree_test.cpp`

- `llquaternion2_test.cpp`

- `llquaternion_test.cpp`

- `llrect_test.cpp`

- `llsdutil_math_test.cpp`

- `llsimd_bench.cpp`

- `llvector4a_test.cpp`

- `llvolume_bench.cpp`

- `llvolume_test.cpp`

- `m3math_test.cpp`

- `mathmisc_test.cpp`

- `v2math_test.cpp`

- `v3color_test.cpp`

- `v3dmath_test.cpp`

- `v3math_test.cpp`

- `v4color_test.cpp`

- `v4coloru_test.cpp`

- `v4math_test.cpp`

- `xform_test.cpp`


## indra/llmessage/ (155 files)

- `CMakeLists.txt`

- `alnetimpairment.cpp`

- `alnetimpairment.h`

- `alsessioncapture.cpp`

- `alsessioncapture.h`

- `llassetstorage.cpp`

- `llassetstorage.h`

- `llavatarname.cpp`

- `llavatarname.h`

- `llavatarnamecache.cpp`

- `llavatarnamecache.h`

- `llbuffer.cpp`

- `llbuffer.h`

- `llbufferstream.cpp`

- `llbufferstream.h`

- `llcachename.cpp`

- `llcachename.h`

- `llchainio.cpp`

- `llchainio.h`

- `llcipher.h`

- `llcircuit.cpp`

- `llcircuit.h`

- `llclassifiedflags.cpp`

- `llclassifiedflags.h`

- `llcoproceduremanager.cpp`

- `llcoproceduremanager.h`

- `llcorehttputil.cpp`

- `llcorehttputil.h`

- `lldatapacker.cpp`

- `lldatapacker.h`

- `lldbstrings.h`

- `lldispatcher.cpp`

- `lldispatcher.h`

- `lleventflags.h`

- `llexperiencecache.cpp`

- `llexperiencecache.h`

- `llextendedstatus.h`

- `llfollowcamparams.h`

- `llgenericstreamingmessage.cpp`

- `llgenericstreamingmessage.h`

- `llhost.cpp`

- `llhost.h`

- `llhttpnode.cpp`

- `llhttpnode.h`

- `llhttpnodeadapter.h`

- `llhttpsdhandler.cpp`

- `llhttpsdhandler.h`

- `llinstantmessage.cpp`

- `llinstantmessage.h`

- `llinvite.h`

- `lliobuffer.cpp`

- `lliobuffer.h`

- `lliopipe.cpp`

- `lliopipe.h`

- `lliosocket.cpp`

- `lliosocket.h`

- `llioutil.cpp`

- `llioutil.h`

- `llloginflags.h`

- `llmessagebuilder.cpp`

- `llmessagebuilder.h`

- `llmessageconfig.cpp`

- `llmessageconfig.h`

- `llmessagelog.cpp`

- `llmessagelog.h`

- `llmessagereader.cpp`

- `llmessagereader.h`

- `llmessagesenderinterface.h`

- `llmessagetemplate.cpp`

- `llmessagetemplate.h`

- `llmessagetemplateparser.cpp`

- `llmessagetemplateparser.h`

- `llmessagethrottle.cpp`

- `llmessagethrottle.h`

- `llmsgvariabletype.h`

- `llnamevalue.cpp`

- `llnamevalue.h`

- `llpacketack.cpp`

- `llpacketack.h`

- `llpacketbuffer.cpp`

- `llpacketbuffer.h`

- `llpacketring.cpp`

- `llpacketring.h`

- `llpartdata.cpp`

- `llpartdata.h`

- `llproxy.cpp`

- `llproxy.h`

- `llpumpio.cpp`

- `llpumpio.h`

- `llqueryflags.h`

- `llregionflags.h`

- `llregionhandle.h`

- `llsdappservices.cpp`

- `llsdappservices.h`

- `llsdhttpserver.cpp`

- `llsdhttpserver.h`

- `llsdmessagebuilder.cpp`

- `llsdmessagebuilder.h`

- `llsdmessagereader.cpp`

- `llsdmessagereader.h`

- `llstoredmessage.cpp`

- `llstoredmessage.h`

- `lltaskname.h`

- `llteleportflags.h`

- `lltemplatemessagebuilder.cpp`

- `lltemplatemessagebuilder.h`

- `lltemplatemessagedispatcher.cpp`

- `lltemplatemessagedispatcher.h`

- `lltemplatemessagereader.cpp`

- `lltemplatemessagereader.h`

- `llthrottle.cpp`

- `llthrottle.h`

- `lltransfermanager.cpp`

- `lltransfermanager.h`

- `lltransfersourceasset.cpp`

- `lltransfersourceasset.h`

- `lltransfersourcefile.cpp`

- `lltransfersourcefile.h`

- `lltransfertargetfile.cpp`

- `lltransfertargetfile.h`

- `lltransfertargetvfile.cpp`

- `lltransfertargetvfile.h`

- `lltrustedmessageservice.cpp`

- `lltrustedmessageservice.h`

- `llvehicleparams.h`

- `llxfer.cpp`

- `llxfer.h`

- `llxfer_file.cpp`

- `llxfer_file.h`

- `llxfer_mem.cpp`

- `llxfer_mem.h`

- `llxfer_vfile.cpp`

- `llxfer_vfile.h`

- `llxfermanager.cpp`

- `llxfermanager.h`

- `llxorcipher.cpp`

- `llxorcipher.h`

- `llzerocode.h`

- `machine.cpp`

- `machine.h`

- `mean_collision_data.h`

- `message.cpp`

- `message.h`

- `message_prehash.cpp`

- `message_prehash.h`

- `message_string_table.cpp`

- `net.cpp`

- `net.h`

- `patch_code.cpp`

- `patch_code.h`

- `patch_dct.cpp`

- `patch_dct.h`

- `patch_idct.cpp`

- `sound_ids.cpp`

- `sound_ids.h`


## indra/llmessage/tests/ (34 files)

- `almessagesystem_stub.cpp`

- `alnetimpairment_test.cpp`

- `alsessioncapture_test.cpp`

- `io_test.cpp`

- `layerpatch_test.cpp`

- `llavatarnamecache_test.cpp`

- `llbuffer_test.cpp`

- `llcircuit_test.cpp`

- `llcoproceduremanager_test.cpp`

- `llcorehttputil_test.cpp`

- `lldatapacker_test.cpp`

- `llhost_test.cpp`

- `llhttpnode_stub.cpp`

- `llhttpnode_test.cpp`

- `llmessage_test_checks.cpp`

- `llmessageconfig_test.cpp`

- `llmessagesystem_fixture.h`

- `llmessagetemplateparser_test.cpp`

- `llnamevalue_test.cpp`

- `llpartdata_test.cpp`

- `llpipeutil.cpp`

- `llpipeutil.h`

- `llsdmessagebuilder_test.cpp`

- `llsdmessagereader_test.cpp`

- `lltemplatemessagebuilder_test.cpp`

- `lltemplatemessagedispatcher_test.cpp`

- `lltrustedmessageservice_test.cpp`

- `llxfer_file_test.cpp`

- `llxfermanager_test.cpp`

- `llxorcipher_test.cpp`

- `llzerocode_test.cpp`

- `message_test.cpp`

- `patch_code_test.cpp`

- `testrunner.py`


## indra/llphysicsextensionsos/ (13 files)

- `CMakeLists.txt`

- `LLPathingLibStubImpl.cpp`

- `LLPathingLibStubImpl.h`

- `LLPhysicsExtensionsStubImpl.cpp`

- `LLPhysicsExtensionsStubImpl.h`

- `llconvexdecomposition.cpp`

- `llconvexdecomposition.h`

- `llconvexdecompositionvhacd.cpp`

- `llconvexdecompositionvhacd.h`

- `llpathinglib.cpp`

- `llpathinglib.h`

- `llphysicsextensions.cpp`

- `llphysicsextensions.h`


## indra/llplugin/ (17 files)

- `CMakeLists.txt`

- `llpluginclassmedia.cpp`

- `llpluginclassmedia.h`

- `llpluginclassmediaowner.h`

- `llplugininstance.cpp`

- `llplugininstance.h`

- `llpluginmessage.cpp`

- `llpluginmessage.h`

- `llpluginmessageclasses.h`

- `llpluginmessagepipe.cpp`

- `llpluginmessagepipe.h`

- `llpluginprocesschild.cpp`

- `llpluginprocesschild.h`

- `llpluginprocessparent.cpp`

- `llpluginprocessparent.h`

- `llpluginsharedmemory.cpp`

- `llpluginsharedmemory.h`


## indra/llplugin/slplugin/ (7 files)

- `slplugin-objc.h`

- `slplugin-objc.mm`

- `slplugin.cpp`

- `slplugin.manifest`

- `slplugin_daemon.cpp`

- `slplugin_info.plist`

- `slplugin_static.cpp`


## indra/llprecompiled/ (2 files)

- `CMakeLists.txt`

- `cmake_dummy.cpp`


## indra/llprimitive/ (43 files)

- `CMakeLists.txt`

- `alcompressedupdate.cpp`

- `alcompressedupdate.h`

- `alobjectmotion.cpp`

- `alobjectmotion.h`

- `alobjectorphans.h`

- `alobjectupdate.cpp`

- `alobjectupdate.h`

- `legacy_object_types.h`

- `lldaeloader.cpp`

- `lldaeloader.h`

- `llgltfmaterial.cpp`

- `llgltfmaterial.h`

- `llgltfmaterial_templates.h`

- `lllslconstants.h`

- `llmaterial.cpp`

- `llmaterial.h`

- `llmaterialid.cpp`

- `llmaterialid.h`

- `llmaterialtable.cpp`

- `llmaterialtable.h`

- `llmediaentry.cpp`

- `llmediaentry.h`

- `llmodel.cpp`

- `llmodel.h`

- `llmodelloader.cpp`

- `llmodelloader.h`

- `llprimitive.cpp`

- `llprimitive.h`

- `llprimtexturelist.cpp`

- `llprimtexturelist.h`

- `lltextureanim.cpp`

- `lltextureanim.h`

- `lltextureentry.cpp`

- `lltextureentry.h`

- `lltree_common.h`

- `lltreeparams.cpp`

- `lltreeparams.h`

- `llvolumemessage.cpp`

- `llvolumemessage.h`

- `material_codes.cpp`

- `material_codes.h`

- `object_flags.h`


## indra/llprimitive/tests/ (13 files)

- `alcompressedupdate_test.cpp`

- `alobjectmotion_test.cpp`

- `alobjectorphans_test.cpp`

- `alobjectupdate_test.cpp`

- `llgltfmaterial_test.cpp`

- `llmaterial_test.cpp`

- `llmaterialid_test.cpp`

- `llmediaentry_test.cpp`

- `llmessagesystem_stub.cpp`

- `llmodel_test.cpp`

- `llprimitive_test.cpp`

- `llprimitivetemessage_test.cpp`

- `lltextureentry_test.cpp`


## indra/llrender/ (88 files)

- `CMakeLists.txt`

- `aldepthbounds.cpp`

- `aldepthbounds.h`

- `alfontcolrv1.cpp`

- `alfontcolrv1.h`

- `alfontface.cpp`

- `alfontface.h`

- `alfontshaping.cpp`

- `alfontshaping.h`

- `alframefences.cpp`

- `alframefences.h`

- `algpubuffer.cpp`

- `algpubuffer.h`

- `algputimer.cpp`

- `algputimer.h`

- `alimageslot.cpp`

- `alimageslot.h`

- `alpacingslack.cpp`

- `alpacingslack.h`

- `alprimitiveplot.cpp`

- `alprimitiveplot.h`

- `alquerypool.cpp`

- `alquerypool.h`

- `alrendertargetdesc.h`

- `alsamplerstate.cpp`

- `alsamplerstate.h`

- `alstagingring.cpp`

- `alstagingring.h`

- `altexture3d.cpp`

- `altexture3d.h`

- `altextureblit.cpp`

- `altextureblit.h`

- `altexturereadback.cpp`

- `altexturereadback.h`

- `altextureslot.cpp`

- `altextureslot.h`

- `aluniformbuffer.cpp`

- `aluniformbuffer.h`

- `alvramusage.cpp`

- `alvramusage.h`

- `llcubemap.cpp`

- `llcubemap.h`

- `llcubemaparray.cpp`

- `llcubemaparray.h`

- `llfontbitmapcache.cpp`

- `llfontbitmapcache.h`

- `llfontfreetype.cpp`

- `llfontfreetype.h`

- `llfontgl.cpp`

- `llfontgl.h`

- `llfontregistry.cpp`

- `llfontregistry.h`

- `llfonttextcache.cpp`

- `llfonttextcache.h`

- `llgl.cpp`

- `llgl.h`

- `llglcommonfunc.cpp`

- `llglcommonfunc.h`

- `llglheaders.h`

- `llglslshader.cpp`

- `llglslshader.h`

- `llglstates.h`

- `llgltexture.cpp`

- `llgltexture.h`

- `llgltypes.h`

- `llimagegl.cpp`

- `llimagegl.h`

- `llrender.cpp`

- `llrender.h`

- `llrender2dutils.cpp`

- `llrender2dutils.h`

- `llrendernavprim.cpp`

- `llrendernavprim.h`

- `llrendersphere.cpp`

- `llrendersphere.h`

- `llrendertarget.cpp`

- `llrendertarget.h`

- `llshadermgr.cpp`

- `llshadermgr.h`

- `lltexture.cpp`

- `lltexture.h`

- `lltexturemanagerbridge.cpp`

- `lltexturemanagerbridge.h`

- `lluiimage.cpp`

- `lluiimage.h`

- `lluiimage.inl`

- `llvertexbuffer.cpp`

- `llvertexbuffer.h`


## indra/llrender/tests/ (46 files)

- `aldepthbounds_gl_test.cpp`

- `aldriversync_bench.cpp`

- `alfontcolrv1_gl_test.cpp`

- `alfontcolrv1_test.cpp`

- `alfontshaping_gl_test.cpp`

- `alfontshaping_test.cpp`

- `alframefences_gl_test.cpp`

- `algpubuffer_gl_test.cpp`

- `algputimer_gl_test.cpp`

- `alimageslot_gl_test.cpp`

- `alinfiniteprojection_gl_test.cpp`

- `alinstanceddraw_gl_test.cpp`

- `alpacingslack_test.cpp`

- `alquerypool_gl_test.cpp`

- `alrenderstate_gl_test.cpp`

- `alrendertargetdesc_test.cpp`

- `alstagingring_gl_test.cpp`

- `altessellation_gl_test.cpp`

- `altextureblit_gl_test.cpp`

- `altexturereadback_gl_test.cpp`

- `aluniformbuffer_gl_test.cpp`

- `alvramusage_gl_test.cpp`

- `alwindowsdlheadless_test.cpp`

- `llfontbitmapcache_gl_test.cpp`

- `llfontbitmapcache_test.cpp`

- `llfontfreetype_gl_test.cpp`

- `llfontfreetype_test.cpp`

- `llfontgl_test.cpp`

- `llfontregistry_gl_test.cpp`

- `llfontregistry_test.cpp`

- `llfonttest_helpers.h`

- `llfonttextcache_test.cpp`

- `llglerrors_gl_test.cpp`

- `llglfloor_test.cpp`

- `llglslshader_gl_test.cpp`

- `llgltexture_test.cpp`

- `llheadlessgl_fixture.h`

- `llimagegl_test.cpp`

- `llrender2dutils_gl_test.cpp`

- `llrender_test_checks.cpp`

- `llrendermatrix_test.cpp`

- `llrendersphere_gl_test.cpp`

- `llrendertarget_gl_test.cpp`

- `lluiimage_test.cpp`

- `lluitransform_test.cpp`

- `llvertexbuffer_gl_test.cpp`


## indra/llui/ (227 files)

- `CMakeLists.txt`

- `fsvirtualtrackpad.cpp`

- `fsvirtualtrackpad.h`

- `llaccordionctrl.cpp`

- `llaccordionctrl.h`

- `llaccordionctrltab.cpp`

- `llaccordionctrltab.h`

- `llbadge.cpp`

- `llbadge.h`

- `llbadgeholder.cpp`

- `llbadgeholder.h`

- `llbadgeowner.cpp`

- `llbadgeowner.h`

- `llbutton.cpp`

- `llbutton.h`

- `llcallbackmap.h`

- `llchat.h`

- `llchatautocompletemodel.cpp`

- `llchatautocompletemodel.h`

- `llchatentry.cpp`

- `llchatentry.h`

- `llchatmentionhelper.cpp`

- `llchatmentionhelper.h`

- `llcheckboxctrl.cpp`

- `llcheckboxctrl.h`

- `llclipboard.cpp`

- `llclipboard.h`

- `llcombobox.cpp`

- `llcombobox.h`

- `llcommandmanager.cpp`

- `llcommandmanager.h`

- `llconsole.cpp`

- `llconsole.h`

- `llcontainerview.cpp`

- `llcontainerview.h`

- `llctrlselectioninterface.cpp`

- `llctrlselectioninterface.h`

- `lldockablefloater.cpp`

- `lldockablefloater.h`

- `lldockcontrol.cpp`

- `lldockcontrol.h`

- `lldraghandle.cpp`

- `lldraghandle.h`

- `lleditmenuhandler.cpp`

- `lleditmenuhandler.h`

- `llemojidictionary.cpp`

- `llemojidictionary.h`

- `llemojihelper.cpp`

- `llemojihelper.h`

- `llf32uictrl.cpp`

- `llf32uictrl.h`

- `llfiltereditor.cpp`

- `llfiltereditor.h`

- `llflashtimer.cpp`

- `llflashtimer.h`

- `llflatlistview.cpp`

- `llflatlistview.h`

- `llfloater.cpp`

- `llfloater.h`

- `llfloaterreg.cpp`

- `llfloaterreg.h`

- `llfloaterreglistener.cpp`

- `llfloaterreglistener.h`

- `llflyoutbutton.cpp`

- `llflyoutbutton.h`

- `llfocusmgr.cpp`

- `llfocusmgr.h`

- `llfolderview.cpp`

- `llfolderview.h`

- `llfolderviewitem.cpp`

- `llfolderviewitem.h`

- `llfolderviewmodel.cpp`

- `llfolderviewmodel.h`

- `llfunctorregistry.h`

- `llgestureautocompletehelper.cpp`

- `llgestureautocompletehelper.h`

- `llhelp.h`

- `lliconctrl.cpp`

- `lliconctrl.h`

- `lllayoutstack.cpp`

- `lllayoutstack.h`

- `lllazyvalue.h`

- `lllineeditor.cpp`

- `lllineeditor.h`

- `llloadingindicator.cpp`

- `llloadingindicator.h`

- `lllocalcliprect.cpp`

- `lllocalcliprect.h`

- `llmenubutton.cpp`

- `llmenubutton.h`

- `llmenugl.cpp`

- `llmenugl.h`

- `llmodaldialog.cpp`

- `llmodaldialog.h`

- `llmultifloater.cpp`

- `llmultifloater.h`

- `llmultislider.cpp`

- `llmultislider.h`

- `llmultisliderctrl.cpp`

- `llmultisliderctrl.h`

- `llnotificationptr.h`

- `llnotifications.cpp`

- `llnotifications.h`

- `llnotificationslistener.cpp`

- `llnotificationslistener.h`

- `llnotificationsutil.cpp`

- `llnotificationsutil.h`

- `llnotificationtemplate.h`

- `llnotificationvisibilityrule.h`

- `llpanel.cpp`

- `llpanel.h`

- `llprogressbar.cpp`

- `llprogressbar.h`

- `llradiogroup.cpp`

- `llradiogroup.h`

- `llresizebar.cpp`

- `llresizebar.h`

- `llresizehandle.cpp`

- `llresizehandle.h`

- `llresmgr.cpp`

- `llresmgr.h`

- `llscrollbar.cpp`

- `llscrollbar.h`

- `llscrollcontainer.cpp`

- `llscrollcontainer.h`

- `llscrollingpanellist.cpp`

- `llscrollingpanellist.h`

- `llscrolllistcell.cpp`

- `llscrolllistcell.h`

- `llscrolllistcolumn.cpp`

- `llscrolllistcolumn.h`

- `llscrolllistctrl.cpp`

- `llscrolllistctrl.h`

- `llscrolllistitem.cpp`

- `llscrolllistitem.h`

- `llsearchablecontrol.h`

- `llsearcheditor.cpp`

- `llsearcheditor.h`

- `llslider.cpp`

- `llslider.h`

- `llsliderctrl.cpp`

- `llsliderctrl.h`

- `llspellcheck.cpp`

- `llspellcheck.h`

- `llspellcheckengine.h`

- `llspellcheckengine_hunspell.cpp`

- `llspellcheckengine_mac.mm`

- `llspellcheckengine_win32.cpp`

- `llspellcheckmenuhandler.h`

- `llspinctrl.cpp`

- `llspinctrl.h`

- `llstatbar.cpp`

- `llstatbar.h`

- `llstatgraph.cpp`

- `llstatgraph.h`

- `llstatview.cpp`

- `llstatview.h`

- `llstyle.cpp`

- `llstyle.h`

- `lltabcontainer.cpp`

- `lltabcontainer.h`

- `lltextbase.cpp`

- `lltextbase.h`

- `lltextbox.cpp`

- `lltextbox.h`

- `lltexteditor.cpp`

- `lltexteditor.h`

- `lltextparser.cpp`

- `lltextparser.h`

- `lltextutil.cpp`

- `lltextutil.h`

- `lltextvalidate.cpp`

- `lltextvalidate.h`

- `lltimectrl.cpp`

- `lltimectrl.h`

- `lltoggleablemenu.cpp`

- `lltoggleablemenu.h`

- `lltoolbar.cpp`

- `lltoolbar.h`

- `lltooltip.cpp`

- `lltooltip.h`

- `lltrans.cpp`

- `lltrans.h`

- `lltransutil.cpp`

- `lltransutil.h`

- `llui.cpp`

- `llui.h`

- `lluicolor.cpp`

- `lluicolor.h`

- `lluicolortable.cpp`

- `lluicolortable.h`

- `lluiconstants.h`

- `lluictrl.cpp`

- `lluictrl.h`

- `lluictrlfactory.cpp`

- `lluictrlfactory.h`

- `lluifwd.h`

- `lluistring.cpp`

- `lluistring.h`

- `llundo.cpp`

- `llundo.h`

- `llurlaction.cpp`

- `llurlaction.h`

- `llurlentry.cpp`

- `llurlentry.h`

- `llurlmatch.cpp`

- `llurlmatch.h`

- `llurlregistry.cpp`

- `llurlregistry.h`

- `llview.cpp`

- `llview.h`

- `llviewborder.cpp`

- `llviewborder.h`

- `llviewinject.cpp`

- `llviewinject.h`

- `llviewmodel.cpp`

- `llviewmodel.h`

- `llviewquery.cpp`

- `llviewquery.h`

- `llvirtualtrackball.cpp`

- `llvirtualtrackball.h`

- `llwindowshade.cpp`

- `llwindowshade.h`

- `llxuiparser.cpp`

- `llxuiparser.h`

- `llxyvector.cpp`

- `llxyvector.h`


## indra/llui/base/ (14 files)

- `aldeferredrebuild.cpp`

- `aldeferredrebuild.h`

- `aldraggesture.cpp`

- `aldraggesture.h`

- `alfuzzymatch.cpp`

- `alfuzzymatch.h`

- `alplace.cpp`

- `alplace.h`

- `alsaid.h`

- `alstringmatch.h`

- `alsurface.cpp`

- `alsurface.h`

- `alundostack.h`

- `alviewtype.h`


## indra/llui/code/ (28 files)

- `albracketindex.cpp`

- `albracketindex.h`

- `alchangepeek.cpp`

- `alchangepeek.h`

- `alchangessincesaved.cpp`

- `alchangessincesaved.h`

- `alcodecards.cpp`

- `alcodecards.h`

- `alcodeeditor.cpp`

- `alcodeeditor.h`

- `alcodeliterals.cpp`

- `alcodeliterals.h`

- `alcompletionmodel.cpp`

- `alcompletionmodel.h`

- `alfixlistmodel.cpp`

- `alfixlistmodel.h`

- `alfoldmodel.cpp`

- `alfoldmodel.h`

- `alkeychord.cpp`

- `alkeychord.h`

- `alkeymap.cpp`

- `alkeymap.h`

- `alsnippetsession.cpp`

- `alsnippetsession.h`

- `alsyntaxgrammar.cpp`

- `alsyntaxgrammar.h`

- `alsyntaxhighlighter.cpp`

- `alsyntaxhighlighter.h`


## indra/llui/diff/ (41 files)

- `aldiffbar.cpp`

- `aldiffbar.h`

- `aldiffcolors.cpp`

- `aldiffcolors.h`

- `aldiffedit.cpp`

- `aldiffedit.h`

- `aldifffill.cpp`

- `aldifffill.h`

- `aldiffids.h`

- `aldifflexer.cpp`

- `aldifflexer.h`

- `aldiffmerge.cpp`

- `aldiffmerge.h`

- `aldiffmodel.cpp`

- `aldiffmodel.h`

- `aldiffmoves.cpp`

- `aldiffmoves.h`

- `aldiffrangesame.cpp`

- `aldiffrangesame.h`

- `aldiffsame.cpp`

- `aldiffsame.h`

- `aldiffsplice.cpp`

- `aldiffsplice.h`

- `aldifftokens.cpp`

- `aldifftokens.h`

- `aldiffview.cpp`

- `aldiffview.h`

- `allinediff.cpp`

- `allinediff.h`

- `allinepairs.cpp`

- `allinepairs.h`

- `alstructuraldiff.cpp`

- `alstructuraldiff.h`

- `altextdiff.cpp`

- `altextdiff.h`

- `altextmerge.cpp`

- `altextmerge.h`

- `alunifieddiff.cpp`

- `alunifieddiff.h`

- `alworddiff.cpp`

- `alworddiff.h`


## indra/llui/fields/ (30 files)

- `alangledial.cpp`

- `alangledial.h`

- `alcolorfield.cpp`

- `alcolorfield.h`

- `alcolorpicker.cpp`

- `alcolorpicker.h`

- `alcolorsheet.cpp`

- `alcolorsheet.h`

- `alcolortablepanel.cpp`

- `alcolortablepanel.h`

- `alcornerfield.cpp`

- `alcornerfield.h`

- `alfieldeditors.cpp`

- `alfieldeditors.h`

- `alflagsfield.cpp`

- `alflagsfield.h`

- `alfollowscontrol.cpp`

- `alfollowscontrol.h`

- `alfontfield.cpp`

- `alfontfield.h`

- `alimagefield.cpp`

- `alimagefield.h`

- `aloffsetpad.cpp`

- `aloffsetpad.h`

- `alpicturefield.cpp`

- `alpicturefield.h`

- `alpropertygrid.cpp`

- `alpropertygrid.h`

- `alsettingrow.cpp`

- `alsettingrow.h`


## indra/llui/studio/ (28 files)

- `aldockpanel.cpp`

- `aldockpanel.h`

- `alemptystate.cpp`

- `alemptystate.h`

- `alfindings.h`

- `alfolderfilter.cpp`

- `alfolderfilter.h`

- `alhistorylist.cpp`

- `alhistorylist.h`

- `alkeycapture.cpp`

- `alkeycapture.h`

- `alkeyshome.h`

- `almenuslot.cpp`

- `almenuslot.h`

- `aloutputview.cpp`

- `aloutputview.h`

- `alpanefolds.cpp`

- `alpanefolds.h`

- `alpanelist.cpp`

- `alpanelist.h`

- `alpaneroom.cpp`

- `alpaneroom.h`

- `alquickask.cpp`

- `alquickask.h`

- `alquickopen.cpp`

- `alquickopen.h`

- `alstudiofloater.cpp`

- `alstudiofloater.h`


## indra/llui/tests/ (130 files)

- `alanchoredranges_test.cpp`

- `alangledial_test.cpp`

- `albracketindex_test.cpp`

- `alcanvasview_test.cpp`

- `alchangepeek_test.cpp`

- `alchoicelist_test.cpp`

- `alcodecards_test.cpp`

- `alcodeeditor_test.cpp`

- `alcolorfield_test.cpp`

- `alcolorpicker_test.cpp`

- `alcolorsheet_test.cpp`

- `alcolortablepanel_test.cpp`

- `alcompletionmodel_test.cpp`

- `alcornerfield_test.cpp`

- `aldifflexer_test.cpp`

- `aldiffmerge_test.cpp`

- `aldiffmodel_test.cpp`

- `aldiffview_gl_test.cpp`

- `aldiffview_test.cpp`

- `aldockpanel_test.cpp`

- `aldraggesture_test.cpp`

- `alemptystate_test.cpp`

- `alfenwicktree_test.cpp`

- `alfindbar_test.cpp`

- `alfixlistmodel_test.cpp`

- `alflagsfield_test.cpp`

- `alfolderfilter_test.cpp`

- `alfoldmodel_test.cpp`

- `alfollowscontrol_test.cpp`

- `alfontfield_test.cpp`

- `alfuzzymatch_test.cpp`

- `alheadlessui_fixture.h`

- `alhistorylist_test.cpp`

- `alimagefield_test.cpp`

- `aljumpbar_test.cpp`

- `alkeycapture_test.cpp`

- `alkeymap_test.cpp`

- `allinetable_test.cpp`

- `almaxima_test.cpp`

- `almenuslot_test.cpp`

- `alnotecarditems_test.cpp`

- `aloffsetpad_test.cpp`

- `aloutputview_test.cpp`

- `alpanefolds_test.cpp`

- `alpanelist_test.cpp`

- `alpaneroom_test.cpp`

- `alplace_test.cpp`

- `alpopover_test.cpp`

- `alprefixsums_test.cpp`

- `alpropertygrid_test.cpp`

- `alquickopen_test.cpp`

- `alscopebar_test.cpp`

- `alsettingrow_test.cpp`

- `alsnippetsession_test.cpp`

- `alspecimenlist_test.cpp`

- `alstringmatch_test.cpp`

- `alstudiofloater_test.cpp`

- `alsurface_gl_test.cpp`

- `alsurface_test.cpp`

- `alsyntaxgrammars_test.cpp`

- `alsyntaxhighlighter_test.cpp`

- `altabstrip_test.cpp`

- `altesttempdir.h`

- `altextcarets_test.cpp`

- `altextdiff_bench.cpp`

- `altextdiff_test.cpp`

- `altextdocument_test.cpp`

- `altextdraw_bench.cpp`

- `altextediting_test.cpp`

- `altextengine_bench.cpp`

- `altextfind_test.cpp`

- `altextgotoline_test.cpp`

- `altextindent_test.cpp`

- `altextlayout_test.cpp`

- `altextsearch_test.cpp`

- `altextspelling_test.cpp`

- `altextundo_test.cpp`

- `altextview_gl_test.cpp`

- `altextview_test.cpp`

- `altextviewprobe.h`

- `aluigl_fixture.h`

- `aluistatescope.h`

- `alundostack_test.cpp`

- `alunifieddiff_test.cpp`

- `alviewtype_test.cpp`

- `alvimkeymap_test.cpp`

- `alvimmappings_test.cpp`

- `alvimpattern_test.cpp`

- `alvimregisters_test.cpp`

- `alxuicatalog_test.cpp`

- `alxuidiagnostics_test.cpp`

- `alxuidocuments_test.cpp`

- `alxuiedit_test.cpp`

- `alxuifields_test.cpp`

- `alxuifill_test.cpp`

- `alxuifindings_test.cpp`

- `alxuilint_test.cpp`

- `alxuinotes_test.cpp`

- `alxuioverlay_test.cpp`

- `alxuischema_test.cpp`

- `alxuiselection_test.cpp`

- `alxuiservice_test.cpp`

- `alxuishellbuild_test.cpp`

- `alxuisourcemap_test.cpp`

- `alxuitranslate_test.cpp`

- `alxuitreemodel_test.cpp`

- `llaccordionctrltab_test.cpp`

- `llchatautocompletemodel_test.cpp`

- `llcombobox_test.cpp`

- `llconsole_test.cpp`

- `llemojidictionary_test.cpp`

- `llfloater_test.cpp`

- `llfocusmgr_test.cpp`

- `lllayoutstack_test.cpp`

- `llradiogroup_test.cpp`

- `llresizebar_test.cpp`

- `llscrolllistctrl_test.cpp`

- `llspinctrl_test.cpp`

- `llstatbar_test.cpp`

- `lltabcontainer_test.cpp`

- `lltextparser_test.cpp`

- `llui_test_checks.cpp`

- `llui_test_fakes.cpp`

- `lluicolortable_test.cpp`

- `lluistring_test.cpp`

- `llurlentry_test.cpp`

- `llurlmatch_test.cpp`

- `llurlregistry_test.cpp`

- `llview_test.cpp`

- `llxuiparser_test.cpp`


## indra/llui/text/ (38 files)

- `alanchoredranges.h`

- `alfenwicktree.h`

- `alfindbar.cpp`

- `alfindbar.h`

- `allinetable.h`

- `almaxima.h`

- `alnotecarditems.cpp`

- `alnotecarditems.h`

- `alprefixsums.h`

- `alsmartselect.cpp`

- `alsmartselect.h`

- `altextcaret.h`

- `altextcarets.cpp`

- `altextcarets.h`

- `altextchars.h`

- `altextdocument.cpp`

- `altextdocument.h`

- `altextediting.cpp`

- `altextediting.h`

- `altextfeatures.h`

- `altextfind.cpp`

- `altextfind.h`

- `altextgotoline.cpp`

- `altextgotoline.h`

- `altextindent.cpp`

- `altextindent.h`

- `altextlayout.cpp`

- `altextlayout.h`

- `altextruler.cpp`

- `altextruler.h`

- `altextsearch.cpp`

- `altextsearch.h`

- `altextspelling.cpp`

- `altextspelling.h`

- `altextundo.cpp`

- `altextundo.h`

- `altextview.cpp`

- `altextview.h`


## indra/llui/utils/ (10 files)

- `CMakeLists.txt`

- `alparamfingerprint.cpp`

- `alparamfingerprint.h`

- `llui_libtest.cpp`

- `llui_libtest.h`

- `llwidgetreg.cpp`

- `llwidgetreg.h`

- `xui_overlay_baseline.txt`

- `xui_overlay_check.cpp`

- `xui_translate_repair.cpp`


## indra/llui/vim/ (16 files)

- `alvimcommandline.cpp`

- `alvimcommandline.h`

- `alvimexcommands.cpp`

- `alvimexcommands.h`

- `alvimhost.h`

- `alvimkeymap.cpp`

- `alvimkeymap.h`

- `alvimmappings.cpp`

- `alvimmappings.h`

- `alvimpattern.cpp`

- `alvimpattern.h`

- `alvimregisters.cpp`

- `alvimregisters.h`

- `alvimsearch.cpp`

- `alvimsearch.h`

- `alvimtext.h`


## indra/llui/widgets/ (16 files)

- `alchoicelist.cpp`

- `alchoicelist.h`

- `alchoicepopup.cpp`

- `alchoicepopup.h`

- `alflatbutton.cpp`

- `alflatbutton.h`

- `aljumpbar.cpp`

- `aljumpbar.h`

- `alpopover.cpp`

- `alpopover.h`

- `alscopebar.cpp`

- `alscopebar.h`

- `alspecimenlist.cpp`

- `alspecimenlist.h`

- `altabstrip.cpp`

- `altabstrip.h`


## indra/llui/xui/ (33 files)

- `alcanvasview.cpp`

- `alcanvasview.h`

- `alxuicatalog.cpp`

- `alxuicatalog.h`

- `alxuidiagnostics.cpp`

- `alxuidiagnostics.h`

- `alxuidocuments.cpp`

- `alxuidocuments.h`

- `alxuiedit.cpp`

- `alxuiedit.h`

- `alxuifields.cpp`

- `alxuifields.h`

- `alxuifindings.h`

- `alxuilint.cpp`

- `alxuilint.h`

- `alxuinotes.cpp`

- `alxuinotes.h`

- `alxuioverlay.cpp`

- `alxuioverlay.h`

- `alxuischema.cpp`

- `alxuischema.h`

- `alxuiselection.cpp`

- `alxuiselection.h`

- `alxuiservice.cpp`

- `alxuiservice.h`

- `alxuishellbuild.cpp`

- `alxuishellbuild.h`

- `alxuisourcemap.cpp`

- `alxuisourcemap.h`

- `alxuitranslate.cpp`

- `alxuitranslate.h`

- `alxuitreemodel.cpp`

- `alxuitreemodel.h`


## indra/llwebrtc/ (8 files)

- `CMakeLists.txt`

- `alaudiodevicenotifier.cpp`

- `alaudiodevicenotifier.h`

- `alaudioechobuffer.cpp`

- `alaudioechobuffer.h`

- `llwebrtc.cpp`

- `llwebrtc.h`

- `llwebrtc_impl.h`


## indra/llwindow/ (40 files)

- `CMakeLists.txt`

- `alwindowsdlheadless.cpp`

- `alwindowsdlheadless.h`

- `llcursortypes.cpp`

- `llcursortypes.h`

- `lldragdropwin32.cpp`

- `lldragdropwin32.h`

- `lldxhardware.cpp`

- `lldxhardware.h`

- `llgamecontrol.cpp`

- `llgamecontrol.h`

- `llgamecontroltranslator.cpp`

- `llgamecontroltranslator.h`

- `llkeyboard.cpp`

- `llkeyboard.h`

- `llkeyboardheadless.cpp`

- `llkeyboardheadless.h`

- `llkeyboardsdl.cpp`

- `llkeyboardsdl.h`

- `llkeyboardwin32.cpp`

- `llkeyboardwin32.h`

- `llmousehandler.cpp`

- `llmousehandler.h`

- `llpreeditor.h`

- `llscrolldelta.h`

- `llsdl.cpp`

- `llsdl.h`

- `llsdl_macos.h`

- `llsdl_macos.mm`

- `llwindow.cpp`

- `llwindow.h`

- `llwindowcallbacks.cpp`

- `llwindowcallbacks.h`

- `llwindowheadless.cpp`

- `llwindowheadless.h`

- `llwindowmacosx_iokit.h`

- `llwindowsdl.cpp`

- `llwindowsdl.h`

- `llwindowwin32.cpp`

- `llwindowwin32.h`


## indra/llxml/ (13 files)

- `CMakeLists.txt`

- `alxmldocument.cpp`

- `alxmldocument.h`

- `alxmllayermerge.cpp`

- `alxmllayermerge.h`

- `alxmlmergelog.cpp`

- `alxmlmergelog.h`

- `llcontrol.cpp`

- `llcontrol.h`

- `llxmlnode.cpp`

- `llxmlnode.h`

- `llxmltree.cpp`

- `llxmltree.h`


## indra/llxml/tests/ (4 files)

- `alxmllayermerge_test.cpp`

- `llcontrol_test.cpp`

- `llxml_test_checks.cpp`

- `llxmlnode_test.cpp`


## indra/lscript/ (14 files)

- `CMakeLists.txt`

- `allslreference.cpp`

- `allslreference.h`

- `llscriptresource.h`

- `llscriptresourceconsumer.h`

- `llscriptresourcepool.h`

- `lscript_alloc.h`

- `lscript_byteconvert.h`

- `lscript_byteformat.h`

- `lscript_execute.h`

- `lscript_export.h`

- `lscript_http.h`

- `lscript_library.h`

- `lscript_rt_interface.h`


## indra/lscript/fuzz/ (4 files)

- `allsofuzz.h`

- `allsofuzzprogram.cpp`

- `allsofuzzsource.cpp`

- `lsl.dict`


## indra/lscript/lscript_compile/ (17 files)

- `indra.l`

- `indra.y`

- `lscript_alloc.cpp`

- `lscript_bytecode.cpp`

- `lscript_bytecode.h`

- `lscript_error.cpp`

- `lscript_error.h`

- `lscript_heap.cpp`

- `lscript_heap.h`

- `lscript_resource.cpp`

- `lscript_resource.h`

- `lscript_scope.cpp`

- `lscript_scope.h`

- `lscript_tree.cpp`

- `lscript_tree.h`

- `lscript_typecheck.cpp`

- `lscript_typecheck.h`


## indra/lscript/lscript_execute/ (8 files)

- `llscriptresource.cpp`

- `llscriptresourceconsumer.cpp`

- `llscriptresourcepool.cpp`

- `lscript_execute.cpp`

- `lscript_heapruntime.cpp`

- `lscript_heapruntime.h`

- `lscript_readlso.cpp`

- `lscript_readlso.h`


## indra/lscript/lscript_library/ (3 files)

- `lscript_alloc.cpp`

- `lscript_export.cpp`

- `lscript_library.cpp`


## indra/lscript/tests/ (6 files)

- `allslreference_test.cpp`

- `allslreferencecheck_test.cpp`

- `allsolibrary.cpp`

- `allsolibrary.h`

- `allsovm_test.cpp`

- `allsovmrun.h`


## indra/lscript/tests/regressions/ (10 files)

- `float_to_integer_out_of_range.lsl`

- `infinite_vector_cast.lsl`

- `infinite_vector_list_postadd.lsl`

- `infinite_vector_list_preadd.lsl`

- `list_constant_infinite_component.lsl`

- `list_in_list_literal.lsl`

- `long_operator_chain.lsl`

- `many_empty_statements.lsl`

- `nul_in_string_literal.lsl`

- `unset_global_in_list_literal.lsl`


## indra/media_plugins/ (1 files)

- `CMakeLists.txt`


## indra/media_plugins/base/ (3 files)

- `CMakeLists.txt`

- `media_plugin_base.cpp`

- `media_plugin_base.h`


## indra/media_plugins/cef/ (9 files)

- `CMakeLists.txt`

- `SLPluginCEF-Info.plist.in`

- `mac_volume_catcher.cpp`

- `media_plugin_cef.cpp`

- `slplugin_cef.cpp`

- `slplugin_cef_bootstrap.cpp`

- `volume_catcher.h`

- `volume_catcher_null.cpp`

- `windows_volume_catcher.cpp`


## indra/media_plugins/cef/linux/ (7 files)

- `volume_catcher_linux.cpp`

- `volume_catcher_linux.h`

- `volume_catcher_pipewire.cpp`

- `volume_catcher_pipewire_syms.inc`

- `volume_catcher_pulseaudio.cpp`

- `volume_catcher_pulseaudio_glib_syms.inc`

- `volume_catcher_pulseaudio_syms.inc`


## indra/media_plugins/example/ (2 files)

- `CMakeLists.txt`

- `media_plugin_example.cpp`


## indra/media_plugins/gstreamer10/ (3 files)

- `CMakeLists.txt`

- `llmediaimplgstreamer_syms_raw.inc`

- `media_plugin_gstreamer10.cpp`


## indra/media_plugins/libvlc/ (2 files)

- `CMakeLists.txt`

- `media_plugin_libvlc.cpp`


## indra/newview/ (1803 files)

- `CMakeLists.txt`

- `Info-AlchemySDL.plist`

- `SMAAAreaTex.h`

- `SMAASearchTex.h`

- `VIEWER_VERSION.txt`

- `alagentlistupdates.h`

- `alagentlocationformat.cpp`

- `alagentlocationformat.h`

- `alapplinks.cpp`

- `alapplinks.h`

- `alassetblocklist.cpp`

- `alassetblocklist.h`

- `alavataractions.cpp`

- `alavataractions.h`

- `alavatargroups.cpp`

- `alavatargroups.h`

- `albakeproxies.cpp`

- `albakeproxies.h`

- `albulkrename.cpp`

- `albulkrename.h`

- `alchatautocomplete.cpp`

- `alchatautocomplete.h`

- `alchatbar.cpp`

- `alchatbar.h`

- `alchatcommand.cpp`

- `alchatcommand.h`

- `alchattimestamp.cpp`

- `alchattimestamp.h`

- `alcheatcodes.cpp`

- `alclassifieditem.cpp`

- `alclassifieditem.h`

- `alcolorpopover.cpp`

- `alcolorpopover.h`

- `alcolorwheelctrl.cpp`

- `alcolorwheelctrl.h`

- `alcolorwheelmodel.cpp`

- `alcolorwheelmodel.h`

- `alcrashreporter.cpp`

- `alcrashreporter.h`

- `alcrashreporter_cocoa.mm`

- `alcrashreporter_native.cpp`

- `alcrashreporter_run.cpp`

- `alcurveeditorctrl.cpp`

- `alcurveeditorctrl.h`

- `alcurvemodel.cpp`

- `alcurvemodel.h`

- `aldaycyclelandmarks.cpp`

- `aldaycyclelandmarks.h`

- `alderenderlist.cpp`

- `alderenderlist.h`

- `aldiscordmanager.cpp`

- `aldiscordmanager.h`

- `aldroptarget.cpp`

- `aldroptarget.h`

- `alfarplaneoverlay.cpp`

- `alfarplaneoverlay.h`

- `alfeedback.cpp`

- `alfeedback.h`

- `alfeedback_send.cpp`

- `alfeedbackoutbox.cpp`

- `alfeedbackoutbox.h`

- `alfloaterblocked.cpp`

- `alfloaterblocked.h`

- `alfloaterbulkrename.cpp`

- `alfloaterbulkrename.h`

- `alfloaterdirectory.cpp`

- `alfloaterdirectory.h`

- `alfloaterevent.cpp`

- `alfloaterevent.h`

- `alfloaterexploresounds.cpp`

- `alfloaterexploresounds.h`

- `alfloaterfeedback.cpp`

- `alfloaterfeedback.h`

- `alfloaterfeedbackpreview.cpp`

- `alfloaterfeedbackpreview.h`

- `alfloatergenerictext.cpp`

- `alfloatergenerictext.h`

- `alfloatergroupprofile.cpp`

- `alfloatergroupprofile.h`

- `alfloaterlightbox.cpp`

- `alfloaterlightbox.h`

- `alfloaterparticleeditor.cpp`

- `alfloaterparticleeditor.h`

- `alfloaterprofilelegacy.cpp`

- `alfloaterprofilelegacy.h`

- `alfloaterprogressview.cpp`

- `alfloaterprogressview.h`

- `alfloaterregiontracker.cpp`

- `alfloaterregiontracker.h`

- `alfloatersceneexplorer.cpp`

- `alfloatersceneexplorer.h`

- `alfloatersceneexplorerfilters.cpp`

- `alfloatersceneexplorerfilters.h`

- `alfloaterscopes.cpp`

- `alfloaterscopes.h`

- `alfloaterscriptpreferences.cpp`

- `alfloaterscriptpreferences.h`

- `alfloaterscriptstudio.cpp`

- `alfloaterscriptstudio.h`

- `alfloatertransactionlog.cpp`

- `alfloatertransactionlog.h`

- `alfloaterwebprofile.cpp`

- `alfloaterwebprofile.h`

- `alfloaterxuilibrary.cpp`

- `alfloaterxuilibrary.h`

- `alfloaterxuistudio.cpp`

- `alfloaterxuistudio.h`

- `alfollowednotecard.cpp`

- `alfollowednotecard.h`

- `alfriendbacklog.h`

- `algltfmaterialretry.h`

- `algltfoverridestate.h`

- `algradehistory.cpp`

- `algradehistory.h`

- `algroupchanges.h`

- `algroupmembers.h`

- `alhoverglow.cpp`

- `alhoverglow.h`

- `allegacynotificationwellwindow.cpp`

- `allegacynotificationwellwindow.h`

- `allightboxdirectory.cpp`

- `allightboxdirectory.h`

- `almaturitypreference.h`

- `almeshuploadassets.h`

- `almotionpredictor.cpp`

- `almotionpredictor.h`

- `almutelookup.h`

- `alnotecardembedded.cpp`

- `alnotecardembedded.h`

- `alnotecardworld.cpp`

- `alnotecardworld.h`

- `alobjectcapture.cpp`

- `alobjectcapture.h`

- `alobjectproperties.cpp`

- `alobjectproperties.h`

- `alobjectroster.h`

- `alpanelaomini.cpp`

- `alpanelaomini.h`

- `alpanelaopulldown.cpp`

- `alpanelaopulldown.h`

- `alpanelavatarlegacy.cpp`

- `alpanelavatarlegacy.h`

- `alpanelclassified.cpp`

- `alpanelclassified.h`

- `alpanelclassifiededit.cpp`

- `alpanelclassifiededit.h`

- `alpaneleventinfo.cpp`

- `alpaneleventinfo.h`

- `alpanelmusicticker.cpp`

- `alpanelmusicticker.h`

- `alpanelpick.cpp`

- `alpanelpick.h`

- `alpanelprofilelegacy.cpp`

- `alpanelprofilelegacy.h`

- `alpanelquicksettings.cpp`

- `alpanelquicksettings.h`

- `alpanelquicksettingspulldown.cpp`

- `alpanelquicksettingspulldown.h`

- `alpanelradaralert.cpp`

- `alpanelradaralert.h`

- `alpanelscriptaliases.cpp`

- `alpanelscriptaliases.h`

- `alpanelscriptkeymap.cpp`

- `alpanelscriptkeymap.h`

- `alpanelsearchbase.cpp`

- `alpanelsearchbase.h`

- `alpanelsearchclassifieds.cpp`

- `alpanelsearchclassifieds.h`

- `alpanelsearchevents.cpp`

- `alpanelsearchevents.h`

- `alpanelsearchgroups.cpp`

- `alpanelsearchgroups.h`

- `alpanelsearchlandsales.cpp`

- `alpanelsearchlandsales.h`

- `alpanelsearchpeople.cpp`

- `alpanelsearchpeople.h`

- `alpanelsearchplaces.cpp`

- `alpanelsearchplaces.h`

- `alpanelsearchweb.cpp`

- `alpanelsearchweb.h`

- `alpanelstreaminfo.cpp`

- `alpanelstreaminfo.h`

- `alparceliconstrip.cpp`

- `alparceliconstrip.h`

- `alpickitem.cpp`

- `alpickitem.h`

- `alprobereach.h`

- `alrecovery.cpp`

- `alrecovery.h`

- `alrecoverykeeper.cpp`

- `alrecoverykeeper.h`

- `alregionretirement.cpp`

- `alregionretirement.h`

- `alrenderisolation.cpp`

- `alrenderisolation.h`

- `alrendersizeoverride.cpp`

- `alrendersizeoverride.h`

- `alsceneexplorermodel.cpp`

- `alsceneexplorermodel.h`

- `alsceneexplorerpredicate.cpp`

- `alsceneexplorerpredicate.h`

- `alscopedata.cpp`

- `alscopedata.h`

- `alscriptanalysis.cpp`

- `alscriptanalysis.h`

- `alscriptanalysislane.cpp`

- `alscriptanalysislane.h`

- `alscriptanalyzers.cpp`

- `alscriptanalyzers.h`

- `alscriptcontentsindex.cpp`

- `alscriptcontentsindex.h`

- `alscriptcrumbsbar.cpp`

- `alscriptcrumbsbar.h`

- `alscriptdiskmasters.cpp`

- `alscriptdiskmasters.h`

- `alscriptexplorermodel.cpp`

- `alscriptexplorermodel.h`

- `alscriptexplorerpane.cpp`

- `alscriptexplorerpane.h`

- `alscriptexplorertree.cpp`

- `alscriptexplorertree.h`

- `alscriptexternaleditor.cpp`

- `alscriptexternaleditor.h`

- `alscriptincluderesolver.cpp`

- `alscriptincluderesolver.h`

- `alscriptinspectorpane.cpp`

- `alscriptinspectorpane.h`

- `alscriptinventoryindex.cpp`

- `alscriptinventoryindex.h`

- `alscriptitemdrop.cpp`

- `alscriptitemdrop.h`

- `alscriptjobqueue.h`

- `alscriptkeymap.cpp`

- `alscriptkeymap.h`

- `alscriptkeypresets.cpp`

- `alscriptkeypresets.h`

- `alscriptlinkbadges.cpp`

- `alscriptlinkbadges.h`

- `alscriptlinkpane.cpp`

- `alscriptlinkpane.h`

- `alscriptlinkscripts.cpp`

- `alscriptlinkscripts.h`

- `alscriptlookup.cpp`

- `alscriptlookup.h`

- `alscriptmasteradopt.cpp`

- `alscriptmasteradopt.h`

- `alscriptmasterfanout.cpp`

- `alscriptmasterfanout.h`

- `alscriptmastertoasts.cpp`

- `alscriptmastertoasts.h`

- `alscriptmasterupload.cpp`

- `alscriptmasterupload.h`

- `alscriptmodules.cpp`

- `alscriptmodules.h`

- `alscriptnavigation.cpp`

- `alscriptnavigation.h`

- `alscriptnoticebar.cpp`

- `alscriptnoticebar.h`

- `alscriptobjectcheck.cpp`

- `alscriptobjectcheck.h`

- `alscriptoutlinepane.cpp`

- `alscriptoutlinepane.h`

- `alscriptoutputpane.cpp`

- `alscriptoutputpane.h`

- `alscriptpreprocessor.cpp`

- `alscriptpreprocessor.h`

- `alscriptproblemspane.cpp`

- `alscriptproblemspane.h`

- `alscriptrecompile.cpp`

- `alscriptrecompile.h`

- `alscriptreferencespane.cpp`

- `alscriptreferencespane.h`

- `alscriptregionusage.cpp`

- `alscriptregionusage.h`

- `alscriptsaveflow.cpp`

- `alscriptsaveflow.h`

- `alscriptsearch.cpp`

- `alscriptsearch.h`

- `alscriptsearchpane.cpp`

- `alscriptsearchpane.h`

- `alscriptsnippets.cpp`

- `alscriptsnippets.h`

- `alscriptstudio.h`

- `alscriptstudioaccount.cpp`

- `alscriptstudioaccount.h`

- `alscriptstudioanalysis.h`

- `alscriptstudiocaret.cpp`

- `alscriptstudiocaret.h`

- `alscriptstudiochecking.cpp`

- `alscriptstudiochecking.h`

- `alscriptstudiocommands.cpp`

- `alscriptstudiocommands.h`

- `alscriptstudiocomparepairs.cpp`

- `alscriptstudiocomparepairs.h`

- `alscriptstudiocomparewith.cpp`

- `alscriptstudiocomparewith.h`

- `alscriptstudiodiskmasters.cpp`

- `alscriptstudiodiskmasters.h`

- `alscriptstudiodoc.cpp`

- `alscriptstudiodoc.h`

- `alscriptstudioexpandedcompare.cpp`

- `alscriptstudioexpandedcompare.h`

- `alscriptstudiofileio.cpp`

- `alscriptstudiofileio.h`

- `alscriptstudiofiles.cpp`

- `alscriptstudiofiles.h`

- `alscriptstudioglue.cpp`

- `alscriptstudioglue.h`

- `alscriptstudiohistory.cpp`

- `alscriptstudiohistory.h`

- `alscriptstudiomasters.cpp`

- `alscriptstudiomasters.h`

- `alscriptstudiomerging.cpp`

- `alscriptstudiomerging.h`

- `alscriptstudioorphans.cpp`

- `alscriptstudioorphans.h`

- `alscriptstudiopane.h`

- `alscriptstudioplaces.cpp`

- `alscriptstudioplaces.h`

- `alscriptstudiorecovery.cpp`

- `alscriptstudiorecovery.h`

- `alscriptstudiosaves.h`

- `alscriptstudiosaving.cpp`

- `alscriptstudiosaving.h`

- `alscriptstudioselections.cpp`

- `alscriptstudioselections.h`

- `alscriptstudioservices.h`

- `alscriptstudiosnippetnotecard.cpp`

- `alscriptstudiosnippetnotecard.h`

- `alscriptstudiotabs.h`

- `alscriptstudioviewer.cpp`

- `alscriptstudioviewer.h`

- `alscriptstudiovim.cpp`

- `alscriptstudiovim.h`

- `alscriptstudiovimrc.cpp`

- `alscriptstudiovimrc.h`

- `alscriptstudioweighing.cpp`

- `alscriptstudioweighing.h`

- `alscriptstudiowords.cpp`

- `alscriptstudiowords.h`

- `alscripttheme.cpp`

- `alscripttheme.h`

- `alscripttypes.cpp`

- `alscripttypes.h`

- `alscriptweightspane.cpp`

- `alscriptweightspane.h`

- `alscriptworkspace.cpp`

- `alscriptworkspace.h`

- `alselectionoutline.cpp`

- `alselectionoutline.h`

- `alsky.cpp`

- `alsky.h`

- `alsnapshotcutout.cpp`

- `alsnapshotcutout.h`

- `alstreaminfo.cpp`

- `alstreaminfo.h`

- `alteleportprogress.h`

- `alterrainsurfacemaps.cpp`

- `alterrainsurfacemaps.h`

- `altextureboost.cpp`

- `altextureboost.h`

- `altexturetable.h`

- `altoolalign.cpp`

- `altoolalign.h`

- `altoolscenepicker.cpp`

- `altoolscenepicker.h`

- `alunzip.cpp`

- `alunzip.h`

- `alviewcapture.cpp`

- `alviewcapture.h`

- `alviewermenu.cpp`

- `alviewermenu.h`

- `alwatersurface.cpp`

- `alwatersurface.h`

- `alwhitebalancesolver.cpp`

- `alwhitebalancesolver.h`

- `ao.cpp`

- `ao.h`

- `aoengine.cpp`

- `aoengine.h`

- `aoset.cpp`

- `aoset.h`

- `cmake_dummy.cpp`

- `cube.dae`

- `featuretable.txt`

- `featuretable_linux.txt`

- `featuretable_mac.txt`

- `fsfloaterposer.cpp`

- `fsfloaterposer.h`

- `fsjointpose.cpp`

- `fsjointpose.h`

- `fsjointrotatetool.cpp`

- `fsjointrotatetool.h`

- `fsmaniprotatejoint.cpp`

- `fsmaniprotatejoint.h`

- `fsmaniptranslatejoint.cpp`

- `fsmaniptranslatejoint.h`

- `fspose.cpp`

- `fspose.h`

- `fsposeranimator.cpp`

- `fsposeranimator.h`

- `fsposestate.cpp`

- `fsposestate.h`

- `fsposingmotion.cpp`

- `fsposingmotion.h`

- `groupchatlistener.cpp`

- `groupchatlistener.h`

- `llaccountingcost.h`

- `llaccountingcostmanager.cpp`

- `llaccountingcostmanager.h`

- `llagent.cpp`

- `llagent.h`

- `llagentaccess.cpp`

- `llagentaccess.h`

- `llagentbenefits.cpp`

- `llagentbenefits.h`

- `llagentcamera.cpp`

- `llagentcamera.h`

- `llagentdata.cpp`

- `llagentdata.h`

- `llagenthandler.cpp`

- `llagentlanguage.cpp`

- `llagentlanguage.h`

- `llagentlistener.cpp`

- `llagentlistener.h`

- `llagentpicksinfo.cpp`

- `llagentpicksinfo.h`

- `llagentpilot.cpp`

- `llagentpilot.h`

- `llagentui.cpp`

- `llagentui.h`

- `llagentwearables.cpp`

- `llagentwearables.h`

- `llaisapi.cpp`

- `llaisapi.h`

- `llanimstatelabels.cpp`

- `llanimstatelabels.h`

- `llappcorehttp.cpp`

- `llappcorehttp.h`

- `llappearance.h`

- `llappearancelistener.cpp`

- `llappearancelistener.h`

- `llappearancemgr.cpp`

- `llappearancemgr.h`

- `llappviewer.cpp`

- `llappviewer.h`

- `llappviewerlistener.cpp`

- `llappviewerlistener.h`

- `llappviewersdl.cpp`

- `llappviewersdl.h`

- `llappviewerwin32.cpp`

- `llappviewerwin32.h`

- `llattachmentsmgr.cpp`

- `llattachmentsmgr.h`

- `llaudiosourcevo.cpp`

- `llaudiosourcevo.h`

- `llautoreplace.cpp`

- `llautoreplace.h`

- `llavataractions.cpp`

- `llavataractions.h`

- `llavatariconctrl.cpp`

- `llavatariconctrl.h`

- `llavatarlist.cpp`

- `llavatarlist.h`

- `llavatarlistitem.cpp`

- `llavatarlistitem.h`

- `llavatarpropertiesprocessor.cpp`

- `llavatarpropertiesprocessor.h`

- `llavatarrenderinfoaccountant.cpp`

- `llavatarrenderinfoaccountant.h`

- `llavatarrendernotifier.cpp`

- `llavatarrendernotifier.h`

- `llblockedlistitem.cpp`

- `llblockedlistitem.h`

- `llblocklist.cpp`

- `llblocklist.h`

- `llbox.cpp`

- `llbox.h`

- `llbrowsernotification.cpp`

- `llbuycurrencyhtml.cpp`

- `llbuycurrencyhtml.h`

- `llcallbacklist.cpp`

- `llcallingcard.cpp`

- `llcallingcard.h`

- `llcapabilityprovider.h`

- `llcefaccelinterop.cpp`

- `llcefaccelinterop.h`

- `llcefsurfacereceiver.cpp`

- `llcefsurfacereceiver.h`

- `llchannelmanager.cpp`

- `llchannelmanager.h`

- `llchatbar.cpp`

- `llchatbar.h`

- `llchathistory.cpp`

- `llchathistory.h`

- `llchatitemscontainerctrl.cpp`

- `llchatitemscontainerctrl.h`

- `llchatmsgbox.cpp`

- `llchatmsgbox.h`

- `llchatservicehistory.cpp`

- `llchatservicehistory.h`

- `llchatservicehistorycore.cpp`

- `llchatservicehistorycore.h`

- `llchiclet.cpp`

- `llchiclet.h`

- `llchicletbar.cpp`

- `llchicletbar.h`

- `llclassifiedinfo.cpp`

- `llclassifiedinfo.h`

- `llcofwearables.cpp`

- `llcofwearables.h`

- `llcolorswatch.cpp`

- `llcolorswatch.h`

- `llcommanddispatcherlistener.cpp`

- `llcommanddispatcherlistener.h`

- `llcommandhandler.cpp`

- `llcommandhandler.h`

- `llcommandlineparser.cpp`

- `llcommandlineparser.h`

- `llcommunicationchannel.cpp`

- `llcommunicationchannel.h`

- `llcompilequeue.cpp`

- `llcompilequeue.h`

- `llconfirmationmanager.cpp`

- `llconfirmationmanager.h`

- `llcontrolavatar.cpp`

- `llcontrolavatar.h`

- `llconversationlog.cpp`

- `llconversationlog.h`

- `llconversationloglist.cpp`

- `llconversationloglist.h`

- `llconversationloglistitem.cpp`

- `llconversationloglistitem.h`

- `llconversationmodel.cpp`

- `llconversationmodel.h`

- `llconversationview.cpp`

- `llconversationview.h`

- `llcurrencyuimanager.cpp`

- `llcurrencyuimanager.h`

- `llcylinder.cpp`

- `llcylinder.h`

- `lldateutil.cpp`

- `lldateutil.h`

- `lldebugmessagebox.cpp`

- `lldebugmessagebox.h`

- `lldebugview.cpp`

- `lldebugview.h`

- `lldeferredsounds.cpp`

- `lldeferredsounds.h`

- `lldelayedgestureerror.cpp`

- `lldelayedgestureerror.h`

- `lldirpicker.cpp`

- `lldirpicker.h`

- `lldndbutton.cpp`

- `lldndbutton.h`

- `lldonotdisturbnotificationstorage.cpp`

- `lldonotdisturbnotificationstorage.h`

- `lldrawable.cpp`

- `lldrawable.h`

- `lldrawpool.cpp`

- `lldrawpool.h`

- `lldrawpoolalpha.cpp`

- `lldrawpoolalpha.h`

- `lldrawpoolavatar.cpp`

- `lldrawpoolavatar.h`

- `lldrawpoolbump.cpp`

- `lldrawpoolbump.h`

- `lldrawpoolmaterials.cpp`

- `lldrawpoolmaterials.h`

- `lldrawpoolpbropaque.cpp`

- `lldrawpoolpbropaque.h`

- `lldrawpoolsimple.cpp`

- `lldrawpoolsimple.h`

- `lldrawpoolterrain.cpp`

- `lldrawpoolterrain.h`

- `lldrawpooltree.cpp`

- `lldrawpooltree.h`

- `lldrawpoolwater.cpp`

- `lldrawpoolwater.h`

- `lldrawpoolwaterexclusion.cpp`

- `lldrawpoolwaterexclusion.h`

- `lldynamictexture.cpp`

- `lldynamictexture.h`

- `lleasymessagelogentry.cpp`

- `lleasymessagelogentry.h`

- `lleasymessagereader.cpp`

- `lleasymessagereader.h`

- `lleasymessagesender.cpp`

- `lleasymessagesender.h`

- `llemote.cpp`

- `llemote.h`

- `llenvironment.cpp`

- `llenvironment.h`

- `llestateinfomodel.cpp`

- `llestateinfomodel.h`

- `lleventnotifier.cpp`

- `lleventnotifier.h`

- `lleventpoll.cpp`

- `lleventpoll.h`

- `llexpandabletextbox.cpp`

- `llexpandabletextbox.h`

- `llexperiencelog.cpp`

- `llexperiencelog.h`

- `llexternaleditor.cpp`

- `llexternaleditor.h`

- `llface.cpp`

- `llface.h`

- `llfavoritesbar.cpp`

- `llfavoritesbar.h`

- `llfeaturemanager.cpp`

- `llfeaturemanager.h`

- `llfetchedgltfmaterial.cpp`

- `llfetchedgltfmaterial.h`

- `llfilepicker.cpp`

- `llfilepicker.h`

- `llfilepicker_mac.h`

- `llfilepicker_mac.mm`

- `llfilteredwearablelist.cpp`

- `llfilteredwearablelist.h`

- `llfirstuse.cpp`

- `llfirstuse.h`

- `llflexibleobject.cpp`

- `llflexibleobject.h`

- `llfloater360capture.cpp`

- `llfloater360capture.h`

- `llfloaterabout.cpp`

- `llfloaterabout.h`

- `llfloaterauction.cpp`

- `llfloaterauction.h`

- `llfloaterautoreplacesettings.cpp`

- `llfloaterautoreplacesettings.h`

- `llfloateravatarpicker.cpp`

- `llfloateravatarpicker.h`

- `llfloateravatarrendersettings.cpp`

- `llfloateravatarrendersettings.h`

- `llfloateravatartextures.cpp`

- `llfloateravatartextures.h`

- `llfloateravatarwelcomepack.cpp`

- `llfloateravatarwelcomepack.h`

- `llfloaterbanduration.cpp`

- `llfloaterbanduration.h`

- `llfloaterbeacons.cpp`

- `llfloaterbeacons.h`

- `llfloaterbuildoptions.cpp`

- `llfloaterbuildoptions.h`

- `llfloaterbulkpermission.cpp`

- `llfloaterbulkpermission.h`

- `llfloaterbulkupload.cpp`

- `llfloaterbulkupload.h`

- `llfloaterbump.cpp`

- `llfloaterbump.h`

- `llfloaterbuy.cpp`

- `llfloaterbuy.h`

- `llfloaterbuycontents.cpp`

- `llfloaterbuycontents.h`

- `llfloaterbuycurrency.cpp`

- `llfloaterbuycurrency.h`

- `llfloaterbuycurrencyhtml.cpp`

- `llfloaterbuycurrencyhtml.h`

- `llfloaterbuyland.cpp`

- `llfloaterbuyland.h`

- `llfloaterbvhpreview.cpp`

- `llfloaterbvhpreview.h`

- `llfloatercamera.cpp`

- `llfloatercamera.h`

- `llfloatercamerapresets.cpp`

- `llfloatercamerapresets.h`

- `llfloaterchangeitemthumbnail.cpp`

- `llfloaterchangeitemthumbnail.h`

- `llfloaterchatalerts.cpp`

- `llfloaterchatalerts.h`

- `llfloaterchatmentionpicker.cpp`

- `llfloaterchatmentionpicker.h`

- `llfloaterchatvoicevolume.cpp`

- `llfloaterchatvoicevolume.h`

- `llfloaterclassified.cpp`

- `llfloaterclassified.h`

- `llfloatercolorpicker.cpp`

- `llfloatercolorpicker.h`

- `llfloaterconversationlog.cpp`

- `llfloaterconversationlog.h`

- `llfloaterconversationpreview.cpp`

- `llfloaterconversationpreview.h`

- `llfloatercreatelandmark.cpp`

- `llfloatercreatelandmark.h`

- `llfloaterdeleteprefpreset.cpp`

- `llfloaterdeleteprefpreset.h`

- `llfloaterdestinations.cpp`

- `llfloaterdestinations.h`

- `llfloaterdirectory.cpp`

- `llfloaterdirectory.h`

- `llfloaterdisplayname.cpp`

- `llfloaterdisplayname.h`

- `llfloatereditenvironmentbase.cpp`

- `llfloatereditenvironmentbase.h`

- `llfloatereditextdaycycle.cpp`

- `llfloatereditextdaycycle.h`

- `llfloateremojipicker.cpp`

- `llfloateremojipicker.h`

- `llfloaterenvironmentadjust.cpp`

- `llfloaterenvironmentadjust.h`

- `llfloaterevent.cpp`

- `llfloaterevent.h`

- `llfloaterexperiencepicker.cpp`

- `llfloaterexperiencepicker.h`

- `llfloaterexperienceprofile.cpp`

- `llfloaterexperienceprofile.h`

- `llfloaterexperiences.cpp`

- `llfloaterexperiences.h`

- `llfloaterfixedenvironment.cpp`

- `llfloaterfixedenvironment.h`

- `llfloaterfonttest.cpp`

- `llfloaterfonttest.h`

- `llfloaterforgetuser.cpp`

- `llfloaterforgetuser.h`

- `llfloatergesture.cpp`

- `llfloatergesture.h`

- `llfloatergestureautocompletepicker.cpp`

- `llfloatergestureautocompletepicker.h`

- `llfloatergodtools.cpp`

- `llfloatergodtools.h`

- `llfloatergridstatus.cpp`

- `llfloatergridstatus.h`

- `llfloatergroupbulkban.cpp`

- `llfloatergroupbulkban.h`

- `llfloatergroupinvite.cpp`

- `llfloatergroupinvite.h`

- `llfloatergroups.cpp`

- `llfloatergroups.h`

- `llfloaterhandler.cpp`

- `llfloaterhandler.h`

- `llfloaterhelpbrowser.cpp`

- `llfloaterhelpbrowser.h`

- `llfloaterhexeditor.cpp`

- `llfloaterhexeditor.h`

- `llfloaterhoverheight.cpp`

- `llfloaterhoverheight.h`

- `llfloaterhud.cpp`

- `llfloaterhud.h`

- `llfloaterimagepreview.cpp`

- `llfloaterimagepreview.h`

- `llfloaterimcontainer.cpp`

- `llfloaterimcontainer.h`

- `llfloaterimnearbychat.cpp`

- `llfloaterimnearbychat.h`

- `llfloaterimnearbychathandler.cpp`

- `llfloaterimnearbychathandler.h`

- `llfloaterimnearbychatlistener.cpp`

- `llfloaterimnearbychatlistener.h`

- `llfloaterimsession.cpp`

- `llfloaterimsession.h`

- `llfloaterimsessiontab.cpp`

- `llfloaterimsessiontab.h`

- `llfloaterinspect.cpp`

- `llfloaterinspect.h`

- `llfloaterinventorysettings.cpp`

- `llfloaterinventorysettings.h`

- `llfloaterinventorythumbnailshelper.cpp`

- `llfloaterinventorythumbnailshelper.h`

- `llfloaterjoin.cpp`

- `llfloaterjoin.h`

- `llfloaterjoystick.cpp`

- `llfloaterjoystick.h`

- `llfloaterlagmeter.cpp`

- `llfloaterlagmeter.h`

- `llfloaterland.cpp`

- `llfloaterland.h`

- `llfloaterlandholdings.cpp`

- `llfloaterlandholdings.h`

- `llfloaterlinkreplace.cpp`

- `llfloaterlinkreplace.h`

- `llfloaterloadprefpreset.cpp`

- `llfloaterloadprefpreset.h`

- `llfloaterlocalassets.cpp`

- `llfloaterlocalassets.h`

- `llfloatermap.cpp`

- `llfloatermap.h`

- `llfloatermarketplace.cpp`

- `llfloatermarketplace.h`

- `llfloatermarketplacelistings.cpp`

- `llfloatermarketplacelistings.h`

- `llfloatermaturitydialog.cpp`

- `llfloatermaturitydialog.h`

- `llfloatermediasettings.cpp`

- `llfloatermediasettings.h`

- `llfloatermemleak.cpp`

- `llfloatermemleak.h`

- `llfloatermessagebuilder.cpp`

- `llfloatermessagebuilder.h`

- `llfloatermessagelog.cpp`

- `llfloatermessagelog.h`

- `llfloatermessagerewriter.cpp`

- `llfloatermessagerewriter.h`

- `llfloatermodelpreview.cpp`

- `llfloatermodelpreview.h`

- `llfloatermodeluploadbase.cpp`

- `llfloatermodeluploadbase.h`

- `llfloatermyenvironment.cpp`

- `llfloatermyenvironment.h`

- `llfloatermyscripts.cpp`

- `llfloatermyscripts.h`

- `llfloaternamedesc.cpp`

- `llfloaternamedesc.h`

- `llfloaternewfeaturenotification.cpp`

- `llfloaternewfeaturenotification.h`

- `llfloaternotificationstabbed.cpp`

- `llfloaternotificationstabbed.h`

- `llfloaterobjectweights.cpp`

- `llfloaterobjectweights.h`

- `llfloateropenobject.cpp`

- `llfloateropenobject.h`

- `llfloaterpathfindingcharacters.cpp`

- `llfloaterpathfindingcharacters.h`

- `llfloaterpathfindingconsole.cpp`

- `llfloaterpathfindingconsole.h`

- `llfloaterpathfindinglinksets.cpp`

- `llfloaterpathfindinglinksets.h`

- `llfloaterpathfindingobjects.cpp`

- `llfloaterpathfindingobjects.h`

- `llfloaterpay.cpp`

- `llfloaterpay.h`

- `llfloaterperformance.cpp`

- `llfloaterperformance.h`

- `llfloaterperms.cpp`

- `llfloaterperms.h`

- `llfloaterpreference.cpp`

- `llfloaterpreference.h`

- `llfloaterpreferencesgraphicsadvanced.cpp`

- `llfloaterpreferencesgraphicsadvanced.h`

- `llfloaterpreferenceviewadvanced.cpp`

- `llfloaterpreferenceviewadvanced.h`

- `llfloaterpreviewtrash.cpp`

- `llfloaterpreviewtrash.h`

- `llfloaterprofile.cpp`

- `llfloaterprofile.h`

- `llfloaterprofiletexture.cpp`

- `llfloaterprofiletexture.h`

- `llfloaterpublishclassified.cpp`

- `llfloaterpublishclassified.h`

- `llfloaterregiondebugconsole.cpp`

- `llfloaterregiondebugconsole.h`

- `llfloaterregioninfo.cpp`

- `llfloaterregioninfo.h`

- `llfloaterregionrestarting.cpp`

- `llfloaterregionrestarting.h`

- `llfloaterregionrestartschedule.cpp`

- `llfloaterregionrestartschedule.h`

- `llfloaterreporter.cpp`

- `llfloaterreporter.h`

- `llfloatersavecamerapreset.cpp`

- `llfloatersavecamerapreset.h`

- `llfloatersaveprefpreset.cpp`

- `llfloatersaveprefpreset.h`

- `llfloatersceneloadstats.cpp`

- `llfloatersceneloadstats.h`

- `llfloaterscriptdebug.cpp`

- `llfloaterscriptdebug.h`

- `llfloaterscripting.cpp`

- `llfloaterscripting.h`

- `llfloaterscriptlimits.cpp`

- `llfloaterscriptlimits.h`

- `llfloatersellland.cpp`

- `llfloatersellland.h`

- `llfloatersettingscolor.cpp`

- `llfloatersettingscolor.h`

- `llfloatersettingsdebug.cpp`

- `llfloatersettingsdebug.h`

- `llfloatersidepanelcontainer.cpp`

- `llfloatersidepanelcontainer.h`

- `llfloatersimplesnapshot.cpp`

- `llfloatersimplesnapshot.h`

- `llfloaterslapptest.cpp`

- `llfloaterslapptest.h`

- `llfloatersnapshot.cpp`

- `llfloatersnapshot.h`

- `llfloaterspellchecksettings.cpp`

- `llfloaterspellchecksettings.h`

- `llfloatertelehub.cpp`

- `llfloatertelehub.h`

- `llfloatertestinspectors.cpp`

- `llfloatertestinspectors.h`

- `llfloatertestlistview.cpp`

- `llfloatertestlistview.h`

- `llfloatertools.cpp`

- `llfloatertools.h`

- `llfloatertopobjects.cpp`

- `llfloatertopobjects.h`

- `llfloatertos.cpp`

- `llfloatertos.h`

- `llfloatertoybox.cpp`

- `llfloatertoybox.h`

- `llfloatertranslationsettings.cpp`

- `llfloatertranslationsettings.h`

- `llfloaterurlentry.cpp`

- `llfloaterurlentry.h`

- `llfloatervoicevolume.cpp`

- `llfloatervoicevolume.h`

- `llfloaterwebcontent.cpp`

- `llfloaterwebcontent.h`

- `llfloaterwebmodal.cpp`

- `llfloaterwebmodal.h`

- `llfloaterwhitelistentry.cpp`

- `llfloaterwhitelistentry.h`

- `llfloaterwindowsize.cpp`

- `llfloaterwindowsize.h`

- `llfloaterworldmap.cpp`

- `llfloaterworldmap.h`

- `llflycam.cpp`

- `llflycam.h`

- `llflyoutcombobtn.cpp`

- `llflyoutcombobtn.h`

- `llfolderviewmodelinventory.cpp`

- `llfolderviewmodelinventory.h`

- `llfollowcam.cpp`

- `llfollowcam.h`

- `llfriendcard.cpp`

- `llfriendcard.h`

- `llgesturelistener.cpp`

- `llgesturelistener.h`

- `llgesturemgr.cpp`

- `llgesturemgr.h`

- `llgiveinventory.cpp`

- `llgiveinventory.h`

- `llglsandbox.cpp`

- `llgltffolderitem.cpp`

- `llgltffolderitem.h`

- `llgltffoldermodel.cpp`

- `llgltffoldermodel.h`

- `llgltfmateriallist.cpp`

- `llgltfmateriallist.h`

- `llgltfmaterialpreviewmgr.cpp`

- `llgltfmaterialpreviewmgr.h`

- `llgroupactions.cpp`

- `llgroupactions.h`

- `llgroupiconctrl.cpp`

- `llgroupiconctrl.h`

- `llgrouplist.cpp`

- `llgrouplist.h`

- `llgroupmgr.cpp`

- `llgroupmgr.h`

- `llhasheduniqueid.cpp`

- `llhasheduniqueid.h`

- `llheroprobemanager.cpp`

- `llheroprobemanager.h`

- `llhexeditor.cpp`

- `llhexeditor.h`

- `llhints.cpp`

- `llhints.h`

- `llhttpretrypolicy.cpp`

- `llhttpretrypolicy.h`

- `llhudeffect.cpp`

- `llhudeffect.h`

- `llhudeffectblob.cpp`

- `llhudeffectblob.h`

- `llhudeffectlookat.cpp`

- `llhudeffectlookat.h`

- `llhudeffectpointat.cpp`

- `llhudeffectpointat.h`

- `llhudeffectresetskeleton.cpp`

- `llhudeffectresetskeleton.h`

- `llhudeffecttrail.cpp`

- `llhudeffecttrail.h`

- `llhudicon.cpp`

- `llhudicon.h`

- `llhudmanager.cpp`

- `llhudmanager.h`

- `llhudnametag.cpp`

- `llhudnametag.h`

- `llhudobject.cpp`

- `llhudobject.h`

- `llhudrender.cpp`

- `llhudrender.h`

- `llhudtext.cpp`

- `llhudtext.h`

- `llhudview.cpp`

- `llhudview.h`

- `llimagefiltersmanager.cpp`

- `llimagefiltersmanager.h`

- `llimhandler.cpp`

- `llimprocessing.cpp`

- `llimprocessing.h`

- `llimview.cpp`

- `llimview.h`

- `llinspect.cpp`

- `llinspect.h`

- `llinspectavatar.cpp`

- `llinspectavatar.h`

- `llinspectgroup.cpp`

- `llinspectgroup.h`

- `llinspectobject.cpp`

- `llinspectobject.h`

- `llinspectremoteobject.cpp`

- `llinspectremoteobject.h`

- `llinspecttexture.cpp`

- `llinspecttexture.h`

- `llinspecttoast.cpp`

- `llinspecttoast.h`

- `llinventoryactions.h`

- `llinventorybridge.cpp`

- `llinventorybridge.h`

- `llinventoryfilter.cpp`

- `llinventoryfilter.h`

- `llinventoryfunctions.cpp`

- `llinventoryfunctions.h`

- `llinventorygallery.cpp`

- `llinventorygallery.h`

- `llinventorygallerymenu.cpp`

- `llinventorygallerymenu.h`

- `llinventoryicon.cpp`

- `llinventoryicon.h`

- `llinventoryitemslist.cpp`

- `llinventoryitemslist.h`

- `llinventorylistener.cpp`

- `llinventorylistener.h`

- `llinventorylistitem.cpp`

- `llinventorylistitem.h`

- `llinventorymodel.cpp`

- `llinventorymodel.h`

- `llinventorymodelbackgroundfetch.cpp`

- `llinventorymodelbackgroundfetch.h`

- `llinventoryobserver.cpp`

- `llinventoryobserver.h`

- `llinventorypanel.cpp`

- `llinventorypanel.h`

- `lljoystickbutton.cpp`

- `lljoystickbutton.h`

- `llkeyconflict.cpp`

- `llkeyconflict.h`

- `lllandmarkactions.cpp`

- `lllandmarkactions.h`

- `lllandmarklist.cpp`

- `lllandmarklist.h`

- `lllegacyatmospherics.cpp`

- `lllegacyatmospherics.h`

- `lllightconstants.h`

- `lllistcontextmenu.cpp`

- `lllistcontextmenu.h`

- `lllistview.cpp`

- `lllistview.h`

- `lllivelslfile.cpp`

- `lllivelslfile.h`

- `lllocalanim.cpp`

- `lllocalanim.h`

- `lllocalassetpaths.cpp`

- `lllocalassetpaths.h`

- `lllocalbitmaps.cpp`

- `lllocalbitmaps.h`

- `lllocalgltfmaterials.cpp`

- `lllocalgltfmaterials.h`

- `lllocalmesh.cpp`

- `lllocalmesh.h`

- `lllocationhistory.cpp`

- `lllocationhistory.h`

- `lllocationinputctrl.cpp`

- `lllocationinputctrl.h`

- `lllogchat.cpp`

- `lllogchat.h`

- `llloginhandler.cpp`

- `llloginhandler.h`

- `lllogininstance.cpp`

- `lllogininstance.h`

- `llmachineid.cpp`

- `llmachineid.h`

- `llmanip.cpp`

- `llmanip.h`

- `llmaniprotate.cpp`

- `llmaniprotate.h`

- `llmanipscale.cpp`

- `llmanipscale.h`

- `llmaniptranslate.cpp`

- `llmaniptranslate.h`

- `llmarketplacefunctions.cpp`

- `llmarketplacefunctions.h`

- `llmarketplacenotifications.cpp`

- `llmarketplacenotifications.h`

- `llmaterialeditor.cpp`

- `llmaterialeditor.h`

- `llmaterialmgr.cpp`

- `llmaterialmgr.h`

- `llmediactrl.cpp`

- `llmediactrl.h`

- `llmediadataclient.cpp`

- `llmediadataclient.h`

- `llmenuoptionpathfindingrebakenavmesh.cpp`

- `llmenuoptionpathfindingrebakenavmesh.h`

- `llmeshrepository.cpp`

- `llmeshrepository.h`

- `llmimetypes.cpp`

- `llmimetypes.h`

- `llmodelpreview.cpp`

- `llmodelpreview.h`

- `llmorphview.cpp`

- `llmorphview.h`

- `llmoveview.cpp`

- `llmoveview.h`

- `llmutelist.cpp`

- `llmutelist.h`

- `llnamebox.cpp`

- `llnamebox.h`

- `llnameeditor.cpp`

- `llnameeditor.h`

- `llnamelistctrl.cpp`

- `llnamelistctrl.h`

- `llnavigationbar.cpp`

- `llnavigationbar.h`

- `llnearbyvoicemoderation.cpp`

- `llnearbyvoicemoderation.h`

- `llnetmap.cpp`

- `llnetmap.h`

- `llnotificationalerthandler.cpp`

- `llnotificationgrouphandler.cpp`

- `llnotificationhandler.h`

- `llnotificationhandlerutil.cpp`

- `llnotificationhinthandler.cpp`

- `llnotificationlistitem.cpp`

- `llnotificationlistitem.h`

- `llnotificationlistview.cpp`

- `llnotificationlistview.h`

- `llnotificationmanager.cpp`

- `llnotificationmanager.h`

- `llnotificationofferhandler.cpp`

- `llnotificationscripthandler.cpp`

- `llnotificationstorage.cpp`

- `llnotificationstorage.h`

- `llnotificationtiphandler.cpp`

- `lloutfitgallery.cpp`

- `lloutfitgallery.h`

- `lloutfitobserver.cpp`

- `lloutfitobserver.h`

- `lloutfitslist.cpp`

- `lloutfitslist.h`

- `lloutputmonitorctrl.cpp`

- `lloutputmonitorctrl.h`

- `llpanelappearancetab.cpp`

- `llpanelappearancetab.h`

- `llpanelavatar.cpp`

- `llpanelavatar.h`

- `llpanelavatartag.cpp`

- `llpanelavatartag.h`

- `llpanelblockedlist.cpp`

- `llpanelblockedlist.h`

- `llpanelclassified.cpp`

- `llpanelclassified.h`

- `llpanelcontents.cpp`

- `llpanelcontents.h`

- `llpaneldirbrowser.cpp`

- `llpaneldirbrowser.h`

- `llpaneldirclassified.cpp`

- `llpaneldirclassified.h`

- `llpaneldirevents.cpp`

- `llpaneldirevents.h`

- `llpaneldirgroups.cpp`

- `llpaneldirgroups.h`

- `llpaneldirland.cpp`

- `llpaneldirland.h`

- `llpaneldirpeople.cpp`

- `llpaneldirpeople.h`

- `llpaneldirplaces.cpp`

- `llpaneldirplaces.h`

- `llpaneldirweb.cpp`

- `llpaneldirweb.h`

- `llpaneleditsky.cpp`

- `llpaneleditsky.h`

- `llpaneleditwater.cpp`

- `llpaneleditwater.h`

- `llpaneleditwearable.cpp`

- `llpaneleditwearable.h`

- `llpanelemojicomplete.cpp`

- `llpanelemojicomplete.h`

- `llpanelenvironment.cpp`

- `llpanelenvironment.h`

- `llpaneleventinfo.cpp`

- `llpaneleventinfo.h`

- `llpanelexperiencelisteditor.cpp`

- `llpanelexperiencelisteditor.h`

- `llpanelexperiencelog.cpp`

- `llpanelexperiencelog.h`

- `llpanelexperiencepicker.cpp`

- `llpanelexperiencepicker.h`

- `llpanelexperiences.cpp`

- `llpanelexperiences.h`

- `llpanelface.cpp`

- `llpanelface.h`

- `llpanelgenerictip.cpp`

- `llpanelgenerictip.h`

- `llpanelgroup.cpp`

- `llpanelgroup.h`

- `llpanelgroupbulk.cpp`

- `llpanelgroupbulk.h`

- `llpanelgroupbulkban.cpp`

- `llpanelgroupbulkban.h`

- `llpanelgroupbulkimpl.h`

- `llpanelgroupcreate.cpp`

- `llpanelgroupcreate.h`

- `llpanelgroupexperiences.cpp`

- `llpanelgroupexperiences.h`

- `llpanelgroupgeneral.cpp`

- `llpanelgroupgeneral.h`

- `llpanelgroupinvite.cpp`

- `llpanelgroupinvite.h`

- `llpanelgrouplandmoney.cpp`

- `llpanelgrouplandmoney.h`

- `llpanelgroupnotices.cpp`

- `llpanelgroupnotices.h`

- `llpanelgrouproles.cpp`

- `llpanelgrouproles.h`

- `llpanelhome.cpp`

- `llpanelhome.h`

- `llpanelland.cpp`

- `llpanelland.h`

- `llpanellandaudio.cpp`

- `llpanellandaudio.h`

- `llpanellandmarkinfo.cpp`

- `llpanellandmarkinfo.h`

- `llpanellandmarks.cpp`

- `llpanellandmarks.h`

- `llpanellandmedia.cpp`

- `llpanellandmedia.h`

- `llpanellogin.cpp`

- `llpanellogin.h`

- `llpanelloginlistener.cpp`

- `llpanelloginlistener.h`

- `llpanelmaininventory.cpp`

- `llpanelmaininventory.h`

- `llpanelmarketplaceinbox.cpp`

- `llpanelmarketplaceinbox.h`

- `llpanelmarketplaceinboxinventory.cpp`

- `llpanelmarketplaceinboxinventory.h`

- `llpanelmediasettingsgeneral.cpp`

- `llpanelmediasettingsgeneral.h`

- `llpanelmediasettingspermissions.cpp`

- `llpanelmediasettingspermissions.h`

- `llpanelmediasettingssecurity.cpp`

- `llpanelmediasettingssecurity.h`

- `llpanelnearbymedia.cpp`

- `llpanelnearbymedia.h`

- `llpanelobject.cpp`

- `llpanelobject.h`

- `llpanelobjectinventory.cpp`

- `llpanelobjectinventory.h`

- `llpanelonlinestatus.cpp`

- `llpanelonlinestatus.h`

- `llpaneloutfitedit.cpp`

- `llpaneloutfitedit.h`

- `llpaneloutfitsinventory.cpp`

- `llpaneloutfitsinventory.h`

- `llpanelpeople.cpp`

- `llpanelpeople.h`

- `llpanelpeoplemenus.cpp`

- `llpanelpeoplemenus.h`

- `llpanelpermissions.cpp`

- `llpanelpermissions.h`

- `llpanelplaceinfo.cpp`

- `llpanelplaceinfo.h`

- `llpanelplaceprofile.cpp`

- `llpanelplaceprofile.h`

- `llpanelplaces.cpp`

- `llpanelplaces.h`

- `llpanelplacestab.cpp`

- `llpanelplacestab.h`

- `llpanelpreferencegamecontrol.cpp`

- `llpanelpreferencegamecontrol.h`

- `llpanelpresetscamerapulldown.cpp`

- `llpanelpresetscamerapulldown.h`

- `llpanelpresetspulldown.cpp`

- `llpanelpresetspulldown.h`

- `llpanelprimmediacontrols.cpp`

- `llpanelprimmediacontrols.h`

- `llpanelprofile.cpp`

- `llpanelprofile.h`

- `llpanelprofileclassifieds.cpp`

- `llpanelprofileclassifieds.h`

- `llpanelprofilepicks.cpp`

- `llpanelprofilepicks.h`

- `llpanelpulldown.cpp`

- `llpanelpulldown.h`

- `llpanelsnapshot.cpp`

- `llpanelsnapshot.h`

- `llpanelsnapshotinventory.cpp`

- `llpanelsnapshotlocal.cpp`

- `llpanelsnapshotoptions.cpp`

- `llpanelsnapshotpostcard.cpp`

- `llpanelsnapshotprofile.cpp`

- `llpanelteleporthistory.cpp`

- `llpanelteleporthistory.h`

- `llpaneltiptoast.cpp`

- `llpaneltiptoast.h`

- `llpaneltopinfobar.cpp`

- `llpaneltopinfobar.h`

- `llpanelvoicedevicesettings.cpp`

- `llpanelvoicedevicesettings.h`

- `llpanelvolume.cpp`

- `llpanelvolume.h`

- `llpanelvolumepulldown.cpp`

- `llpanelvolumepulldown.h`

- `llpanelwearing.cpp`

- `llpanelwearing.h`

- `llparcelselection.cpp`

- `llparcelselection.h`

- `llparticipantlist.cpp`

- `llparticipantlist.h`

- `llpathfindingcharacter.cpp`

- `llpathfindingcharacter.h`

- `llpathfindingcharacterlist.cpp`

- `llpathfindingcharacterlist.h`

- `llpathfindinglinkset.cpp`

- `llpathfindinglinkset.h`

- `llpathfindinglinksetlist.cpp`

- `llpathfindinglinksetlist.h`

- `llpathfindingmanager.cpp`

- `llpathfindingmanager.h`

- `llpathfindingnavmesh.cpp`

- `llpathfindingnavmesh.h`

- `llpathfindingnavmeshstatus.cpp`

- `llpathfindingnavmeshstatus.h`

- `llpathfindingnavmeshzone.cpp`

- `llpathfindingnavmeshzone.h`

- `llpathfindingobject.cpp`

- `llpathfindingobject.h`

- `llpathfindingobjectlist.cpp`

- `llpathfindingobjectlist.h`

- `llpathfindingpathtool.cpp`

- `llpathfindingpathtool.h`

- `llpbrterrainfeatures.cpp`

- `llpbrterrainfeatures.h`

- `llperfstats.cpp`

- `llperfstats.h`

- `llpersistentnotificationstorage.cpp`

- `llpersistentnotificationstorage.h`

- `llphysicsmotion.cpp`

- `llphysicsmotion.h`

- `llphysicsshapebuilderutil.cpp`

- `llphysicsshapebuilderutil.h`

- `llpipelinelistener.cpp`

- `llpipelinelistener.h`

- `llplacesfolderview.cpp`

- `llplacesfolderview.h`

- `llplacesinventorybridge.cpp`

- `llplacesinventorybridge.h`

- `llplacesinventorypanel.cpp`

- `llplacesinventorypanel.h`

- `llpopupview.cpp`

- `llpopupview.h`

- `llpostcard.cpp`

- `llpostcard.h`

- `llpresetsmanager.cpp`

- `llpresetsmanager.h`

- `llpreview.cpp`

- `llpreview.h`

- `llpreviewanim.cpp`

- `llpreviewanim.h`

- `llpreviewgesture.cpp`

- `llpreviewgesture.h`

- `llpreviewnotecard.cpp`

- `llpreviewnotecard.h`

- `llpreviewsound.cpp`

- `llpreviewsound.h`

- `llpreviewtexture.cpp`

- `llpreviewtexture.h`

- `llproductinforequest.cpp`

- `llproductinforequest.h`

- `llprofileimagectrl.cpp`

- `llprofileimagectrl.h`

- `llprofileimagepicker.cpp`

- `llprofileimagepicker.h`

- `llprogressview.cpp`

- `llprogressview.h`

- `llpublishedobjectmgr.cpp`

- `llpublishedobjectmgr.h`

- `llrecentpeople.cpp`

- `llrecentpeople.h`

- `llreflectionmap.cpp`

- `llreflectionmap.h`

- `llreflectionmapmanager.cpp`

- `llreflectionmapmanager.h`

- `llregioninfomodel.cpp`

- `llregioninfomodel.h`

- `llregionposition.cpp`

- `llregionposition.h`

- `llremoteparcelrequest.cpp`

- `llremoteparcelrequest.h`

- `llresourcedata.h`

- `llrootview.h`

- `llsaveoutfitcombobtn.cpp`

- `llsaveoutfitcombobtn.h`

- `llscenemonitor.cpp`

- `llscenemonitor.h`

- `llsceneview.cpp`

- `llsceneview.h`

- `llscreenchannel.cpp`

- `llscreenchannel.h`

- `llscripteditorws.cpp`

- `llscripteditorws.h`

- `llscriptfloater.cpp`

- `llscriptfloater.h`

- `llscriptruntimeperms.h`

- `llscrollingpanelparam.cpp`

- `llscrollingpanelparam.h`

- `llscrollingpanelparambase.cpp`

- `llscrollingpanelparambase.h`

- `llsculptidsize.cpp`

- `llsculptidsize.h`

- `llsdlfiledialog.h`

- `llsearchableui.cpp`

- `llsearchableui.h`

- `llsearchcombobox.cpp`

- `llsearchcombobox.h`

- `llsearchhistory.cpp`

- `llsearchhistory.h`

- `llsecapi.cpp`

- `llsecapi.h`

- `llsechandler_basic.cpp`

- `llsechandler_basic.h`

- `llselectmgr.cpp`

- `llselectmgr.h`

- `llsetkeybinddialog.cpp`

- `llsetkeybinddialog.h`

- `llsettingspicker.cpp`

- `llsettingspicker.h`

- `llsettingsvo.cpp`

- `llsettingsvo.h`

- `llshareavatarhandler.cpp`

- `llsidepanelappearance.cpp`

- `llsidepanelappearance.h`

- `llsidepanelinventory.cpp`

- `llsidepanelinventory.h`

- `llsidepanelinventorysubpanel.cpp`

- `llsidepanelinventorysubpanel.h`

- `llsidepaneliteminfo.cpp`

- `llsidepaneliteminfo.h`

- `llsidepaneltaskinfo.cpp`

- `llsidepaneltaskinfo.h`

- `llsidetraypanelcontainer.cpp`

- `llsidetraypanelcontainer.h`

- `llskinningutil.cpp`

- `llskinningutil.h`

- `llslurl.cpp`

- `llslurl.h`

- `llsnapshotlivepreview.cpp`

- `llsnapshotlivepreview.h`

- `llsnapshotmodel.h`

- `llspatialpartition.cpp`

- `llspatialpartition.h`

- `llspeakers.cpp`

- `llspeakers.h`

- `llspeakingindicatormanager.cpp`

- `llspeakingindicatormanager.h`

- `llsplitbutton.cpp`

- `llsplitbutton.h`

- `llsprite.cpp`

- `llsprite.h`

- `llsrv.cpp`

- `llsrv.h`

- `llstartup.cpp`

- `llstartup.h`

- `llstartuplistener.cpp`

- `llstartuplistener.h`

- `llstatslistener.cpp`

- `llstatslistener.h`

- `llstatusbar.cpp`

- `llstatusbar.h`

- `llstylemap.cpp`

- `llstylemap.h`

- `llsurface.cpp`

- `llsurface.h`

- `llsurfacepatch.cpp`

- `llsurfacepatch.h`

- `llsyntaxid.cpp`

- `llsyntaxid.h`

- `llsyswellitem.cpp`

- `llsyswellitem.h`

- `llsyswellwindow.cpp`

- `llsyswellwindow.h`

- `lltable.h`

- `llteleporthistory.cpp`

- `llteleporthistory.h`

- `llteleporthistorystorage.cpp`

- `llteleporthistorystorage.h`

- `llterrainpaintmap.cpp`

- `llterrainpaintmap.h`

- `lltexturecache.cpp`

- `lltexturecache.h`

- `lltexturectrl.cpp`

- `lltexturectrl.h`

- `lltexturefetch.cpp`

- `lltexturefetch.h`

- `lltextureinfo.cpp`

- `lltextureinfo.h`

- `lltextureinfodetails.cpp`

- `lltextureinfodetails.h`

- `lltexturestats.cpp`

- `lltexturestats.h`

- `lltextureview.cpp`

- `lltextureview.h`

- `llthumbnailctrl.cpp`

- `llthumbnailctrl.h`

- `lltinygltfhelper.cpp`

- `lltinygltfhelper.h`

- `lltoast.cpp`

- `lltoast.h`

- `lltoastalertpanel.cpp`

- `lltoastalertpanel.h`

- `lltoastgroupnotifypanel.cpp`

- `lltoastgroupnotifypanel.h`

- `lltoastimpanel.cpp`

- `lltoastimpanel.h`

- `lltoastnotifypanel.cpp`

- `lltoastnotifypanel.h`

- `lltoastpanel.cpp`

- `lltoastpanel.h`

- `lltoastscriptquestion.cpp`

- `lltoastscriptquestion.h`

- `lltoastscripttextbox.cpp`

- `lltoastscripttextbox.h`

- `lltool.cpp`

- `lltool.h`

- `lltoolbarview.cpp`

- `lltoolbarview.h`

- `lltoolbrush.cpp`

- `lltoolbrush.h`

- `lltoolcomp.cpp`

- `lltoolcomp.h`

- `lltooldraganddrop.cpp`

- `lltooldraganddrop.h`

- `lltoolface.cpp`

- `lltoolface.h`

- `lltoolfocus.cpp`

- `lltoolfocus.h`

- `lltoolgrab.cpp`

- `lltoolgrab.h`

- `lltoolgun.cpp`

- `lltoolgun.h`

- `lltoolindividual.cpp`

- `lltoolindividual.h`

- `lltoolmgr.cpp`

- `lltoolmgr.h`

- `lltoolmorph.cpp`

- `lltoolmorph.h`

- `lltoolobjpicker.cpp`

- `lltoolobjpicker.h`

- `lltoolpie.cpp`

- `lltoolpie.h`

- `lltoolpipette.cpp`

- `lltoolpipette.h`

- `lltoolplacer.cpp`

- `lltoolplacer.h`

- `lltoolselect.cpp`

- `lltoolselect.h`

- `lltoolselectland.cpp`

- `lltoolselectland.h`

- `lltoolselectrect.cpp`

- `lltoolselectrect.h`

- `lltracker.cpp`

- `lltracker.h`

- `lltrackpicker.cpp`

- `lltrackpicker.h`

- `lltransientdockablefloater.cpp`

- `lltransientdockablefloater.h`

- `lltransientfloatermgr.cpp`

- `lltransientfloatermgr.h`

- `lltranslate.cpp`

- `lltranslate.h`

- `lluiavatar.cpp`

- `lluiavatar.h`

- `lluiconstants.h`

- `lluilistener.cpp`

- `lluilistener.h`

- `lluploaddialog.cpp`

- `lluploaddialog.h`

- `lluploadfloaterobservers.h`

- `llurl.cpp`

- `llurl.h`

- `llurldispatcher.cpp`

- `llurldispatcher.h`

- `llurldispatcherlistener.cpp`

- `llurldispatcherlistener.h`

- `llurlfloaterdispatchhandler.cpp`

- `llurlfloaterdispatchhandler.h`

- `llurlhistory.cpp`

- `llurlhistory.h`

- `llurllineeditorctrl.cpp`

- `llurllineeditorctrl.h`

- `llurlwhitelist.cpp`

- `llurlwhitelist.h`

- `llvelopack.cpp`

- `llvelopack.h`

- `llversioninfo.cpp`

- `llversioninfo.h`

- `llversioninfovars.h.in`

- `llviewchildren.cpp`

- `llviewchildren.h`

- `llviewerassetstats.cpp`

- `llviewerassetstats.h`

- `llviewerassetstorage.cpp`

- `llviewerassetstorage.h`

- `llviewerassettype.cpp`

- `llviewerassettype.h`

- `llviewerassetupload.cpp`

- `llviewerassetupload.h`

- `llviewerattachmenu.cpp`

- `llviewerattachmenu.h`

- `llvieweraudio.cpp`

- `llvieweraudio.h`

- `llviewercamera.cpp`

- `llviewercamera.h`

- `llviewerchat.cpp`

- `llviewerchat.h`

- `llviewercontrol.cpp`

- `llviewercontrol.h`

- `llviewercontrollistener.cpp`

- `llviewercontrollistener.h`

- `llviewerdisplay.cpp`

- `llviewerdisplay.h`

- `llviewerdisplayname.cpp`

- `llviewerdisplayname.h`

- `llviewerfloaterreg.cpp`

- `llviewerfloaterreg.h`

- `llviewerfoldertype.cpp`

- `llviewerfoldertype.h`

- `llviewergenericmessage.cpp`

- `llviewergenericmessage.h`

- `llviewergesture.cpp`

- `llviewergesture.h`

- `llviewerhelp.cpp`

- `llviewerhelp.h`

- `llviewerhelputil.cpp`

- `llviewerhelputil.h`

- `llviewerhome.cpp`

- `llviewerhome.h`

- `llviewerinput.cpp`

- `llviewerinput.h`

- `llviewerinventory.cpp`

- `llviewerinventory.h`

- `llviewerjoint.cpp`

- `llviewerjoint.h`

- `llviewerjointattachment.cpp`

- `llviewerjointattachment.h`

- `llviewerjointmesh.cpp`

- `llviewerjointmesh.h`

- `llviewerjoystick.cpp`

- `llviewerjoystick.h`

- `llviewerlayer.cpp`

- `llviewerlayer.h`

- `llviewermedia.cpp`

- `llviewermedia.h`

- `llviewermedia_streamingaudio.cpp`

- `llviewermedia_streamingaudio.h`

- `llviewermediafocus.cpp`

- `llviewermediafocus.h`

- `llviewermediaobserver.h`

- `llviewermenu.cpp`

- `llviewermenu.h`

- `llviewermenufile.cpp`

- `llviewermenufile.h`

- `llviewermessage.cpp`

- `llviewermessage.h`

- `llviewernetwork.cpp`

- `llviewernetwork.h`

- `llviewerobject.cpp`

- `llviewerobject.h`

- `llviewerobjectlist.cpp`

- `llviewerobjectlist.h`

- `llvieweroctree.cpp`

- `llvieweroctree.h`

- `llviewerparcelaskplay.cpp`

- `llviewerparcelaskplay.h`

- `llviewerparcelmedia.cpp`

- `llviewerparcelmedia.h`

- `llviewerparcelmediaautoplay.cpp`

- `llviewerparcelmediaautoplay.h`

- `llviewerparcelmgr.cpp`

- `llviewerparcelmgr.h`

- `llviewerparceloverlay.cpp`

- `llviewerparceloverlay.h`

- `llviewerpartsim.cpp`

- `llviewerpartsim.h`

- `llviewerpartsource.cpp`

- `llviewerpartsource.h`

- `llviewerprecompiledheaders.h`

- `llviewerregion.cpp`

- `llviewerregion.h`

- `llviewershadermgr.cpp`

- `llviewershadermgr.h`

- `llviewerstats.cpp`

- `llviewerstats.h`

- `llviewerstatsrecorder.cpp`

- `llviewerstatsrecorder.h`

- `llviewertexlayer.cpp`

- `llviewertexlayer.h`

- `llviewertexteditor.cpp`

- `llviewertexteditor.h`

- `llviewertexture.cpp`

- `llviewertexture.h`

- `llviewertextureanim.cpp`

- `llviewertextureanim.h`

- `llviewertexturelist.cpp`

- `llviewertexturelist.h`

- `llviewerthrottle.cpp`

- `llviewerthrottle.h`

- `llviewerwearable.cpp`

- `llviewerwearable.h`

- `llviewerwindow.cpp`

- `llviewerwindow.h`

- `llviewerwindowlistener.cpp`

- `llviewerwindowlistener.h`

- `llvisualeffect.cpp`

- `llvisualeffect.h`

- `llvlcomposition.cpp`

- `llvlcomposition.h`

- `llvlmanager.cpp`

- `llvlmanager.h`

- `llvoavatar.cpp`

- `llvoavatar.h`

- `llvoavatarself.cpp`

- `llvoavatarself.h`

- `llvocache.cpp`

- `llvocache.h`

- `llvograss.cpp`

- `llvograss.h`

- `llvoicecallhandler.cpp`

- `llvoicechannel.cpp`

- `llvoicechannel.h`

- `llvoiceclient.cpp`

- `llvoiceclient.h`

- `llvoicevisualizer.cpp`

- `llvoicevisualizer.h`

- `llvoicewebrtc.cpp`

- `llvoicewebrtc.h`

- `llvoinventorylistener.cpp`

- `llvoinventorylistener.h`

- `llvopartgroup.cpp`

- `llvopartgroup.h`

- `llvosurfacepatch.cpp`

- `llvosurfacepatch.h`

- `llvotree.cpp`

- `llvotree.h`

- `llvovolume.cpp`

- `llvovolume.h`

- `llvvmquery.cpp`

- `llvvmquery.h`

- `llwearableitemslist.cpp`

- `llwearableitemslist.h`

- `llwearablelist.cpp`

- `llwearablelist.h`

- `llweb.cpp`

- `llweb.h`

- `llwebprofile.cpp`

- `llwebprofile.h`

- `llwind.cpp`

- `llwind.h`

- `llwindebug.cpp`

- `llwindebug.h`

- `llwindowlistener.cpp`

- `llwindowlistener.h`

- `llwlhandlers.cpp`

- `llwlhandlers.h`

- `llworld.cpp`

- `llworld.h`

- `llworldmap.cpp`

- `llworldmap.h`

- `llworldmapmessage.cpp`

- `llworldmapmessage.h`

- `llworldmapview.cpp`

- `llworldmapview.h`

- `llworldmipmap.cpp`

- `llworldmipmap.h`

- `llxmlrpclistener.cpp`

- `llxmlrpclistener.h`

- `llxmlrpctransaction.cpp`

- `llxmlrpctransaction.h`

- `lutcube.cpp`

- `lutcube.h`

- `noise.cpp`

- `noise.h`

- `pipeline.cpp`

- `pipeline.h`

- `rlvactions.cpp`

- `rlvactions.h`

- `rlvcommon.cpp`

- `rlvcommon.h`

- `rlvdefines.h`

- `rlveffects.cpp`

- `rlveffects.h`

- `rlvenvironment.cpp`

- `rlvenvironment.h`

- `rlvextensions.cpp`

- `rlvextensions.h`

- `rlvfloaters.cpp`

- `rlvfloaters.h`

- `rlvhandler.cpp`

- `rlvhandler.h`

- `rlvhelper.cpp`

- `rlvhelper.h`

- `rlvinventory.cpp`

- `rlvinventory.h`

- `rlvlocks.cpp`

- `rlvlocks.h`

- `rlvmodifiers.h`

- `rlvui.cpp`

- `rlvui.h`

- `roles_constants.h`

- `slplugin.entitlements`

- `windows.manifest`


## indra/newview/English.lproj/ (2 files)

- `InfoPlist.strings`

- `language.txt`


## indra/newview/German.lproj/ (1 files)

- `language.txt`


## indra/newview/Japanese.lproj/ (1 files)

- `language.txt`


## indra/newview/Korean.lproj/ (1 files)

- `language.txt`


## indra/newview/app_settings/ (21 files)

- `anim.ini`

- `autoreplace.xml`

- `cmd_line.xml`

- `commands.xml`

- `emoji_groups.xml`

- `gamecontrollerdb.txt`

- `grass.xml`

- `ignorable_dialogs.xml`

- `key_bindings.xml`

- `llsd.xsd`

- `logcontrol.xml`

- `message.xml`

- `settings.xml`

- `settings_alchemy.xml`

- `settings_crash_behavior.xml`

- `settings_files.xml`

- `settings_per_account.xml`

- `settings_per_account_alchemy.xml`

- `std_bump.ini`

- `toolbars.xml`

- `trees.xml`


## indra/newview/app_settings/camera/ (3 files)

- `Front.xml`

- `Rear.xml`

- `Side.xml`


## indra/newview/app_settings/colorlut/ (27 files)

- `AESTHETICS_1.png`

- `AESTHETICS_2.png`

- `AESTHETICS_3.png`

- `AESTHETICS_4.png`

- `AESTHETICS_5.png`

- `AcidTrip.png`

- `Battleblue.png`

- `CrossCool.png`

- `CrossWarm.png`

- `Crunchy.png`

- `Dreary.png`

- `FallPainty.png`

- `Harshness.png`

- `NeutralLUT.png`

- `Nuked.png`

- `OGBoy.png`

- `OldPhoto.png`

- `PastelDreams.png`

- `PurpleHaze.png`

- `SicklyBlue.png`

- `Sinner.png`

- `Sinner2.png`

- `Tealness.png`

- `Toonland.png`

- `Warm.png`

- `dog_vision.png`

- `the_perfect_lut.png`


## indra/newview/app_settings/filters/ (11 files)

- `Autocontrast.xml`

- `BlackAndWhite.xml`

- `Colors1970.xml`

- `Intense.xml`

- `LensFlare.xml`

- `Miniature.xml`

- `Newspaper.xml`

- `Sepia.xml`

- `Spotlight.xml`

- `Toycamera.xml`

- `Video.xml`


## indra/newview/app_settings/looks/ (3 files)

- `Golden%20Hour.xml`

- `Neutral.xml`

- `Soft%20Film.xml`


## indra/newview/app_settings/poses/hand_presets/ (9 files)

- `Flat.xml`

- `Grip.xml`

- `Horns.xml`

- `Okay.xml`

- `Pointing.xml`

- `Relaxed.xml`

- `Thumbs_Up.xml`

- `Tight_Grip.xml`

- `Two_Finger_Salute.xml`


## indra/newview/app_settings/script_templates/ (2 files)

- `lsl.xml`

- `slua.xml`


## indra/newview/app_settings/script_themes/ (15 files)

- `alchemy_dark.xml`

- `alchemy_light.xml`

- `dracula.xml`

- `github_dark.xml`

- `github_light.xml`

- `gruvbox_dark.xml`

- `gruvbox_light.xml`

- `high_contrast_dark.xml`

- `high_contrast_light.xml`

- `monokai.xml`

- `nord.xml`

- `one_dark_pro.xml`

- `solarized_dark.xml`

- `solarized_light.xml`

- `tomorrow_night.xml`


## indra/newview/app_settings/shaders/class1/alchemy/ (5 files)

- `blitWithEffectsF.glsl`

- `colorCorrectF.glsl`

- `colorGradeUtilF.glsl`

- `lensFlareStateF.glsl`

- `postEffectUtilsF.glsl`


## indra/newview/app_settings/shaders/class1/avatar/ (4 files)

- `avatarF.glsl`

- `avatarSkinV.glsl`

- `avatarV.glsl`

- `objectSkinV.glsl`


## indra/newview/app_settings/shaders/class1/deferred/ (122 files)

- `CASF.glsl`

- `SMAA.glsl`

- `SMAABlendWeightsF.glsl`

- `SMAABlendWeightsV.glsl`

- `SMAAEdgeDetectF.glsl`

- `SMAAEdgeDetectV.glsl`

- `SMAANeighborhoodBlendF.glsl`

- `SMAANeighborhoodBlendV.glsl`

- `alphaV.glsl`

- `aoUtil.glsl`

- `avatarAlphaMaskShadowF.glsl`

- `avatarAlphaShadowF.glsl`

- `avatarAlphaShadowV.glsl`

- `avatarF.glsl`

- `avatarShadowF.glsl`

- `avatarShadowV.glsl`

- `avatarV.glsl`

- `blurLightC.glsl`

- `blurLightF.glsl`

- `blurLightUtil.glsl`

- `blurLightV.glsl`

- `bumpF.glsl`

- `bumpV.glsl`

- `deferredBlock.glsl`

- `deferredUtil.glsl`

- `depthPyramidC.glsl`

- `depthPyramidUtil.glsl`

- `diffuseAlphaMaskF.glsl`

- `diffuseAlphaMaskIndexedF.glsl`

- `diffuseAlphaMaskNoColorF.glsl`

- `diffuseIndexedF.glsl`

- `diffuseNoColorV.glsl`

- `diffuseV.glsl`

- `dofCoFUtilF.glsl`

- `dofCombineF.glsl`

- `emissiveF.glsl`

- `emissiveIndexedF.glsl`

- `emissiveIndexedV.glsl`

- `emissiveV.glsl`

- `environmentBlock.glsl`

- `exposureF.glsl`

- `exposureHistogramF.glsl`

- `exposureHistogramV.glsl`

- `fullbrightF.glsl`

- `fullbrightShinyV.glsl`

- `fullbrightV.glsl`

- `fxaaF.glsl`

- `gbufferUtil.glsl`

- `genbrdflutF.glsl`

- `genbrdflutV.glsl`

- `globalF.glsl`

- `hazeV.glsl`

- `hexLatticeUtil.glsl`

- `impostorF.glsl`

- `impostorV.glsl`

- `lightsBlock.glsl`

- `luminanceF.glsl`

- `materialF.glsl`

- `materialIndexedF.glsl`

- `materialIndexedV.glsl`

- `materialShadowIndexedF.glsl`

- `materialShadowIndexedV.glsl`

- `materialV.glsl`

- `matricesBlock.glsl`

- `normgenF.glsl`

- `normgenV.glsl`

- `pbrShadowAlphaBlendF.glsl`

- `pbrShadowAlphaMaskF.glsl`

- `pbrShadowAlphaMaskIndexedF.glsl`

- `pbrShadowAlphaMaskIndexedV.glsl`

- `pbrShadowAlphaMaskV.glsl`

- `pbralphaF.glsl`

- `pbralphaV.glsl`

- `pbrglowF.glsl`

- `pbrglowIndexedF.glsl`

- `pbrglowIndexedV.glsl`

- `pbrglowV.glsl`

- `pbropaqueF.glsl`

- `pbropaqueIndexedF.glsl`

- `pbropaqueIndexedV.glsl`

- `pbropaqueV.glsl`

- `pbrterrainF.glsl`

- `pbrterrainTE.glsl`

- `pbrterrainUtilF.glsl`

- `postDeferredF.glsl`

- `postDeferredNoDoFF.glsl`

- `postDeferredNoTCV.glsl`

- `postDeferredV.glsl`

- `postDeferredVisualizeBuffers.glsl`

- `reflectionProbesBlock.glsl`

- `rlvF.glsl`

- `rlvV.glsl`

- `screenSpaceReflUtil.glsl`

- `shadowAlphaMaskF.glsl`

- `shadowAlphaMaskV.glsl`

- `shadowCubeV.glsl`

- `shadowF.glsl`

- `shadowUtil.glsl`

- `shadowV.glsl`

- `skyAuroraF.glsl`

- `skyBodiesF.glsl`

- `skyCloudsF.glsl`

- `skyCompositeF.glsl`

- `skyCompositeMainF.glsl`

- `skyCompositeV.glsl`

- `skyCubeF.glsl`

- `skyMeteorsF.glsl`

- `starsF.glsl`

- `starsV.glsl`

- `terrainF.glsl`

- `terrainPatchV.glsl`

- `terrainShadowTE.glsl`

- `terrainSurface.glsl`

- `terrainTC.glsl`

- `terrainTE.glsl`

- `textureUtilV.glsl`

- `tonemapUtilF.glsl`

- `treeF.glsl`

- `treeShadowF.glsl`

- `treeShadowV.glsl`

- `treeV.glsl`

- `valueNoiseUtil.glsl`


## indra/newview/app_settings/shaders/class1/effects/ (10 files)

- `bloomCompositeF.glsl`

- `bloomDownsampleF.glsl`

- `bloomExtractF.glsl`

- `bloomUpsampleF.glsl`

- `crossFilterF.glsl`

- `glowExtractF.glsl`

- `glowExtractV.glsl`

- `glowF.glsl`

- `glowV.glsl`

- `lensDirtGenF.glsl`


## indra/newview/app_settings/shaders/class1/environment/ (13 files)

- `srgbF.glsl`

- `waterExclusionF.glsl`

- `waterExclusionV.glsl`

- `waterF.glsl`

- `waterFieldF.glsl`

- `waterFieldV.glsl`

- `waterFogF.glsl`

- `waterPatchV.glsl`

- `waterSurface.glsl`

- `waterTC.glsl`

- `waterTE.glsl`

- `waterV.glsl`

- `waterVaryingsV.glsl`


## indra/newview/app_settings/shaders/class1/interface/ (57 files)

- `alphamaskF.glsl`

- `alphamaskV.glsl`

- `benchmarkF.glsl`

- `benchmarkV.glsl`

- `clipF.glsl`

- `clipV.glsl`

- `copyF.glsl`

- `copyV.glsl`

- `debugF.glsl`

- `debugV.glsl`

- `gaussianF.glsl`

- `glowcombineF.glsl`

- `glowcombineV.glsl`

- `highlightF.glsl`

- `highlightNormV.glsl`

- `highlightSpecV.glsl`

- `highlightV.glsl`

- `irradianceGenV.glsl`

- `normaldebugF.glsl`

- `normaldebugG.glsl`

- `normaldebugV.glsl`

- `occlusionCubeV.glsl`

- `occlusionF.glsl`

- `occlusionV.glsl`

- `onetexturefilterF.glsl`

- `onetexturefilterV.glsl`

- `pathfindingF.glsl`

- `pathfindingNoNormalV.glsl`

- `pathfindingV.glsl`

- `pbrTerrainBakeF.glsl`

- `pbrTerrainBakeV.glsl`

- `radianceGenF.glsl`

- `radianceGenV.glsl`

- `reflectionmipF.glsl`

- `selectionAlphaF.glsl`

- `selectionBackdropMaskF.glsl`

- `selectionContrastF.glsl`

- `selectionGlowReachF.glsl`

- `selectionGlowRowF.glsl`

- `selectionIdF.glsl`

- `selectionIdV.glsl`

- `selectionJumpF.glsl`

- `selectionOutlineF.glsl`

- `selectionTileF.glsl`

- `selectionUtilF.glsl`

- `selectionWireframeF.glsl`

- `selectionWireframeG.glsl`

- `shPackUtilF.glsl`

- `shProjectF.glsl`

- `shProjectReduceF.glsl`

- `solidcolorF.glsl`

- `solidcolorV.glsl`

- `splattexturerectV.glsl`

- `twotexturecompareF.glsl`

- `twotexturecompareV.glsl`

- `uiF.glsl`

- `uiV.glsl`


## indra/newview/app_settings/shaders/class1/lighting/ (9 files)

- `lightAlphaMaskF.glsl`

- `lightAlphaMaskNonIndexedF.glsl`

- `lightF.glsl`

- `lightFuncSpecularV.glsl`

- `lightFuncV.glsl`

- `lightNonIndexedF.glsl`

- `lightSpecularV.glsl`

- `sumLightsSpecularV.glsl`

- `sumLightsV.glsl`


## indra/newview/app_settings/shaders/class1/objects/ (14 files)

- `bumpF.glsl`

- `bumpV.glsl`

- `impostorF.glsl`

- `impostorV.glsl`

- `indexedTextureV.glsl`

- `nonindexedTextureV.glsl`

- `previewF.glsl`

- `previewPhysicsF.glsl`

- `previewPhysicsV.glsl`

- `previewV.glsl`

- `simpleColorF.glsl`

- `simpleF.glsl`

- `simpleNoAtmosV.glsl`

- `simpleNoColorV.glsl`


## indra/newview/app_settings/shaders/class1/windlight/ (8 files)

- `atmosphericsF.glsl`

- `atmosphericsFuncs.glsl`

- `atmosphericsHelpersF.glsl`

- `atmosphericsHelpersV.glsl`

- `atmosphericsV.glsl`

- `atmosphericsVarsF.glsl`

- `atmosphericsVarsV.glsl`

- `windlightDomeF.glsl`


## indra/newview/app_settings/shaders/class2/deferred/ (7 files)

- `alphaF.glsl`

- `pbralphaF.glsl`

- `reflectionProbeF.glsl`

- `softenLightV.glsl`

- `sunLightF.glsl`

- `sunLightSSAOF.glsl`

- `sunLightV.glsl`


## indra/newview/app_settings/shaders/class2/interface/ (2 files)

- `reflectionprobeF.glsl`

- `reflectionprobeV.glsl`


## indra/newview/app_settings/shaders/class3/deferred/ (13 files)

- `fullbrightShinyF.glsl`

- `hazeF.glsl`

- `materialF.glsl`

- `multiPointLightF.glsl`

- `multiPointLightV.glsl`

- `pointLightF.glsl`

- `pointLightV.glsl`

- `reflectionProbeF.glsl`

- `screenSpaceReflUtil.glsl`

- `softenLightF.glsl`

- `spotLightF.glsl`

- `waterHazeF.glsl`

- `waterHazeV.glsl`


## indra/newview/app_settings/shaders/class3/environment/ (2 files)

- `underWaterF.glsl`

- `waterF.glsl`


## indra/newview/app_settings/shaders/class3/lighting/ (2 files)

- `lightV.glsl`

- `sumLightsSpecularV.glsl`


## indra/newview/app_settings/snippets/ (2 files)

- `lsl.xml`

- `slua.xml`


## indra/newview/app_settings/syntax/ (6 files)

- `config.xml`

- `json.xml`

- `lsl.xml`

- `slua.xml`

- `text.xml`

- `xml.xml`


## indra/newview/app_settings/windlight/skies/ (36 files)

- `A%2D12AM.xml`

- `A%2D12PM.xml`

- `A%2D3AM.xml`

- `A%2D3PM.xml`

- `A%2D6AM.xml`

- `A%2D6PM.xml`

- `A%2D9AM.xml`

- `A%2D9PM.xml`

- `Barcelona.xml`

- `Blizzard.xml`

- `Blue%20Midday.xml`

- `Coastal%20Afternoon.xml`

- `Coastal%20Sunset.xml`

- `Default.xml`

- `Desert%20Sunset.xml`

- `Fine%20Day.xml`

- `Fluffy%20Big%20Clouds.xml`

- `Foggy.xml`

- `Funky%20Funky%20Funky.xml`

- `Funky%20Funky.xml`

- `Gelatto.xml`

- `Ghost.xml`

- `Incongruent%20Truths.xml`

- `Midday%201.xml`

- `Midday%202.xml`

- `Midday%203.xml`

- `Midday%204.xml`

- `Midday.xml`

- `Midnight.xml`

- `Night.xml`

- `Pirate.xml`

- `Purple.xml`

- `Sailor%27s%20Delight.xml`

- `Sheer%20Surreality.xml`

- `Sunrise.xml`

- `Sunset.xml`


## indra/newview/app_settings/windlight/water/ (7 files)

- `Default.xml`

- `Glassy.xml`

- `Murky.xml`

- `Pond.xml`

- `SNAKE%21%21%21.xml`

- `Second%20Plague.xml`

- `Valdez.xml`


## indra/newview/character/ (96 files)

- `attentions.xml`

- `attentionsN.xml`

- `aux_base.tga`

- `avatar_eye.llm`

- `avatar_eye_1.llm`

- `avatar_eyelashes.llm`

- `avatar_hair.llm`

- `avatar_hair_1.llm`

- `avatar_hair_2.llm`

- `avatar_hair_3.llm`

- `avatar_hair_4.llm`

- `avatar_hair_5.llm`

- `avatar_head.llm`

- `avatar_head_1.llm`

- `avatar_head_2.llm`

- `avatar_head_3.llm`

- `avatar_head_4.llm`

- `avatar_lad.xml`

- `avatar_lower_body.llm`

- `avatar_lower_body_1.llm`

- `avatar_lower_body_2.llm`

- `avatar_lower_body_3.llm`

- `avatar_lower_body_4.llm`

- `avatar_skeleton.xml`

- `avatar_skirt.llm`

- `avatar_skirt_1.llm`

- `avatar_skirt_2.llm`

- `avatar_skirt_3.llm`

- `avatar_skirt_4.llm`

- `avatar_upper_body.llm`

- `avatar_upper_body_1.llm`

- `avatar_upper_body_2.llm`

- `avatar_upper_body_3.llm`

- `avatar_upper_body_4.llm`

- `blush_alpha.tga`

- `body_skingrain.tga`

- `bodyfreckles_alpha.tga`

- `bump_face_wrinkles.tga`

- `bump_head_base.tga`

- `bump_lowerbody_base.tga`

- `bump_pants_wrinkles.tga`

- `bump_shirt_wrinkles.tga`

- `bump_upperbody_base.tga`

- `checkerboard.tga`

- `eyebrows_alpha.tga`

- `eyeliner_alpha.tga`

- `eyeshadow_inner_alpha.tga`

- `eyeshadow_outer_alpha.tga`

- `eyewhite.tga`

- `facehair_chincurtains_alpha.tga`

- `facehair_moustache_alpha.tga`

- `facehair_sideburns_alpha.tga`

- `facehair_soulpatch_alpha.tga`

- `freckles_alpha.tga`

- `genepool.xml`

- `glove_length_alpha.tga`

- `gloves_fingers_alpha.tga`

- `head_alpha.tga`

- `head_color.tga`

- `head_hair.tga`

- `head_highlights_alpha.tga`

- `head_shading_alpha.tga`

- `head_skingrain.tga`

- `invisible_head.tga`

- `jacket_length_lower_alpha.tga`

- `jacket_length_upper_alpha.tga`

- `jacket_open_lower_alpha.tga`

- `jacket_open_upper_alpha.tga`

- `lipgloss_alpha.tga`

- `lips_mask.tga`

- `lipstick_alpha.tga`

- `lowerbody_color.tga`

- `lowerbody_highlights_alpha.tga`

- `lowerbody_shading_alpha.tga`

- `nailpolish_alpha.tga`

- `pants_length_alpha.tga`

- `pants_waist_alpha.tga`

- `rosyface_alpha.tga`

- `rouge_alpha.tga`

- `shirt_bottom_alpha.tga`

- `shirt_collar_alpha.tga`

- `shirt_collar_back_alpha.tga`

- `shirt_sleeve_alpha.tga`

- `shoe_height_alpha.tga`

- `skirt_length_alpha.tga`

- `skirt_slit_back_alpha.tga`

- `skirt_slit_front_alpha.tga`

- `skirt_slit_left_alpha.tga`

- `skirt_slit_right_alpha.tga`

- `underpants_trial_female.tga`

- `underpants_trial_male.tga`

- `undershirt_trial_female.tga`

- `upperbody_color.tga`

- `upperbody_highlights_alpha.tga`

- `upperbody_shading_alpha.tga`

- `upperbodyfreckles_alpha.tga`


## indra/newview/cursors_mac/ (36 files)

- `UI_CURSOR_ARROW.tif`

- `UI_CURSOR_ARROWDRAG.tif`

- `UI_CURSOR_ARROWLOCKED.tif`

- `UI_CURSOR_GRABLOCKED.tif`

- `UI_CURSOR_NO.tif`

- `UI_CURSOR_NOLOCKED.tif`

- `UI_CURSOR_PATHFINDING.tif`

- `UI_CURSOR_PATHFINDING_END.tif`

- `UI_CURSOR_PATHFINDING_END_ADD.tif`

- `UI_CURSOR_PATHFINDING_START.tif`

- `UI_CURSOR_PATHFINDING_START_ADD.tif`

- `UI_CURSOR_PIPETTE.tif`

- `UI_CURSOR_SIZEALL.tif`

- `UI_CURSOR_SIZENESW.tif`

- `UI_CURSOR_SIZENS.tif`

- `UI_CURSOR_SIZENWSE.tif`

- `UI_CURSOR_SIZEWE.tif`

- `UI_CURSOR_TOOLBUY.tif`

- `UI_CURSOR_TOOLCAMERA.tif`

- `UI_CURSOR_TOOLCREATE.tif`

- `UI_CURSOR_TOOLFOCUS.tif`

- `UI_CURSOR_TOOLGRAB.tif`

- `UI_CURSOR_TOOLLAND.tif`

- `UI_CURSOR_TOOLMEDIAOPEN.tif`

- `UI_CURSOR_TOOLOPEN.tif`

- `UI_CURSOR_TOOLPAN.tif`

- `UI_CURSOR_TOOLPAUSE.tif`

- `UI_CURSOR_TOOLPICKOBJECT3.tif`

- `UI_CURSOR_TOOLPLAY.tif`

- `UI_CURSOR_TOOLROTATE.tif`

- `UI_CURSOR_TOOLSCALE.tif`

- `UI_CURSOR_TOOLSIT.tif`

- `UI_CURSOR_TOOLTRANSLATE.tif`

- `UI_CURSOR_TOOLZOOMIN.tif`

- `UI_CURSOR_TOOLZOOMOUT.tif`

- `UI_CURSOR_WORKING.tif`


## indra/newview/da.lproj/ (1 files)

- `language.txt`


## indra/newview/es.lproj/ (1 files)

- `language.txt`


## indra/newview/fr.lproj/ (1 files)

- `language.txt`


## indra/newview/gltf/ (13 files)

- `README.md`

- `accessor.cpp`

- `accessor.h`

- `animation.cpp`

- `animation.h`

- `asset.cpp`

- `asset.h`

- `buffer_util.h`

- `common.h`

- `llgltfloader.cpp`

- `llgltfloader.h`

- `primitive.cpp`

- `primitive.h`


## indra/newview/hu.lproj/ (1 files)

- `language.txt`


## indra/newview/installers/darwin/ (1 files)

- `dmg_settings.py`


## indra/newview/it.lproj/ (1 files)

- `language.txt`


## indra/newview/linux_tools/ (6 files)

- `chrome_sandboxing_permissions_setup.sh`

- `desktop_integration.sh`

- `install.sh.in`

- `viewer.desktop.in`

- `viewer.metainfo.xml.in`

- `wrapper.sh`


## indra/newview/nl.lproj/ (1 files)

- `language.txt`


## indra/newview/pl.lproj/ (1 files)

- `language.txt`


## indra/newview/pt.lproj/ (1 files)

- `language.txt`


## indra/newview/res/ (47 files)

- `arrow.cur`

- `arrowcop.cur`

- `arrowcopmulti.cur`

- `arrowdrag.cur`

- `bitmap2.bmp`

- `circleandline.cur`

- `have_artwork_bundle.marker`

- `icon1.ico`

- `install_icon.BMP`

- `llarrow.cur`

- `llarrowdrag.cur`

- `llarrowdragmulti.cur`

- `llarrowlocked.cur`

- `llgrablocked.cur`

- `llno.cur`

- `llnolocked.cur`

- `lltoolcamera.cur`

- `lltoolcreate.cur`

- `lltoolfocus.cur`

- `lltoolgrab.cur`

- `lltoolland.cur`

- `lltoolpan.cur`

- `lltoolpathfinding.cur`

- `lltoolpathfindingpathend.cur`

- `lltoolpathfindingpathendadd.cur`

- `lltoolpathfindingpathstart.cur`

- `lltoolpathfindingpathstartadd.cur`

- `lltoolpipette.cur`

- `lltoolrotate.cur`

- `lltoolscale.cur`

- `lltooltranslate.cur`

- `lltoolzoomin.cur`

- `lltoolzoomout.cur`

- `loginbackground.bmp`

- `resource.h`

- `toolbuy.cur`

- `toolmediaopen.cur`

- `toolopen.cur`

- `toolpause.cur`

- `toolpickobject.cur`

- `toolpickobject2.cur`

- `toolpickobject3.cur`

- `toolpipette.cur`

- `toolplay.cur`

- `toolsit.cur`

- `uninstall_icon.BMP`

- `viewerRes.rc`


## indra/newview/res-sdl/ (32 files)

- `arrowcop.png`

- `arrowcopmulti.png`

- `arrowdrag.png`

- `llarrowdragmulti.png`

- `llarrowlocked.png`

- `llgrablocked.png`

- `llno.png`

- `llnolocked.png`

- `lltoolcamera.png`

- `lltoolcreate.png`

- `lltoolfocus.png`

- `lltoolgrab.png`

- `lltoolland.png`

- `lltoolpan.png`

- `lltoolpathfinding.png`

- `lltoolpathfindingpathend.png`

- `lltoolpathfindingpathendadd.png`

- `lltoolpathfindingpathstart.png`

- `lltoolpathfindingpathstartadd.png`

- `lltoolpipette.png`

- `lltoolrotate.png`

- `lltoolscale.png`

- `lltooltranslate.png`

- `lltoolzoomin.png`

- `lltoolzoomout.png`

- `toolbuy.png`

- `toolmediaopen.png`

- `toolopen.png`

- `toolpause.png`

- `toolpickobject3.png`

- `toolplay.png`

- `toolsit.png`


## indra/newview/ru.lproj/ (1 files)

- `language.txt`


## indra/newview/skins/ (1 files)

- `xui.xsd`


## indra/newview/skins/alchemy/ (3 files)

- `colors.xml`

- `manifest.json`

- `skin_settings.xml`


## indra/newview/skins/alchemy/textures/ (1 files)

- `textures.xml`


## indra/newview/skins/alchemy/textures/bottomtray/ (13 files)

- `Cam_Rotate_In.png`

- `Cam_Tracking_In.png`

- `Movement_Backward_On.png`

- `Movement_Down_On.png`

- `Movement_Forward_On.png`

- `Movement_Left_On.png`

- `Movement_Right_On.png`

- `Movement_TurnLeft_On.png`

- `Movement_TurnRight_On.png`

- `Movement_Up_On.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_On.png`


## indra/newview/skins/alchemy/textures/build/ (15 files)

- `Object_Cone_Selected.png`

- `Object_Cube_Selected.png`

- `Object_Cylinder_Selected.png`

- `Object_Grass_Selected.png`

- `Object_Hemi_Cone_Selected.png`

- `Object_Hemi_Cylinder_Selected.png`

- `Object_Hemi_Sphere_Selected.png`

- `Object_Prism_Selected.png`

- `Object_Pyramid_Selected.png`

- `Object_Ring_Selected.png`

- `Object_Sphere_Selected.png`

- `Object_Tetrahedron_Selected.png`

- `Object_Torus_Selected.png`

- `Object_Tree_Selected.png`

- `Object_Tube_Selected.png`


## indra/newview/skins/alchemy/textures/containers/ (20 files)

- `Accordion_Off.png`

- `Accordion_Selected.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Selected.png`


## indra/newview/skins/alchemy/textures/icons/ (38 files)

- `Info_Small.png`

- `Inv_FolderClosed.png`

- `Inv_FolderClosedToxic.png`

- `Inv_FolderClosed_WT.png`

- `Inv_FolderOpen.png`

- `Inv_FolderOpenToxic.png`

- `Inv_FolderOpen_WT.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderOpen.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_SysClosed.png`

- `Inv_SysOpen.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Parcel_BuildNo_Light.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_M_Light.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Light.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_VoiceNo_Light.png`

- `Pathfinding_Dirty.png`

- `Pathfinding_Disabled.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_On.png`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `see_me_online.png`

- `see_on_map.png`

- `see_them_on_map.png`

- `see_them_online.png`


## indra/newview/skins/alchemy/textures/navbar/ (8 files)

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `NavBar_BG.png`


## indra/newview/skins/alchemy/textures/toolbar_icons/ (1 files)

- `web.png`


## indra/newview/skins/alchemy/textures/widgets/ (55 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Badge_Background.png`

- `Badge_Border.png`

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Press.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Off.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `DisclosureArrow_Opened_Off.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Press.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `ProgressBar.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Press.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Vert.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Highlight.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`


## indra/newview/skins/alchemy/textures/windows/ (19 files)

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Collapse_Foreground.png`

- `Icon_Collapse_Press.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Restore_Foreground.png`

- `Icon_Undock_Foreground.png`

- `Inspector_I.png`

- `Resize_Corner.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `startup_logo.png`


## indra/newview/skins/alchemy/xui/en/ (1 files)

- `panel_toolbar_view.xml`


## indra/newview/skins/alchemy/xui/en/widgets/ (2 files)

- `chat_editor.xml`

- `line_editor.xml`


## indra/newview/skins/default/ (4 files)

- `colors.xml`

- `default_languages.xml`

- `manifest.json`

- `skin_settings.xml`


## indra/newview/skins/default/html/ (2 files)

- `btn_purplepill_bg.png`

- `unabletoconnect.png`


## indra/newview/skins/default/html/common/equirectangular/ (2 files)

- `default.html`

- `eqr_gen.html`


## indra/newview/skins/default/html/da/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/de/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/de/loading-error/ (1 files)

- `index.html`


## indra/newview/skins/default/html/en-us/help-offline/ (1 files)

- `index.html`


## indra/newview/skins/default/html/en-us/loading/ (2 files)

- `loading.html`

- `sl_logo_rotate_black.gif`


## indra/newview/skins/default/html/en-us/loading-error/ (1 files)

- `index.html`


## indra/newview/skins/default/html/es/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/es/loading-error/ (1 files)

- `index.html`


## indra/newview/skins/default/html/fr/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/fr/loading-error/ (1 files)

- `index.html`


## indra/newview/skins/default/html/hu/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/it/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/ja/help-offline/ (1 files)

- `index.html`


## indra/newview/skins/default/html/ja/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/ja/loading-error/ (1 files)

- `index.html`


## indra/newview/skins/default/html/ko/loading-error/ (1 files)

- `index.html`


## indra/newview/skins/default/html/nl/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/pl/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/pt/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/pt/loading-error/ (1 files)

- `index.html`


## indra/newview/skins/default/html/ru/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/tr/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/uk/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/zh/loading/ (1 files)

- `loading.html`


## indra/newview/skins/default/html/zh/loading-error/ (1 files)

- `index.html`


## indra/newview/skins/default/textures/ (96 files)

- `Blank.png`

- `PixieSmall.png`

- `Rounded_Rect.png`

- `SoftDotNoBack.png`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_up.tga`

- `avatar_thumb_bkgrnd.png`

- `badge_note.j2c`

- `badge_ok.j2c`

- `badge_warn.j2c`

- `button_anim_pause.tga`

- `button_anim_pause_selected.tga`

- `button_anim_play.tga`

- `button_anim_play_selected.tga`

- `checker.png`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_irradiance.png`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `flatnormal.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `green_checkmark.png`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icon_auction.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale_adult.tga`

- `icon_group.tga`

- `icon_place.tga`

- `icon_top_pick.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `locked_image_dark.png`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_below_32.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_32.tga`

- `map_event.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_ui_collapse_icon.png`

- `map_ui_expand_icon.png`

- `materials_ui_x_24.png`

- `menu_separator.png`

- `missing_asset.tga`

- `notify_caution_icon.tga`

- `pixiesmall.j2c`

- `red_x.png`

- `rounded_square.j2c`

- `script_error.j2c`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `spacer24.tga`

- `square_selection.png`

- `tabarea.tga`

- `target_arrow.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `textures.xml`

- `ticker_visualizer_grid.tga`

- `transparent.j2c`

- `transparent.tga`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/default/textures/alchemy/ (4 files)

- `alchemy_128.png`

- `alchemybeta_128.png`

- `alchemyproject_128.png`

- `alchemytest_128.png`


## indra/newview/skins/default/textures/bottomtray/ (54 files)

- `Cam_Avatar_Off.png`

- `Cam_FreeCam_Off.png`

- `Cam_Orbit_Off.png`

- `Cam_Pan_Off.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Rotate_Center.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_Center.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Dpad.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Off.png`

- `Move_Run_Off.png`

- `Move_Walk_Off.png`

- `Movement_Backward_Off.png`

- `Movement_Backward_On.png`

- `Movement_Down_Off.png`

- `Movement_Down_On.png`

- `Movement_Forward_Off.png`

- `Movement_Forward_On.png`

- `Movement_Left_Off.png`

- `Movement_Left_On.png`

- `Movement_Right_Off.png`

- `Movement_Right_On.png`

- `Movement_TurnLeft_Off.png`

- `Movement_TurnLeft_On.png`

- `Movement_TurnRight_Off.png`

- `Movement_TurnRight_On.png`

- `Movement_Up_Off.png`

- `Movement_Up_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Off.png`

- `Snapshot_Off.png`

- `Unread_Chiclet.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`


## indra/newview/skins/default/textures/build/ (35 files)

- `Object_Cone.png`

- `Object_Cone_Selected.png`

- `Object_Cube.png`

- `Object_Cube_Selected.png`

- `Object_Cylinder.png`

- `Object_Cylinder_Selected.png`

- `Object_Grass.png`

- `Object_Grass_Selected.png`

- `Object_Hemi_Cone.png`

- `Object_Hemi_Cone_Selected.png`

- `Object_Hemi_Cylinder.png`

- `Object_Hemi_Cylinder_Selected.png`

- `Object_Hemi_Sphere.png`

- `Object_Hemi_Sphere_Selected.png`

- `Object_Prism.png`

- `Object_Prism_Selected.png`

- `Object_Pyramid.png`

- `Object_Pyramid_Selected.png`

- `Object_Ring.png`

- `Object_Ring_Selected.png`

- `Object_Sphere.png`

- `Object_Sphere_Selected.png`

- `Object_Tetrahedron.png`

- `Object_Tetrahedron_Selected.png`

- `Object_Torus.png`

- `Object_Torus_Selected.png`

- `Object_Tree.png`

- `Object_Tree_Selected.png`

- `Object_Tube.png`

- `Object_Tube_Selected.png`

- `Tool_Create.png`

- `Tool_Dozer.png`

- `Tool_Face.png`

- `Tool_Grab.png`

- `Tool_Zoom.png`


## indra/newview/skins/default/textures/containers/ (36 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabLeft_Flat_Off.png`

- `TabLeft_Flat_Selected.png`

- `TabTop_First_Flat_Off.png`

- `TabTop_First_Flat_Selected.png`

- `TabTop_Last_Flat_Off.png`

- `TabTop_Last_Flat_Selected.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Flat_Off.png`

- `TabTop_Middle_Flat_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Flashing.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Selected.png`


## indra/newview/skins/default/textures/icons/ (333 files)

- `AL_Logo.png`

- `AccountLevel_Plus.png`

- `AccountLevel_Premium.png`

- `AddItem_Disabled.png`

- `AddItem_Off.png`

- `AddItem_Press.png`

- `AlignBottom_Disabled.png`

- `AlignBottom_Off.png`

- `AlignBottom_Press.png`

- `AlignCenter_Disabled.png`

- `AlignCenter_Off.png`

- `AlignCenter_Press.png`

- `AlignLeft_Disabled.png`

- `AlignLeft_Off.png`

- `AlignLeft_Press.png`

- `AlignMiddle_Disabled.png`

- `AlignMiddle_Off.png`

- `AlignMiddle_Press.png`

- `AlignRight_Disabled.png`

- `AlignRight_Off.png`

- `AlignRight_Press.png`

- `AlignTop_Disabled.png`

- `AlignTop_Off.png`

- `AlignTop_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `Audio_Off.png`

- `Audio_Press.png`

- `BackArrow_Off.png`

- `Cam_Recall.png`

- `Cam_Save.png`

- `ClipboardMenu_Disabled.png`

- `ClipboardMenu_Off.png`

- `ClipboardMenu_Press.png`

- `ClipboardSmallMenu_Disabled.png`

- `ClipboardSmallMenu_Off.png`

- `ClipboardSmallMenu_Press.png`

- `Conv_log_inbox.png`

- `Conv_toolbar_add_person.png`

- `Conv_toolbar_arrow_ne.png`

- `Conv_toolbar_arrow_sw.png`

- `Conv_toolbar_call_log.png`

- `Conv_toolbar_close.png`

- `Conv_toolbar_collapse.png`

- `Conv_toolbar_expand.png`

- `Conv_toolbar_hang_up.png`

- `Conv_toolbar_open_call.png`

- `Conv_toolbar_pay.png`

- `Conv_toolbar_plus.png`

- `Conv_toolbar_snooze.png`

- `Conv_toolbar_sort.png`

- `Conv_toolbar_teleport.png`

- `Conv_typing.png`

- `Copy.png`

- `CopyBright.png`

- `Default_Outfit_Photo.png`

- `DownArrow_Off.png`

- `Edit_Flip_X.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `Facebook.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Group_Notices.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_Attachment_Large.png`

- `Icon_Attachment_Small.png`

- `Icon_Color_Palette.png`

- `Icon_Font_Size.png`

- `Icon_For_Sale.png`

- `Icon_Notification_Condense.png`

- `Icon_Notification_Expand.png`

- `Icon_Pointer.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_Eye.png`

- `Inv_Favorite_Star_Content.png`

- `Inv_Favorite_Star_Full.png`

- `Inv_FolderClosed.png`

- `Inv_FolderClosedToxic.png`

- `Inv_FolderClosed_WT.png`

- `Inv_FolderOpen.png`

- `Inv_FolderOpenToxic.png`

- `Inv_FolderOpen_WT.png`

- `Inv_Gesture.png`

- `Inv_Gloves.png`

- `Inv_Hair.png`

- `Inv_Invalid.png`

- `Inv_Jacket.png`

- `Inv_Landmark.png`

- `Inv_Link.png`

- `Inv_LinkFolder.png`

- `Inv_LinkItem.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderOpen.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Material.png`

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Script_Luau.png`

- `Inv_Settings.png`

- `Inv_SettingsDay.png`

- `Inv_SettingsSky.png`

- `Inv_SettingsWater.png`

- `Inv_Shape.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_StockFolderClosed.png`

- `Inv_StockFolderOpen.png`

- `Inv_SysClosed.png`

- `Inv_SysOpen.png`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_Toolbar_SearchVisibility.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_Universal.png`

- `Inv_UnknownObject.png`

- `Inv_VersionFolderClosed.png`

- `Inv_VersionFolderOpen.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `MusicNote.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Press.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_Over.png`

- `OutboxPush_Press.png`

- `OutboxPush_Progress_1.png`

- `OutboxPush_Progress_2.png`

- `OutboxPush_Progress_3.png`

- `OutboxPush_Progress_4.png`

- `OutboxPush_Progress_5.png`

- `OutboxPush_Progress_6.png`

- `OutboxPush_Selected.png`

- `OutboxPush_Selected_Disabled.png`

- `OutboxPush_Selected_Over.png`

- `OutboxPush_Selected_Press.png`

- `Parcel_BuildNo_Dark.png`

- `Parcel_BuildNo_Light.png`

- `Parcel_Build_Dark.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Exp_Color.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Pathfinding_Dirty.png`

- `Pathfinding_Disabled.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Permission_Ungranted.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

- `Presets_Icon.png`

- `Presets_Icon_Graphic.png`

- `Profile_Friend_Offline.png`

- `Profile_Friend_Online.png`

- `Profile_Perm_Find_Disabled.png`

- `Profile_Perm_Find_Enabled.png`

- `Profile_Perm_Objects_Disabled.png`

- `Profile_Perm_Objects_Enabled.png`

- `Profile_Perm_Online_Disabled.png`

- `Profile_Perm_Online_Enabled.png`

- `Progress_1.png`

- `Progress_10.png`

- `Progress_11.png`

- `Progress_12.png`

- `Progress_2.png`

- `Progress_3.png`

- `Progress_4.png`

- `Progress_5.png`

- `Progress_6.png`

- `Progress_7.png`

- `Progress_8.png`

- `Progress_9.png`

- `Refresh_Off.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SidebarBottom_Disabled.png`

- `SidebarBottom_Off.png`

- `SidebarBottom_Press.png`

- `SidebarLeft_Disabled.png`

- `SidebarLeft_Off.png`

- `SidebarLeft_Press.png`

- `SidebarRight_Disabled.png`

- `SidebarRight_Off.png`

- `SidebarRight_Press.png`

- `SkipBackward_Off.png`

- `SkipForward_Off.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `Stop_Off.png`

- `Sync_Disabled.png`

- `Sync_Enabled.png`

- `Sync_Progress_1.png`

- `Sync_Progress_2.png`

- `Sync_Progress_3.png`

- `Sync_Progress_4.png`

- `Sync_Progress_5.png`

- `Sync_Progress_6.png`

- `System_Notification_Large.png`

- `System_Notification_Small.png`

- `TrashItem_Disabled.png`

- `TrashItem_Off.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UpArrow_Off.png`

- `Video_URL_Off.png`

- `VoiceMute_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `add_icon.png`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `cake_32.png`

- `check_mark.png`

- `clipboard_copy.png`

- `clipboard_cut.png`

- `clipboard_paste.png`

- `collapse_to_one_line.png`

- `copy_clipboard.png`

- `delete_icon.png`

- `edit_mine.png`

- `edit_theirs.png`

- `emoji_picker_icon.png`

- `expand_one_liner.png`

- `file_upload.png`

- `hand.png`

- `map_placeholder.png`

- `move.png`

- `move_off.png`

- `multi_folder_mode.png`

- `nearby_chat_icon.png`

- `object_icon.png`

- `paste_clipboard.png`

- `pop_up_caution.png`

- `profile_badge_beta.png`

- `profile_badge_beta_lifetime.png`

- `profile_badge_lifetime.png`

- `profile_badge_linden.png`

- `profile_badge_pplus_lifetime.png`

- `profile_badge_premium_lifetime.png`

- `profile_group_visibility_eye_off.png`

- `profile_group_visibility_eye_off_pressed.png`

- `profile_group_visibility_eye_on.png`

- `profile_group_visibility_eye_on_pressed.png`

- `remove_icon.png`

- `see_me_online.png`

- `see_on_map.png`

- `see_them_on_map.png`

- `see_them_online.png`

- `single_folder_back.png`

- `single_folder_forward.png`

- `single_folder_mode.png`

- `single_folder_up.png`

- `snapshot_icon.png`

- `texture_icon.png`

- `thumbnail_fallback_icon.png`

- `unknown_icon.png`

- `visual_pose_enabled.png`


## indra/newview/skins/default/textures/model_wizard/ (2 files)

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/default/textures/navbar/ (24 files)

- `Arrow_Left_Off.png`

- `Arrow_Right_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Press.png`

- `Home_Off.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Landmarks.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/default/textures/script_editor/ (6 files)

- `green_square.png`

- `red_square.png`

- `script_redo.png`

- `script_save.png`

- `script_undo.png`

- `yellow_square.png`


## indra/newview/skins/default/textures/studio/ (30 files)

- `Problem_Error.png`

- `Problem_Note.png`

- `Problem_Warning.png`

- `Studio_Config.png`

- `Studio_Expanded.png`

- `Studio_File.png`

- `Studio_Find.png`

- `Studio_Format.png`

- `Studio_PaneBottom.png`

- `Studio_PaneLeft.png`

- `Studio_PaneRight.png`

- `Studio_Pinned.png`

- `Studio_Prim.png`

- `Studio_Redo.png`

- `Studio_Save.png`

- `Studio_SaveAll.png`

- `Studio_Undo.png`

- `Symbol_Constant.png`

- `Symbol_Deprecated.png`

- `Symbol_Event.png`

- `Symbol_Field.png`

- `Symbol_Function.png`

- `Symbol_Keyword.png`

- `Symbol_Label.png`

- `Symbol_Module.png`

- `Symbol_Parameter.png`

- `Symbol_Snippet.png`

- `Symbol_Type.png`

- `Symbol_Variable.png`

- `Symbol_Word.png`


## indra/newview/skins/default/textures/taskpanel/ (14 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Open_Off.png`

- `TabIcon_People_Off.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Things_Off.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Selected.png`


## indra/newview/skins/default/textures/toolbar_icons/ (54 files)

- `360_capture.png`

- `appearance.png`

- `avatars.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `caret_top.png`

- `chat.png`

- `debug.png`

- `destinations.png`

- `environments.png`

- `facebook.png`

- `flickr.png`

- `gestures.png`

- `grid_status.png`

- `highlighting.png`

- `highlighting_selected.png`

- `inventory.png`

- `land.png`

- `lightbox.png`

- `local_assets.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `mktlistings.png`

- `move.png`

- `nearbyvoice.png`

- `outbox.png`

- `panic.png`

- `people.png`

- `performance.png`

- `personal_lighting.png`

- `picks.png`

- `places.png`

- `poser.png`

- `posestand.png`

- `preferences.png`

- `profile.png`

- `regiontracker.png`

- `report_abuse.png`

- `script.png`

- `script_studio.png`

- `search.png`

- `snapshot.png`

- `snapshot_disk.png`

- `speak.png`

- `speak_small.png`

- `stats.png`

- `toggle_hud.png`

- `twitter.png`

- `view.png`

- `web.png`


## indra/newview/skins/default/textures/widgets/ (157 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

- `Arrow_Small_Down.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Badge_Background.png`

- `Badge_Border.png`

- `BreadCrumbBtn_Left_Disabled.png`

- `BreadCrumbBtn_Left_Off.png`

- `BreadCrumbBtn_Left_Over.png`

- `BreadCrumbBtn_Left_Press.png`

- `BreadCrumbBtn_Middle_Disabled.png`

- `BreadCrumbBtn_Middle_Off.png`

- `BreadCrumbBtn_Middle_Over.png`

- `BreadCrumbBtn_Middle_Press.png`

- `BreadCrumbBtn_Right_Disabled.png`

- `BreadCrumbBtn_Right_Off.png`

- `BreadCrumbBtn_Right_Over.png`

- `BreadCrumbBtn_Right_Press.png`

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Press.png`

- `Checkbox_Press.png`

- `Checkbox_Slim_Off.png`

- `Checkbox_Slim_On.png`

- `ComboButton_Arrow.png`

- `ComboButton_Disabled.png`

- `ComboButton_Hover.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Selected.png`

- `ComboButton_Transparent.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `DisclosureArrow_Opened_Off.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Press.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `Marketplace_Dropzone_Background.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressBarSolid.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Login.png`

- `PushButton_Login_Over.png`

- `PushButton_Login_Pressed.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Press.png`

- `PushButton_Sign.png`

- `PushButton_Sign_Over.png`

- `PushButton_Sign_Pressed.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Press.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Vert.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Highlight.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Highlight.png`

- `TextField_Search_Off.png`

- `TextField_Transparent.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `horizontal_drag_handle.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`

- `track_control_moon_back.png`

- `track_control_moon_front.png`

- `track_control_rotate_bottom.png`

- `track_control_rotate_bottom_active.png`

- `track_control_rotate_left_side.png`

- `track_control_rotate_left_side_active.png`

- `track_control_rotate_right_side.png`

- `track_control_rotate_right_side_active.png`

- `track_control_rotate_top.png`

- `track_control_rotate_top_active.png`

- `track_control_sphere.png`

- `track_control_sun_back.png`

- `track_control_sun_front.png`

- `vertical_drag_handle.png`


## indra/newview/skins/default/textures/windows/ (50 files)

- `Dragbar.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Collapse_Foreground.png`

- `Icon_Collapse_Press.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Resize_Corner.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `add_payment_image_center.png`

- `add_payment_image_left.png`

- `add_payment_image_right.png`

- `first_login_image.jpg`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `login_sl_logo.png`

- `login_sl_logo_horizontal.png`

- `login_sl_logo_small.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/default/textures/world/ (4 files)

- `BeaconArrow.png`

- `CameraDragDot.png`

- `NoEntryLines.png`

- `NoEntryPassLines.png`


## indra/newview/skins/default/xui/da/ (253 files)

- `emoji_categories.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_auction.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_textures.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_chat_alerts.xml`

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_critical.xml`

- `floater_display_name.xml`

- `floater_event.xml`

- `floater_font_test.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_view_finder.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_openobject.xml`

- `floater_outgoing_call.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_preferences.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_price_for_listing.xml`

- `floater_publish_classified.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_report_abuse.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_debug.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_telehub.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_url_entry.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `language_settings.xml`

- `menu_add_wearable_gear.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_self.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_object_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_people_groups.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_profile_overflow.xml`

- `menu_save_outfit.xml`

- `menu_script_chiclet.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `outfit_accordion_tab.xml`

- `panel_active_object_row.xml`

- `panel_avatar_list_item.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_wearable.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_sound.xml`

- `panel_prim_media_controls.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_estate.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/default/xui/de/ (393 files)

- `emoji_categories.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_camera_presets.xml`

- `floater_chat_alerts.xml`

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_poser.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preferences_view_advanced.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_preview_trash.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_publish_classified.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_telehub.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `language_settings.xml`

- `menu_add_wearable_gear.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_gallery_outfit_tab.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_object_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_profile_overflow.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_script_chiclet.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `outfit_accordion_tab.xml`

- `panel_active_object_row.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_chat_header.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_creation_sidetray.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_instant_message.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfit_gallery.xml`

- `panel_outfit_gallery_item.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_sidetray_home_tab.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_sys_well_item.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_tools_texture.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/default/xui/de/widgets/ (1 files)

- `density_ctrl.xml`


## indra/newview/skins/default/xui/en/ (648 files)

- `accordion_drag.xml`

- `accordion_parent.xml`

- `alert_button.xml`

- `alert_check_box.xml`

- `alert_icon.xml`

- `alert_line_editor.xml`

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_flycam.xml`

- `control_table_contents_game_control.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `favorites_bar_button.xml`

- `floater_360capture.xml`

- `floater_aaa.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_al_blocked.xml`

- `floater_al_bulk_rename.xml`

- `floater_al_chatbar.xml`

- `floater_al_directory.xml`

- `floater_al_event.xml`

- `floater_al_feedback.xml`

- `floater_al_feedback_preview.xml`

- `floater_al_generic_text.xml`

- `floater_al_group_profile.xml`

- `floater_al_particle_editor.xml`

- `floater_al_profile_legacy.xml`

- `floater_al_progress_view.xml`

- `floater_al_region_tracker.xml`

- `floater_al_transaction_log.xml`

- `floater_al_web_profile.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_avatar_welcome_pack.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bulk_upload.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_camera_presets.xml`

- `floater_change_item_thumbnail.xml`

- `floater_chat_alerts.xml`

- `floater_chat_mention_picker.xml`

- `floater_choose_group.xml`

- `floater_classified.xml`

- `floater_color_picker.xml`

- `floater_combobox_ok_cancel.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_create_landmark.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_directory.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_emoji_complete.xml`

- `floater_emoji_picker.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_explore_sounds.xml`

- `floater_fbc_web.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_poser.xml`

- `floater_gesture.xml`

- `floater_gesture_autocomplete_picker.xml`

- `floater_god_tools.xml`

- `floater_grid_status.xml`

- `floater_help_browser.xml`

- `floater_hex_editor.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_join.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_legacy_sys_well.xml`

- `floater_lightbox_settings.xml`

- `floater_linkreplace.xml`

- `floater_live_material_editor.xml`

- `floater_load_pref_preset.xml`

- `floater_local_assets.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_maturity_dialog.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_message_builder.xml`

- `floater_message_log.xml`

- `floater_message_rewriter.xml`

- `floater_mfa.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_music_ticker.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_my_web_profile.xml`

- `floater_new_feature_notification.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_performance.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preferences_view_advanced.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_preview_trash.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_quick_settings.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restart_schedule.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_explorer.xml`

- `floater_scene_explorer_filters.xml`

- `floater_scene_load_stats.xml`

- `floater_scopes.xml`

- `floater_script.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_script_studio.xml`

- `floater_script_studio_prefs.xml`

- `floater_scripting_settings.xml`

- `floater_search.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_color.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_side_bar_tab.xml`

- `floater_simple_snapshot.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_task_properties.xml`

- `floater_telehub.xml`

- `floater_test_button.xml`

- `floater_test_checkbox.xml`

- `floater_test_combobox.xml`

- `floater_test_inspectors.xml`

- `floater_test_layout.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_line_editor.xml`

- `floater_test_list_view.xml`

- `floater_test_navigation_bar.xml`

- `floater_test_radiogroup.xml`

- `floater_test_slapp.xml`

- `floater_test_slider.xml`

- `floater_test_spinner.xml`

- `floater_test_text_editor.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_test_textbox.xml`

- `floater_test_toolbar.xml`

- `floater_test_widgets.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_web_modal.xml`

- `floater_web_profile.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `floater_xui_library.xml`

- `floater_xui_studio.xml`

- `fonts.xml`

- `game_control_table_camera_rows.xml`

- `game_control_table_rows.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `inspect_toast.xml`

- `inspector_info_ctrl.xml`

- `language_settings.xml`

- `main_view.xml`

- `menu_add_wearable_gear.xml`

- `menu_al_chatbar_gear.xml`

- `menu_al_profile_image.xml`

- `menu_al_profile_legacy.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_code_editor.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_copy_color_picker.xml`

- `menu_copy_paste_avatar_profile.xml`

- `menu_copy_paste_color.xml`

- `menu_copy_paste_features.xml`

- `menu_copy_paste_group_profile.xml`

- `menu_copy_paste_light.xml`

- `menu_copy_paste_object.xml`

- `menu_copy_paste_pos.xml`

- `menu_copy_paste_rot.xml`

- `menu_copy_paste_size.xml`

- `menu_copy_paste_texture.xml`

- `menu_diff_copy.xml`

- `menu_diff_ignore.xml`

- `menu_dir_people.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_avatar_gear.xml`

- `menu_inspect_object_gear.xml`

- `menu_inspect_options.xml`

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_inventory_view_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_lightbox_curve_presets.xml`

- `menu_local_mesh.xml`

- `menu_login.xml`

- `menu_lsl_font_size.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_message_log_filter.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_nearby_media.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gallery_sort.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_list_sort.xml`

- `menu_outfit_tab.xml`

- `menu_pane_list.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

- `menu_profile_overflow.xml`

- `menu_profile_self.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_scene_explorer.xml`

- `menu_scene_explorer_view.xml`

- `menu_scene_explorer_visibility.xml`

- `menu_scopes_pane.xml`

- `menu_script_chiclet.xml`

- `menu_script_studio_explorer.xml`

- `menu_script_studio_indent.xml`

- `menu_script_studio_problem.xml`

- `menu_script_studio_tab.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_text_view.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `menu_xui_studio_backdrop.xml`

- `menu_xui_studio_tree.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notification_visibility.xml`

- `notifications.xml`

- `outfit_accordion_tab.xml`

- `panel_active_object_row.xml`

- `panel_al_block_asset.xml`

- `panel_al_block_avatar_rendering.xml`

- `panel_al_block_derender.xml`

- `panel_al_block_list.xml`

- `panel_al_classified_info.xml`

- `panel_al_classifieds_list_item.xml`

- `panel_al_edit_classified.xml`

- `panel_al_edit_pick.xml`

- `panel_al_event_info.xml`

- `panel_al_pick_info.xml`

- `panel_al_pick_list_item.xml`

- `panel_al_profile_legacy_firstlife.xml`

- `panel_al_profile_legacy_group_list_item.xml`

- `panel_al_profile_legacy_groups.xml`

- `panel_al_profile_legacy_interests.xml`

- `panel_al_profile_legacy_notes.xml`

- `panel_al_profile_legacy_picks.xml`

- `panel_al_profile_legacy_secondlife.xml`

- `panel_al_profile_legacy_sidetray.xml`

- `panel_al_search_classifieds.xml`

- `panel_al_search_events.xml`

- `panel_al_search_groups.xml`

- `panel_al_search_landsales.xml`

- `panel_al_search_people.xml`

- `panel_al_search_places.xml`

- `panel_al_search_web.xml`

- `panel_ao.xml`

- `panel_ao_mini.xml`

- `panel_ao_pulldown.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_blocked_list_item.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_bottomtray_lite.xml`

- `panel_camera_preset_item.xml`

- `panel_chat_header.xml`

- `panel_chat_item.xml`

- `panel_chat_separator.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_classifieds_list_item.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dir_classified.xml`

- `panel_dir_events.xml`

- `panel_dir_groups.xml`

- `panel_dir_land.xml`

- `panel_dir_people.xml`

- `panel_dir_places.xml`

- `panel_dir_web.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_event_info.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_favorites.xml`

- `panel_generic_tip.xml`

- `panel_gltf_material.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_creation_sidetray.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_hide_beacon.xml`

- `panel_hint.xml`

- `panel_hint_image.xml`

- `panel_hud.xml`

- `panel_inbox_inventory.xml`

- `panel_instant_message.xml`

- `panel_inventory_gallery.xml`

- `panel_inventory_gallery_item.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_lightbox_lens.xml`

- `panel_lightbox_look.xml`

- `panel_lightbox_scene.xml`

- `panel_lightbox_sky.xml`

- `panel_local_asset_list.xml`

- `panel_local_spawned.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_music_ticker.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification.xml`

- `panel_notification_list_item.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfit_gallery.xml`

- `panel_outfit_gallery_item.xml`

- `panel_outfit_snapshot_inventory.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_performance_autoadjustments.xml`

- `panel_performance_complexity.xml`

- `panel_performance_huds.xml`

- `panel_performance_nearby.xml`

- `panel_performance_preferences.xml`

- `panel_pick_list_item.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_chat_autoresponse.xml`

- `panel_preferences_chat_cmd.xml`

- `panel_preferences_chat_general.xml`

- `panel_preferences_chat_rejection.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_game_control.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_interface.xml`

- `panel_preferences_move.xml`

- `panel_preferences_move_general.xml`

- `panel_preferences_move_mlook.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_quick_settings.xml`

- `panel_quick_settings_pulldown.xml`

- `panel_radar_alert_toast.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_region_terrain_texture_transform.xml`

- `panel_rlv_locks.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_script_studio_aliases.xml`

- `panel_script_studio_keys.xml`

- `panel_script_studio_link.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_terrain_elevation.xml`

- `panel_settings_terrain_transform.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_sidetray_home_tab.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_stream_info_toast.xml`

- `panel_sys_well_item.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_toast.xml`

- `panel_toolbar_view.xml`

- `panel_tools_texture.xml`

- `panel_topinfo_bar.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `rlva_strings.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`

- `xui_lint.xml`

- `xui_notes.xml`

- `xui_version.xml`


## indra/newview/skins/default/xui/en/widgets/ (102 files)

- `accordion.xml`

- `accordion_tab.xml`

- `avatar_icon.xml`

- `avatar_list_item.xml`

- `badge.xml`

- `bodyparts_list_item.xml`

- `button.xml`

- `chat_editor.xml`

- `chat_history.xml`

- `check_box.xml`

- `chiclet_offer.xml`

- `chiclet_panel.xml`

- `chiclet_script.xml`

- `choice_list.xml`

- `clothing_list_item.xml`

- `code_editor.xml`

- `color_swatch.xml`

- `combo_box.xml`

- `context_menu.xml`

- `conversation_view_participant.xml`

- `conversation_view_session.xml`

- `deletable_wearable_list_item.xml`

- `density_ctrl.xml`

- `drop_down.xml`

- `dummy_clothing_list_item.xml`

- `emoji_complete.xml`

- `expandable_text.xml`

- `filter_editor.xml`

- `flat_list_view.xml`

- `floater.xml`

- `flyout_button.xml`

- `folder_view_item.xml`

- `fs_virtual_trackpad.xml`

- `group_icon.xml`

- `hint_popup.xml`

- `icon.xml`

- `inbox_folder_view_folder.xml`

- `inbox_folder_view_item.xml`

- `inbox_inventory_panel.xml`

- `inspector.xml`

- `inventory_list_item.xml`

- `inventory_panel.xml`

- `joystick_quat.xml`

- `joystick_rotate.xml`

- `layout_stack.xml`

- `line_editor.xml`

- `list_view.xml`

- `loading_indicator.xml`

- `location_input.xml`

- `menu.xml`

- `menu_bar.xml`

- `menu_item.xml`

- `menu_item_call.xml`

- `menu_item_check.xml`

- `menu_item_separator.xml`

- `menu_item_tear_off.xml`

- `multi_slider.xml`

- `multi_slider_bar.xml`

- `name_editor.xml`

- `name_list.xml`

- `notification_list_view.xml`

- `output_monitor.xml`

- `output_view.xml`

- `pane_list.xml`

- `panel.xml`

- `panel_camera_item.xml`

- `person_tab_view.xml`

- `progress_bar.xml`

- `radio_group.xml`

- `radio_item.xml`

- `scroll_bar.xml`

- `scroll_column_header.xml`

- `scroll_container.xml`

- `scroll_list.xml`

- `scrolling_panel_list.xml`

- `search_combo_box.xml`

- `search_editor.xml`

- `sidetray_tab.xml`

- `simple_text_editor.xml`

- `slider.xml`

- `slider_bar.xml`

- `spinner.xml`

- `split_button.xml`

- `sun_moon_trackball.xml`

- `tab_container.xml`

- `talk_button.xml`

- `teleport_history_menu_item.xml`

- `text.xml`

- `text_editor.xml`

- `text_view.xml`

- `textbase.xml`

- `texture_picker.xml`

- `time.xml`

- `toggleable_menu.xml`

- `tool_tip.xml`

- `toolbar.xml`

- `ui_ctrl.xml`

- `view_border.xml`

- `wearable_outfit_list_item.xml`

- `web_browser.xml`

- `window_shade.xml`

- `xy_vector.xml`


## indra/newview/skins/default/xui/es/ (388 files)

- `emoji_categories.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_camera_presets.xml`

- `floater_chat_alerts.xml`

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preferences_view_advanced.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_preview_trash.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_publish_classified.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_telehub.xml`

- `floater_test_layout_stacks.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `language_settings.xml`

- `menu_add_wearable_gear.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_gallery_outfit_tab.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_object_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_profile_overflow.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_script_chiclet.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `outfit_accordion_tab.xml`

- `panel_active_object_row.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_chat_header.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_creation_sidetray.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_instant_message.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfit_gallery.xml`

- `panel_outfit_gallery_item.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_tools_texture.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/default/xui/es/widgets/ (1 files)

- `density_ctrl.xml`


## indra/newview/skins/default/xui/fr/ (393 files)

- `emoji_categories.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_camera_presets.xml`

- `floater_chat_alerts.xml`

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_poser.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preferences_view_advanced.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_preview_trash.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_publish_classified.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_telehub.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `language_settings.xml`

- `menu_add_wearable_gear.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_gallery_outfit_tab.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_object_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_profile_overflow.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_script_chiclet.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `outfit_accordion_tab.xml`

- `panel_active_object_row.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_chat_header.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_creation_sidetray.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_instant_message.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfit_gallery.xml`

- `panel_outfit_gallery_item.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_sidetray_home_tab.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_sys_well_item.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_tools_texture.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/default/xui/fr/widgets/ (1 files)

- `density_ctrl.xml`


## indra/newview/skins/default/xui/it/ (391 files)

- `emoji_categories.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_camera_presets.xml`

- `floater_chat_alerts.xml`

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_poser.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preferences_view_advanced.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_preview_trash.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_publish_classified.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_telehub.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `language_settings.xml`

- `menu_add_wearable_gear.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_gallery_outfit_tab.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_object_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_profile_overflow.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_script_chiclet.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `outfit_accordion_tab.xml`

- `panel_active_object_row.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_chat_header.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_creation_sidetray.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_instant_message.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfit_gallery.xml`

- `panel_outfit_gallery_item.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_tools_texture.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/default/xui/it/widgets/ (1 files)

- `density_ctrl.xml`


## indra/newview/skins/default/xui/ja/ (588 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `floater_360capture.xml`

- `floater_aaa.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_al_blocked.xml`

- `floater_al_chatbar.xml`

- `floater_al_directory.xml`

- `floater_al_event.xml`

- `floater_al_feedback.xml`

- `floater_al_feedback_preview.xml`

- `floater_al_generic_text.xml`

- `floater_al_group_profile.xml`

- `floater_al_particle_editor.xml`

- `floater_al_profile_legacy.xml`

- `floater_al_progress_view.xml`

- `floater_al_region_tracker.xml`

- `floater_al_transaction_log.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_avatar_welcome_pack.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bulk_upload.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_camera_presets.xml`

- `floater_change_item_thumbnail.xml`

- `floater_chat_alerts.xml`

- `floater_chat_mention_picker.xml`

- `floater_choose_group.xml`

- `floater_classified.xml`

- `floater_color_picker.xml`

- `floater_combobox_ok_cancel.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_create_landmark.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_directory.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_emoji_picker.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_explore_sounds.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_poser.xml`

- `floater_gesture.xml`

- `floater_gesture_autocomplete_picker.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hex_editor.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_legacy_sys_well.xml`

- `floater_lightbox_settings.xml`

- `floater_linkreplace.xml`

- `floater_live_material_editor.xml`

- `floater_load_pref_preset.xml`

- `floater_local_assets.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_maturity_dialog.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_message_builder.xml`

- `floater_message_log.xml`

- `floater_message_rewriter.xml`

- `floater_mfa.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_music_ticker.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_new_feature_notification.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_performance.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preferences_view_advanced.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_preview_trash.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_quick_settings.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restart_schedule.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_explorer.xml`

- `floater_scene_explorer_filters.xml`

- `floater_scene_load_stats.xml`

- `floater_scopes.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_script_studio.xml`

- `floater_script_studio_prefs.xml`

- `floater_scripting_settings.xml`

- `floater_search.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_color.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_simple_snapshot.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_task_properties.xml`

- `floater_telehub.xml`

- `floater_test_button.xml`

- `floater_test_checkbox.xml`

- `floater_test_combobox.xml`

- `floater_test_inspectors.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_line_editor.xml`

- `floater_test_radiogroup.xml`

- `floater_test_slapp.xml`

- `floater_test_slider.xml`

- `floater_test_spinner.xml`

- `floater_test_text_editor.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `floater_xui_library.xml`

- `floater_xui_studio.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `language_settings.xml`

- `menu_add_wearable_gear.xml`

- `menu_al_chatbar_gear.xml`

- `menu_al_profile_image.xml`

- `menu_al_profile_legacy.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_code_editor.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_copy_color_picker.xml`

- `menu_copy_paste_avatar_profile.xml`

- `menu_copy_paste_color.xml`

- `menu_copy_paste_features.xml`

- `menu_copy_paste_group_profile.xml`

- `menu_copy_paste_light.xml`

- `menu_copy_paste_object.xml`

- `menu_copy_paste_pos.xml`

- `menu_copy_paste_rot.xml`

- `menu_copy_paste_size.xml`

- `menu_copy_paste_texture.xml`

- `menu_diff_copy.xml`

- `menu_diff_ignore.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_avatar_gear.xml`

- `menu_inspect_object_gear.xml`

- `menu_inspect_options.xml`

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_inventory_view_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_lightbox_curve_presets.xml`

- `menu_local_mesh.xml`

- `menu_login.xml`

- `menu_lsl_font_size.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_message_log_filter.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_nearby_media.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gallery_sort.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_list_sort.xml`

- `menu_outfit_tab.xml`

- `menu_pane_list.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

- `menu_profile_overflow.xml`

- `menu_profile_self.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_scene_explorer.xml`

- `menu_scene_explorer_view.xml`

- `menu_scene_explorer_visibility.xml`

- `menu_scopes_pane.xml`

- `menu_script_chiclet.xml`

- `menu_script_studio_explorer.xml`

- `menu_script_studio_indent.xml`

- `menu_script_studio_problem.xml`

- `menu_script_studio_tab.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_text_view.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `menu_xui_studio_backdrop.xml`

- `menu_xui_studio_tree.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `outfit_accordion_tab.xml`

- `panel_active_object_row.xml`

- `panel_al_block_asset.xml`

- `panel_al_block_avatar_rendering.xml`

- `panel_al_block_derender.xml`

- `panel_al_block_list.xml`

- `panel_al_classified_info.xml`

- `panel_al_edit_classified.xml`

- `panel_al_edit_pick.xml`

- `panel_al_event_info.xml`

- `panel_al_pick_info.xml`

- `panel_al_profile_legacy_firstlife.xml`

- `panel_al_profile_legacy_groups.xml`

- `panel_al_profile_legacy_interests.xml`

- `panel_al_profile_legacy_notes.xml`

- `panel_al_profile_legacy_picks.xml`

- `panel_al_profile_legacy_secondlife.xml`

- `panel_al_profile_legacy_sidetray.xml`

- `panel_al_search_classifieds.xml`

- `panel_al_search_events.xml`

- `panel_al_search_groups.xml`

- `panel_al_search_landsales.xml`

- `panel_al_search_people.xml`

- `panel_al_search_places.xml`

- `panel_al_search_web.xml`

- `panel_ao.xml`

- `panel_ao_mini.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_camera_preset_item.xml`

- `panel_chat_header.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dir_classified.xml`

- `panel_dir_events.xml`

- `panel_dir_groups.xml`

- `panel_dir_land.xml`

- `panel_dir_people.xml`

- `panel_dir_places.xml`

- `panel_dir_web.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_event_info.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_gltf_material.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_creation_sidetray.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_hide_beacon.xml`

- `panel_instant_message.xml`

- `panel_inventory_gallery.xml`

- `panel_inventory_gallery_item.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_lightbox_lens.xml`

- `panel_lightbox_look.xml`

- `panel_lightbox_scene.xml`

- `panel_lightbox_sky.xml`

- `panel_local_asset_list.xml`

- `panel_local_spawned.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_music_ticker.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification.xml`

- `panel_notification_list_item.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfit_gallery.xml`

- `panel_outfit_gallery_item.xml`

- `panel_outfit_snapshot_inventory.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_performance_autoadjustments.xml`

- `panel_performance_complexity.xml`

- `panel_performance_huds.xml`

- `panel_performance_nearby.xml`

- `panel_performance_preferences.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_chat_autoresponse.xml`

- `panel_preferences_chat_cmd.xml`

- `panel_preferences_chat_general.xml`

- `panel_preferences_chat_rejection.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_interface.xml`

- `panel_preferences_move.xml`

- `panel_preferences_move_general.xml`

- `panel_preferences_move_mlook.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_quick_settings.xml`

- `panel_radar_alert_toast.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_region_terrain_texture_transform.xml`

- `panel_rlv_locks.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_script_studio_aliases.xml`

- `panel_script_studio_keys.xml`

- `panel_script_studio_link.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_terrain_elevation.xml`

- `panel_settings_terrain_transform.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_sidetray_home_tab.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_sys_well_item.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_toast.xml`

- `panel_tools_texture.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `rlva_strings.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`

- `xui_lint.xml`


## indra/newview/skins/default/xui/ja/widgets/ (14 files)

- `bodyparts_list_item.xml`

- `clothing_list_item.xml`

- `deletable_wearable_list_item.xml`

- `density_ctrl.xml`

- `dummy_clothing_list_item.xml`

- `flat_list_view.xml`

- `inventory_list_item.xml`

- `menu_item_separator.xml`

- `menu_item_tear_off.xml`

- `name_editor.xml`

- `panel_camera_item.xml`

- `sun_moon_trackball.xml`

- `wearable_outfit_list_item.xml`

- `xy_vector.xml`


## indra/newview/skins/default/xui/pl/ (410 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `floater_360capture.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_camera_presets.xml`

- `floater_chat_alerts.xml`

- `floater_choose_group.xml`

- `floater_classified.xml`

- `floater_color_picker.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_create_landmark.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_poser.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_mfa.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preferences_view_advanced.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_preview_trash.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_telehub.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `language_settings.xml`

- `menu_add_wearable_gear.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_copy_paste_color.xml`

- `menu_copy_paste_features.xml`

- `menu_copy_paste_light.xml`

- `menu_copy_paste_object.xml`

- `menu_copy_paste_pos.xml`

- `menu_copy_paste_rot.xml`

- `menu_copy_paste_size.xml`

- `menu_copy_paste_texture.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_gallery_outfit_tab.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_object_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

- `menu_profile_overflow.xml`

- `menu_profile_self.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_script_chiclet.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `panel_active_object_row.xml`

- `panel_avatar_list_item.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_camera_preset_item.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_creation_sidetray.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_hide_beacon.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notify_textbox.xml`

- `panel_outfit_edit.xml`

- `panel_outfit_gallery.xml`

- `panel_outfit_gallery_item.xml`

- `panel_outfit_snapshot_inventory.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_scrolling_param.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_sidetray_home_tab.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_tools_texture.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/default/xui/pl/widgets/ (10 files)

- `bodyparts_list_item.xml`

- `clothing_list_item.xml`

- `deletable_wearable_list_item.xml`

- `density_ctrl.xml`

- `dummy_clothing_list_item.xml`

- `flat_list_view.xml`

- `inbox_folder_view_folder.xml`

- `inbox_folder_view_item.xml`

- `name_editor.xml`

- `panel_camera_item.xml`


## indra/newview/skins/default/xui/pt/ (390 files)

- `emoji_categories.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_camera_presets.xml`

- `floater_chat_alerts.xml`

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preferences_view_advanced.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_preview_trash.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_publish_classified.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_telehub.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `language_settings.xml`

- `menu_add_wearable_gear.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_gallery_outfit_tab.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_object_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_profile_overflow.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_script_chiclet.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `outfit_accordion_tab.xml`

- `panel_active_object_row.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_chat_header.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_creation_sidetray.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_instant_message.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfit_gallery.xml`

- `panel_outfit_gallery_item.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_tools_texture.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `settings_comments.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/default/xui/pt/widgets/ (1 files)

- `density_ctrl.xml`


## indra/newview/skins/default/xui/ru/ (378 files)

- `emoji_categories.xml`

- `floater_aaa.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_chat_alerts.xml`

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_fs_poser.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_publish_classified.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_telehub.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `menu_add_wearable_gear.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_object_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_profile_overflow.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_script_chiclet.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `panel_active_object_row.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_chat_header.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_instant_message.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_tools_texture.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/default/xui/tr/ (375 files)

- `floater_aaa.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_chat_alerts.xml`

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_publish_classified.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_telehub.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `menu_add_wearable_gear.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_object_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_profile_overflow.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_script_chiclet.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `panel_active_object_row.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_chat_header.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_instant_message.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_tools_texture.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/default/xui/zh/ (378 files)

- `emoji_categories.xml`

- `floater_aaa.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_build_options.xml`

- `floater_bulk_perms.xml`

- `floater_bumps.xml`

- `floater_buy_contents.xml`

- `floater_buy_currency.xml`

- `floater_buy_currency_html.xml`

- `floater_buy_land.xml`

- `floater_buy_object.xml`

- `floater_camera.xml`

- `floater_chat_alerts.xml`

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_fixedenvironment.xml`

- `floater_font_test.xml`

- `floater_fs_poser.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_pick_track.xml`

- `floater_places.xml`

- `floater_preferences.xml`

- `floater_preferences_graphics_advanced.xml`

- `floater_preferences_proxy.xml`

- `floater_preview_animation.xml`

- `floater_preview_gesture.xml`

- `floater_preview_notecard.xml`

- `floater_preview_sound.xml`

- `floater_preview_texture.xml`

- `floater_price_for_listing.xml`

- `floater_profile.xml`

- `floater_publish_classified.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_limits.xml`

- `floater_script_queue.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_snapshot.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_telehub.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `inspect_avatar.xml`

- `inspect_group.xml`

- `inspect_object.xml`

- `inspect_remote_object.xml`

- `menu_add_wearable_gear.xml`

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_edit.xml`

- `menu_favorites.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_gesture_context.xml`

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_im_conversation.xml`

- `menu_im_session_showmodes.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_object_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_gear_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_profile_overflow.xml`

- `menu_save_outfit.xml`

- `menu_save_settings.xml`

- `menu_script_chiclet.xml`

- `menu_settings_add.xml`

- `menu_settings_gear.xml`

- `menu_slurl.xml`

- `menu_teleport_history_gear.xml`

- `menu_teleport_history_item.xml`

- `menu_teleport_history_tab.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_topinfobar.xml`

- `menu_url_agent.xml`

- `menu_url_email.xml`

- `menu_url_experience.xml`

- `menu_url_group.xml`

- `menu_url_http.xml`

- `menu_url_inventory.xml`

- `menu_url_map.xml`

- `menu_url_objectim.xml`

- `menu_url_parcel.xml`

- `menu_url_slapp.xml`

- `menu_url_slurl.xml`

- `menu_url_teleport.xml`

- `menu_viewer.xml`

- `menu_wearable_list_item.xml`

- `menu_wearing_gear.xml`

- `menu_wearing_tab.xml`

- `mime_types.xml`

- `mime_types_linux.xml`

- `mime_types_mac.xml`

- `notifications.xml`

- `panel_active_object_row.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_chat_header.xml`

- `panel_chiclet_bar.xml`

- `panel_classified_info.xml`

- `panel_clothing_list_button_bar.xml`

- `panel_clothing_list_item.xml`

- `panel_cof_wearables.xml`

- `panel_conversation_list_item.xml`

- `panel_conversation_log_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_dummy_clothing_list_item.xml`

- `panel_edit_alpha.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_physics.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_tattoo.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_universal.xml`

- `panel_edit_wearable.xml`

- `panel_experience_info.xml`

- `panel_experience_list_editor.xml`

- `panel_experience_list_item.xml`

- `panel_experience_log.xml`

- `panel_experience_search.xml`

- `panel_experiences.xml`

- `panel_group_bulk_ban.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_invite.xml`

- `panel_group_land_money.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_instant_message.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

- `panel_landmarks.xml`

- `panel_login.xml`

- `panel_main_inventory.xml`

- `panel_marketplace_listings.xml`

- `panel_marketplace_listings_inventory.xml`

- `panel_marketplace_listings_listed.xml`

- `panel_marketplace_listings_unassociated.xml`

- `panel_marketplace_listings_unlisted.xml`

- `panel_media_settings_general.xml`

- `panel_media_settings_permissions.xml`

- `panel_media_settings_security.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notify_textbox.xml`

- `panel_online_status_toast.xml`

- `panel_outfit_edit.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_terrain.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_scrolling_param.xml`

- `panel_scrolling_param_base.xml`

- `panel_settings_sky_atmos.xml`

- `panel_settings_sky_clouds.xml`

- `panel_settings_sky_density.xml`

- `panel_settings_sky_sunmoon.xml`

- `panel_settings_water.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_snapshot_inventory.xml`

- `panel_snapshot_local.xml`

- `panel_snapshot_options.xml`

- `panel_snapshot_postcard.xml`

- `panel_snapshot_profile.xml`

- `panel_sound_devices.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_tools_texture.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/gemini/ (3 files)

- `colors.xml`

- `manifest.json`

- `skin_settings.xml`


## indra/newview/skins/gemini/textures/ (3 files)

- `avatar_thumb_bkgrnd.png`

- `icon_day_cycle_12am.tga`

- `textures.xml`


## indra/newview/skins/gemini/textures/bottomtray/ (5 files)

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`


## indra/newview/skins/gemini/textures/containers/ (9 files)

- `TabTop_Left_Off.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Selected.png`

- `tabtop_Left_Press.png`

- `tabtop_Middle_Press.png`

- `tabtop_Right_Press.png`


## indra/newview/skins/gemini/textures/icons/ (35 files)

- `Inv_FolderClosed_White.png`

- `Inv_FolderOpen_White.png`

- `Inv_SysClosed.png`

- `Inv_SysOpen.png`

- `Parcel_BuildNo_Light.png`

- `Parcel_Build_Light.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Light.png`

- `Parcel_M_Light.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Light.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Light.png`

- `Pathfinding_Dirty_Light.png`

- `Pathfinding_Disabled_Light.png`

- `box_green.png`

- `box_grey.png`

- `radar_dolla.png`

- `radar_dolla_used.png`

- `radar_hasnotes.png`

- `radar_insim.png`

- `radar_interacted.png`

- `radar_sitting.png`

- `radar_typing.png`


## indra/newview/skins/gemini/textures/widgets/ (57 files)

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Press.png`

- `Checkbox_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`


## indra/newview/skins/gemini/textures/windows/ (4 files)

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`


## indra/newview/skins/gemini/textures/world/ (1 files)

- `BeaconArrow.png`


## indra/newview/skins/gemini/xui/en/ (1 files)

- `inspect_avatar.xml`


## indra/newview/skins/gemini/xui/en/widgets/ (3 files)

- `floater.xml`

- `location_input.xml`

- `tool_tip.xml`


## indra/newview/skins/heretic/ (3 files)

- `colors.xml`

- `manifest.json`

- `skin_settings.xml`


## indra/newview/skins/heretic/textures/ (12 files)

- `avatar_thumb_bkgrnd.png`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `green_checkmark.png`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icon_for_sale_adult.tga`

- `icon_group.tga`

- `materials_ui_x_24.png`

- `notify_caution_icon.tga`

- `red_x.png`

- `textures.xml`


## indra/newview/skins/heretic/textures/bottomtray/ (19 files)

- `Cam.psd`

- `Cam_Rotate_In.png`

- `Cam_Tracking_In.png`

- `Movement_Backward_On.png`

- `Movement_Down_On.png`

- `Movement_Forward_On.png`

- `Movement_Left_On.png`

- `Movement_Right_On.png`

- `Movement_TurnLeft_On.png`

- `Movement_TurnRight_On.png`

- `Movement_Up_On.png`

- `Unread_Chiclet.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`


## indra/newview/skins/heretic/textures/build/ (15 files)

- `Object_Cone_Selected.png`

- `Object_Cube_Selected.png`

- `Object_Cylinder_Selected.png`

- `Object_Grass_Selected.png`

- `Object_Hemi_Cone_Selected.png`

- `Object_Hemi_Cylinder_Selected.png`

- `Object_Hemi_Sphere_Selected.png`

- `Object_Prism_Selected.png`

- `Object_Pyramid_Selected.png`

- `Object_Ring_Selected.png`

- `Object_Sphere_Selected.png`

- `Object_Tetrahedron_Selected.png`

- `Object_Torus_Selected.png`

- `Object_Tree_Selected.png`

- `Object_Tube_Selected.png`


## indra/newview/skins/heretic/textures/containers/ (24 files)

- `Accordion_Off.png`

- `Accordion_Selected.png`

- `TabTop.psd`

- `TabTop_Left_Off.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`

- `tabtop_Middle_Press.png`

- `tabtop_Right_Press.png`


## indra/newview/skins/heretic/textures/icons/ (130 files)

- `AccountLevel_Plus.png`

- `AccountLevel_Premium.png`

- `Default_Outfit_Photo.png`

- `ForSale_Badge.png`

- `Generic_Group_Large.png`

- `Generic_Person_Large.png`

- `Icon_For_Sale.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_Eye.png`

- `Inv_FolderClosed.png`

- `Inv_FolderClosed.psd`

- `Inv_FolderClosedToxic.png`

- `Inv_FolderOpen.png`

- `Inv_FolderOpen.psd`

- `Inv_FolderOpenToxic.png`

- `Inv_Gesture.png`

- `Inv_Gloves.png`

- `Inv_Hair.png`

- `Inv_Invalid.png`

- `Inv_Jacket.png`

- `Inv_Landmark.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderOpen.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Material.png`

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Settings.png`

- `Inv_SettingsDay.png`

- `Inv_SettingsSky.png`

- `Inv_SettingsWater.png`

- `Inv_Shape.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_StockFolderClosed.png`

- `Inv_StockFolderOpen.png`

- `Inv_SysClosed.png`

- `Inv_SysOpen.png`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_Universal.png`

- `Inv_UnknownObject.png`

- `Inv_VersionFolderClosed.png`

- `Inv_VersionFolderOpen.png`

- `Lock.png`

- `Locked_Icon.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_Over.png`

- `OutboxPush_Press.png`

- `OutboxPush_Progress_1.png`

- `OutboxPush_Progress_2.png`

- `OutboxPush_Progress_3.png`

- `OutboxPush_Progress_4.png`

- `OutboxPush_Progress_5.png`

- `OutboxPush_Progress_6.png`

- `OutboxPush_Selected.png`

- `OutboxPush_Selected_Disabled.png`

- `OutboxPush_Selected_Over.png`

- `OutboxPush_Selected_Press.png`

- `Parcel_BuildNo_Light.png`

- `Parcel_Build_Light.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Light.png`

- `Parcel_M_Light.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_ScriptsNo_Light.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Light.png`

- `Pathfinding_Dirty.png`

- `Pathfinding_Dirty_Light.png`

- `Pathfinding_Disabled.png`

- `Pathfinding_Disabled_Light.png`

- `Person_Check.png`

- `Person_Star.png`

- `Profile_badge.psd`

- `SL_Logo.png`

- `YouAreHere_Badge.png`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `hand.png`

- `heretic.png`

- `profile_badge_beta.png`

- `profile_badge_beta_lifetime.png`

- `profile_badge_lifetime.png`

- `profile_badge_linden.png`

- `profile_badge_pplus_lifetime.png`

- `profile_badge_premium_lifetime.png`

- `radar_symbols.psd`

- `see_me_online.png`

- `see_on_map.png`

- `see_them_on_map.png`

- `see_them_online.png`

- `unknown_icon.png`


## indra/newview/skins/heretic/textures/model_wizard/ (2 files)

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/heretic/textures/navbar/ (11 files)

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `Row_Selection.png`


## indra/newview/skins/heretic/textures/widgets/ (81 files)

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Press.png`

- `Checkbox_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_Off.psd`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `Linden_Dollar_Alert.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `PushButton_Disabled.png`

- `PushButton_Login.png`

- `PushButton_Login_Over.png`

- `PushButton_Login_Pressed.png`

- `PushButton_Off.png`

- `PushButton_Off.psd`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `SegmentedBtn.psd`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Disabled.psd`

- `SliderThumb_Off.png`

- `SliderThumb_Off.psd`

- `SliderThumb_Press.png`

- `SliderThumb_Press.psd`

- `SliderTrack_Horiz.png`

- `SliderTrack_Horiz.psd`

- `SliderTrack_Vert.png`

- `SliderTrack_Vert.psd`

- `TextField_Active.png`

- `TextField_Active.psd`

- `TextField_Disabled.png`

- `TextField_Disabled.psd`

- `TextField_Off.png`

- `TextField_Off.psd`

- `TextField_Search_Active.png`

- `TextField_Search_Active.psd`

- `TextField_Search_Disabled.png`

- `TextField_Search_Disabled.psd`

- `TextField_Search_Highlight.png`

- `TextField_Search_Off.png`

- `TextField_Search_Off.psd`

- `Tooltip.png`

- `track_control_moon_back.png`

- `track_control_moon_front.png`

- `track_control_sphere.png`

- `track_control_sun_back.png`

- `track_control_sun_front.png`


## indra/newview/skins/heretic/textures/windows/ (23 files)

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Collapse_Foreground.png`

- `Icon_Collapse_Press.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Restore_Foreground.png`

- `Icon_Undock_Foreground.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Toast_Background.png`

- `Volume_Background.png`

- `Window_Background.png`

- `Window_Background.psd`

- `Window_Foreground.png`

- `Window_Foreground.psd`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `add_payment_image_center.png`

- `add_payment_image_left.png`

- `add_payment_image_right.png`

- `yellow_gradient.png`


## indra/newview/skins/heretic/textures/world/ (1 files)

- `BeaconArrow.png`


## indra/newview/skins/heretic/xui/en/ (7 files)

- `floater_about.xml`

- `floater_region_restarting.xml`

- `panel_chiclet_bar.xml`

- `panel_instant_message.xml`

- `panel_login.xml`

- `panel_progress.xml`

- `panel_toolbar_view.xml`


## indra/newview/skins/heretic/xui/en/widgets/ (3 files)

- `floater.xml`

- `location_input.xml`

- `tool_tip.xml`


## indra/newview/skins/heretic/xui/ja/ (1 files)

- `panel_login.xml`


## indra/newview/skins/ionic/ (3 files)

- `colors.xml`

- `manifest.json`

- `skin_settings.xml`


## indra/newview/skins/ionic/textures/ (3 files)

- `Nametag_Rect.j2c`

- `Rounded_Rect.png`

- `textures.xml`


## indra/newview/skins/ionic/textures/bottomtray/ (1 files)

- `ChatBarHandle.png`


## indra/newview/skins/ionic/textures/containers/ (27 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Selected.png`


## indra/newview/skins/ionic/textures/icons/ (50 files)

- `AccountLevel_Plus.png`

- `AccountLevel_Premium.png`

- `Default_Outfit_Photo.png`

- `Generic_Object_Small.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Info_Small.png`

- `Inv_FolderClosed.png`

- `Inv_FolderClosedToxic.png`

- `Inv_FolderOpen.png`

- `Inv_FolderOpenToxic.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderOpen.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_RLVaClosed.png`

- `Inv_RLVaOpen.png`

- `Inv_Script.png`

- `Inv_SysClosed.png`

- `Inv_SysOpen.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Parcel_BuildNo_Dark.png`

- `Parcel_BuildNo_Light.png`

- `Parcel_Build_Dark.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `die.png`

- `object_icon.png`


## indra/newview/skins/ionic/textures/navbar/ (9 files)

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `separator.png`


## indra/newview/skins/ionic/textures/script_editor/ (14 files)

- `green_square.png`

- `red_square.png`

- `script_config.png`

- `script_copy.png`

- `script_cut.png`

- `script_disk_load.png`

- `script_disk_save.png`

- `script_editor.png`

- `script_paste.png`

- `script_redo.png`

- `script_save.png`

- `script_search.png`

- `script_undo.png`

- `yellow_square.png`


## indra/newview/skins/ionic/textures/taskpanel/ (14 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Open_Off.png`

- `TabIcon_People_Off.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Things_Off.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Selected.png`


## indra/newview/skins/ionic/textures/widgets/ (99 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Badge_Background.png`

- `Badge_Border.png`

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Press.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Off.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `DisclosureArrow_Opened_Off.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Press.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `Marketplace_Dropzone_Background.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Login.png`

- `PushButton_Login_Over.png`

- `PushButton_Login_Pressed.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Press.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Vert.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `TextField_Active.png`

- `TextField_Active_Dark.png`

- `TextField_Disabled.png`

- `TextField_Disabled_Dark.png`

- `TextField_Off.png`

- `TextField_Off_Dark.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Highlight.png`

- `Tooltip.png`

- `bevel_background.png`

- `horizontal_drag_handle.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`

- `vertical_drag_handle.png`


## indra/newview/skins/ionic/textures/windows/ (32 files)

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Collapse_Foreground.png`

- `Icon_Collapse_Press.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Resize_Corner.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `Window_Square_NoTransparentEdges.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/ionic/textures/world/ (6 files)

- `BeaconArrow.tga`

- `CameraDragDot.tga`

- `NoEntryLines.tga`

- `NoEntryPassLines.tga`

- `SunTexture.tga`

- `direction_arrow_small.tga`


## indra/newview/skins/ionic/xui/en/ (1 files)

- `panel_progress.xml`


## indra/newview/tests/ (124 files)

- `alagentlistupdates_test.cpp`

- `alagentlocationformat_test.cpp`

- `alapplinks_test.cpp`

- `albakeproxies_test.cpp`

- `albulkrename_test.cpp`

- `alcasfold_bench.cpp`

- `alcasfold_gl_fixture.h`

- `alcasfold_gl_test.cpp`

- `alchattimestamp_test.cpp`

- `alcolorwheelmodel_test.cpp`

- `alcrashreporter_test.cpp`

- `alcurvemodel_test.cpp`

- `aldaycyclelandmarks_test.cpp`

- `aldof_bench.cpp`

- `aldof_gl_fixture.h`

- `aldof_gl_test.cpp`

- `alfeedback_test.cpp`

- `alfeedbackoutbox_test.cpp`

- `alfriendbacklog_test.cpp`

- `algltfmaterialretry_test.cpp`

- `algradehistory_test.cpp`

- `algroupchanges_test.cpp`

- `algroupmembers_test.cpp`

- `almaturitypreference_test.cpp`

- `almotionpredictor_test.cpp`

- `almutelookup_test.cpp`

- `alnotecardembedded_test.cpp`

- `alobjectroster_test.cpp`

- `alpostchain_gl_fixture.h`

- `alprobereach_test.cpp`

- `alrecoverykeeper_test.cpp`

- `alregionretirement_test.cpp`

- `alsceneexplorerpredicate_test.cpp`

- `alscopedata_test.cpp`

- `alscriptanalysislane_test.cpp`

- `alscriptanalyzers_test.cpp`

- `alscriptcontentsindex_test.cpp`

- `alscriptcrumbsbar_test.cpp`

- `alscriptexplorermodel_test.cpp`

- `alscriptexplorertree_test.cpp`

- `alscriptexternaleditor_test.cpp`

- `alscriptinspectorpane_test.cpp`

- `alscriptitemdrop_test.cpp`

- `alscriptjobqueue_test.cpp`

- `alscriptkeymap_test.cpp`

- `alscriptlookup_test.cpp`

- `alscriptnavigation_test.cpp`

- `alscriptobjectcheck_test.cpp`

- `alscriptoutlinepane_test.cpp`

- `alscriptoutputpane_test.cpp`

- `alscriptproblemspane_test.cpp`

- `alscriptrecompile_test.cpp`

- `alscriptreferencespane_test.cpp`

- `alscriptregionusage_test.cpp`

- `alscriptsaveflow_test.cpp`

- `alscriptsearchpane_test.cpp`

- `alscriptsnippets_test.cpp`

- `alscriptstudio_fixture.h`

- `alscriptstudio_stubs.cpp`

- `alscriptstudio_stubs.h`

- `alscriptstudioaccount_test.cpp`

- `alscriptstudiocaret_test.cpp`

- `alscriptstudiochecking_test.cpp`

- `alscriptstudiocommands_test.cpp`

- `alscriptstudiocomparepairs_test.cpp`

- `alscriptstudiocomparewith_test.cpp`

- `alscriptstudiodoc_test.cpp`

- `alscriptstudioexpandedcompare_test.cpp`

- `alscriptstudiofiles_test.cpp`

- `alscriptstudiohistory_test.cpp`

- `alscriptstudiomasters_test.cpp`

- `alscriptstudiomerging_test.cpp`

- `alscriptstudioorphans_test.cpp`

- `alscriptstudiorecovery_test.cpp`

- `alscriptstudiosaving_test.cpp`

- `alscriptstudioselections_test.cpp`

- `alscriptstudiovim_test.cpp`

- `alscriptstudioweighing_test.cpp`

- `alscriptstudiowords_test.cpp`

- `alscripttheme_test.cpp`

- `alscripttypes_test.cpp`

- `alscriptweightspane_test.cpp`

- `alselectionoutline_gl_test.cpp`

- `alssrhistory_bench.cpp`

- `alteleportprogress_test.cpp`

- `alterrainsurfacemaps_test.cpp`

- `altextureboost_test.cpp`

- `altexturetable_test.cpp`

- `alwhitebalancesolver_test.cpp`

- `copycolor_gl_test.cpp`

- `cppfeatures_test.cpp`

- `llagentaccess_test.cpp`

- `llagentbenefits_test.cpp`

- `llautoreplace_test.cpp`

- `llchatservicehistorycore_test.cpp`

- `llconversationlog_test.cpp`

- `lldateutil_test.cpp`

- `llgroupdata_test.cpp`

- `llhttpretrypolicy_test.cpp`

- `lllogininstance_test.cpp`

- `llremoteparcelrequest_test.cpp`

- `llsecapi_test.cpp`

- `llsechandler_basic_test.cpp`

- `llslurl_test.cpp`

- `lltextureinfo_test.cpp`

- `llversioninfo_test.cpp`

- `llviewerassetstats_test.cpp`

- `llviewercontrollistener_test.cpp`

- `llviewerhelputil_test.cpp`

- `llviewernetwork_test.cpp`

- `llvieweroctree_stub.cpp`

- `llviewertexture_stub.cpp`

- `llvocache_test.cpp`

- `llworldmap_test.cpp`

- `llworldmipmap_test.cpp`

- `luminance_gl_test.cpp`

- `lutcube_test.cpp`

- `newview_test_checks.cpp`

- `newview_test_fakes.cpp`

- `newview_test_fakes.h`

- `newview_test_settings.cpp`

- `noise_test.cpp`

- `objectskinblock_gl_test.cpp`

- `shadowutil_gl_test.cpp`


## indra/newview/tr.lproj/ (1 files)

- `language.txt`


## indra/newview/uk.lproj/ (1 files)

- `language.txt`


## indra/newview/zh-Hans.lproj/ (1 files)

- `language.txt`


## indra/rust/ (2 files)

- `Cargo.lock`

- `Cargo.toml`


## indra/rust/pnj2k_libc/ (4 files)

- `Cargo.lock`

- `Cargo.toml`

- `LICENSE-APACHE`

- `LICENSE-MIT`


## indra/rust/pnj2k_libc/include/ (1 files)

- `pnj2k.h`


## indra/rust/pnj2k_libc/src/ (1 files)

- `lib.rs`


## indra/rust/velopack_libc/ (2 files)

- `Cargo.toml`

- `LICENSE`


## indra/rust/velopack_libc/include/ (2 files)

- `Velopack.h`

- `Velopack.hpp`


## indra/rust/velopack_libc/src/ (5 files)

- `csource.rs`

- `lib.rs`

- `raw.rs`

- `statics.rs`

- `types.rs`


## indra/template_verifier/ (2 files)

- `CMakeLists.txt`

- `template_verifier.cpp`


## indra/test/ (31 files)

- `CMakeLists.txt`

- `albigscript.h`

- `alrandomreseed.h`

- `altestbenchmark.h`

- `altestfailure.h`

- `altestfatal.cpp`

- `altestfatal.h`

- `altesthelper.cpp`

- `altesthelper.h`

- `altestlinks.cpp`

- `altestlinks.h`

- `altestlogreplay.cpp`

- `altestlogreplay.h`

- `altestmain.cpp`

- `altestmatchers.cpp`

- `altestmatchers.h`

- `altestname.cpp`

- `altestname.h`

- `altestsanitizer.h`

- `alteststateguard.cpp`

- `alteststateguard.h`

- `altestteardown.cpp`

- `altestteardown.h`

- `catch_and_store_what_in.h`

- `debug.h`

- `llsdtraits.h`

- `lltestapp.h`

- `namedtempfile.h`

- `print.h`

- `run_and_expect.cmake`

- `sync.h`


## indra/test/sanitizers/ (3 files)

- `lsan.supp`

- `tsan.supp`

- `ubsan.supp`


## indra/test/tests/ (2 files)

- `altestsupport_bench.cpp`

- `altestsupport_test.cpp`


## indra/viewer_components/ (1 files)

- `CMakeLists.txt`


## indra/viewer_components/Resources/ (2 files)

- `README`

- `summary.json`


## indra/viewer_components/login/ (3 files)

- `CMakeLists.txt`

- `lllogin.cpp`

- `lllogin.h`


## indra/viewer_components/login/tests/ (1 files)

- `lllogin_test.cpp`


## scripts/ (2 files)

- `md5check.py`

- `setup-path.py`


## scripts/ci/ (4 files)

- `msvc_environment.py`

- `python_tools.py`

- `test_msvc_environment.py`

- `test_python_tools.py`


## scripts/code_tools/ (7 files)

- `check_raw_gl.py`

- `fix_whitespace.py`

- `fix_xml_indentations.py`

- `modified-strings.sh`

- `modified_strings.py`

- `raw_gl_baseline.txt`

- `test_check_raw_gl.py`


## scripts/content_tools/ (11 files)

- `anim_tool.py`

- `arche_tool.py`

- `check_exposure.py`

- `check_lens_dirt.py`

- `check_lens_flare_state.py`

- `check_script_strings.py`

- `check_sh_projection.py`

- `dae_tool.py`

- `generate_lsl_traits.py`

- `generate_studio_icons.py`

- `skel_tool.py`


## scripts/messages/ (1 files)

- `message_template.msg`


## scripts/metrics/ (2 files)

- `viewer_asset_logs.py`

- `viewerstats.py`


## scripts/perf/ (5 files)

- `logsdir.py`

- `perfbot_run.py`

- `profile_cmp.py`

- `profile_csv.py`

- `profile_pretty.py`


## scripts/signing/ (1 files)

- `macos_signing_secrets.py`


## scripts/templates/ (2 files)

- `template-cpp.cpp`

- `template-h.h`


## scripts/testing/ (3 files)

- `test_cost_report.py`

- `tut2catch.py`

- `tut_parity.py`


## scripts/testing/lsl/ (4 files)

- `axon_test_region_driver.lsl`

- `cycle_object_animations.lsl`

- `cycle_object_animations_v2.lsl`

- `move_in_circle_using_llSetRegionPos.lsl`


## scripts/vcpkg/ (2 files)

- `configure_r2_cache.py`

- `test_configure_r2_cache.py`
