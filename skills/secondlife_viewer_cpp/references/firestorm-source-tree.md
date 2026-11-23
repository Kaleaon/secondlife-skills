# Firestorm Source Tree (generated from FirestormViewer/phoenix-firestorm @master)

Complete file index of https://github.com/FirestormViewer/phoenix-firestorm (28105 files). Use it to locate the exact file for a subsystem before fetching or cloning it. Paths are grouped by directory.


## ./ (15 files)

- `.clang-format`

- `.editorconfig`

- `.git-blame-ignore-revs`

- `.gitattributes`

- `.gitignore`

- `.pre-commit-config.yaml`

- `CONTRIBUTING.md`

- `FIRESTORM-SOURCE_LICENSE_HEADER.txt`

- `LICENSE`

- `README.md`

- `autobuild.xml`

- `build.sh`

- `build_target.sh`

- `buildscripts_support_functions`

- `requirements.txt`


## .github/ (4 files)

- `dependabot.yaml`

- `dependabot.yml`

- `labeler.yaml`

- `pull_request_template.md`


## .github/workflows/ (14 files)

- `.gitattributes`

- `build.yaml`

- `build_sl_mac_only.yml`

- `build_viewer.yml`

- `check-pr.yaml`

- `cla.yaml`

- `deploy_only.yml`

- `label.yaml`

- `pre-commit.yaml`

- `qatest.yaml`

- `sign.yml`

- `stale.yaml`

- `tag-fs-build.yml`

- `tag-release.yaml`


## doc/ (12 files)

- `BUILD.LINUX.md`

- `LGPL-license.txt`

- `LICENSE-logos.txt`

- `LICENSE-source.txt`

- `building_linux.md`

- `building_macos.md`

- `building_windows.md`

- `contributions.txt`

- `external-editor-json-rpc.md`

- `firestorm_256.png`

- `linux-crash-reporting.md`

- `translations.txt`


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


## fsutils/ (9 files)

- `build_config.json`

- `build_config.py`

- `ci.py`

- `ci_macos.py`

- `download_list.py`

- `parse_avatar_lad.py`

- `translation_fix_bad_attributes.py`

- `translation_prune_orphans.py`

- `translation_strings_auditing_tool.py`


## fsutils/tests/ (6 files)

- `test_build_config.py`

- `test_ci.py`

- `test_ci_macos.py`

- `test_dmg_templates.py`

- `test_linux_symbols.py`

- `test_run_tests_option.py`


## indra/ (2 files)

- `CMakeLists.txt`

- `Version`


## indra/cmake/ (95 files)

- `00-COMPILE-LINK-RUN.txt`

- `00-Common.cmake`

- `APR.cmake`

- `Audio.cmake`

- `Boost.cmake`

- `BuildPackagesInfo.cmake`

- `BuildVersion.cmake`

- `CEFPlugin.cmake`

- `CMakeCopyIfDifferent.cmake`

- `CMakeLists.txt`

- `CURL.cmake`

- `ColladaDom.cmake`

- `Copy3rdPartyLibs.cmake`

- `CubemapToEquirectangularJS.cmake`

- `DeploySharedLibs.cmake`

- `Discord.cmake`

- `DragDrop.cmake`

- `EXPAT.cmake`

- `ExamplePlugin.cmake`

- `FMODSTUDIO.cmake`

- `FindAutobuild.cmake`

- `FindPipeWire.cmake`

- `FindSCP.cmake`

- `FreeType.cmake`

- `GLEXT.cmake`

- `GLIB.cmake`

- `GLM.cmake`

- `GLOD.cmake`

- `GStreamer10Plugin.cmake`

- `Growl.cmake`

- `Havok.cmake`

- `Hunspell.cmake`

- `JPEG.cmake`

- `JPEGEncoderBasic.cmake`

- `LLAddBuildTest.cmake`

- `LLAppearance.cmake`

- `LLAudio.cmake`

- `LLCA.cmake`

- `LLCommon.cmake`

- `LLCoreHttp.cmake`

- `LLImage.cmake`

- `LLKDU.cmake`

- `LLMath.cmake`

- `LLPhysicsExtensions.cmake`

- `LLPrimitive.cmake`

- `LLSharedLibs.cmake`

- `LLTestCommand.cmake`

- `LLWindow.cmake`

- `LSLDefinitions.cmake`

- `LibVLCPlugin.cmake`

- `Linking.cmake`

- `MediaPluginBase.cmake`

- `Meshoptimizer.cmake`

- `Mikktspace.cmake`

- `NDOF.cmake`

- `NGHTTP2.cmake`

- `NVAPI.cmake`

- `OPENAL.cmake`

- `OpenGL.cmake`

- `OpenJPEG.cmake`

- `OpenSSL.cmake`

- `OpenXR.cmake`

- `PNG.cmake`

- `PluginAPI.cmake`

- `Prebuilt.cmake`

- `PulseAudio.cmake`

- `Python.cmake`

- `SDL3.cmake`

- `SSE2NEON.cmake`

- `TemplateCheck.cmake`

- `ThreeJS.cmake`

- `TinyEXR.cmake`

- `TinyGLTF.cmake`

- `Tracy.cmake`

- `Tut.cmake`

- `UI.cmake`

- `UnixInstall.cmake`

- `VHACD.cmake`

- `Variables.cmake`

- `Velopack.cmake`

- `VersionControl.cmake`

- `Versions.cmake`

- `ViewerManager.cmake`

- `ViewerMiscLibs.cmake`

- `VisualLeakDetector.cmake`

- `VulkanGltf.cmake`

- `WebRTC.cmake`

- `ZLIBNG.cmake`

- `bugsplat.cmake`

- `cmake_dummy.cpp`

- `jemalloc.cmake`

- `run_build_test.py`

- `websocketpp.cmake`

- `windows-rcs.html`

- `xxHash.cmake`


## indra/copy_win_scripts/ (2 files)

- `CMakeLists.txt`

- `start-client.py`


## indra/doxygen/ (2 files)

- `CMakeLists.txt`

- `Doxyfile.in`


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


## indra/integration_tests/llui_libtest/ (5 files)

- `CMakeLists.txt`

- `llui_libtest.cpp`

- `llui_libtest.h`

- `llwidgetreg.cpp`

- `llwidgetreg.h`


## indra/lib/python/indra/ (1 files)

- `__init__.py`


## indra/lib/python/indra/ipc/ (4 files)

- `__init__.py`

- `compatibility.py`

- `llmessage.py`

- `tokenstream.py`


## indra/lib/python/indra/util/ (3 files)

- `__init__.py`

- `llmanifest.py`

- `test_win32_manifest.py`


## indra/linux_crash_logger/ (5 files)

- `CMakeLists.txt`

- `linux_crash_logger.cpp`

- `linux_crash_report.cpp`

- `linux_crash_report.h`

- `llcrashloggerlinux.h`


## indra/linux_crash_logger/tests/ (2 files)

- `report_driver.cpp`

- `test_report.py`


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


## indra/llaudio/ (22 files)

- `CMakeLists.txt`

- `llaudiodecodemgr.cpp`

- `llaudiodecodemgr.h`

- `llaudioengine.cpp`

- `llaudioengine.h`

- `llaudioengine_fmodstudio.cpp`

- `llaudioengine_fmodstudio.h`

- `llaudioengine_openal.cpp`

- `llaudioengine_openal.h`

- `lllistener.cpp`

- `lllistener.h`

- `lllistener_ds3d.h`

- `lllistener_fmodstudio.cpp`

- `lllistener_fmodstudio.h`

- `lllistener_openal.cpp`

- `lllistener_openal.h`

- `llstreamingaudio.h`

- `llstreamingaudio_fmodstudio.cpp`

- `llstreamingaudio_fmodstudio.h`

- `llvorbisencode.cpp`

- `llvorbisencode.h`

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


## indra/llcharacter/tests/ (1 files)

- `lljoint_test.cpp`


## indra/llcommon/ (254 files)

- `CMakeLists.txt`

- `StackWalker.cpp`

- `StackWalker.h`

- `always_return.h`

- `apply.cpp`

- `apply.h`

- `blockingconcurrentqueue.h`

- `chrono.h`

- `classic_callback.cpp`

- `classic_callback.h`

- `commoncontrol.cpp`

- `commoncontrol.h`

- `concurrentqueue.h`

- `fsfiletime.h`

- `fsyspath.h`

- `function_types.h`

- `hbxxh.cpp`

- `hbxxh.h`

- `hexdump.h`

- `indra_constants.cpp`

- `indra_constants.h`

- `inlinemutexs.h`

- `is_approx_equal_fraction.h`

- `lazyeventapi.cpp`

- `lazyeventapi.h`

- `lightweightsemaphore.h`

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

- `lldictionary.cpp`

- `lldictionary.h`

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

- `llfasttimer.cpp`

- `llfasttimer.h`

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

- `llmetricperformancetester.cpp`

- `llmetricperformancetester.h`

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

- `llprofiler.cpp`

- `llprofiler.h`

- `llprofilercategories.h`

- `llptrto.cpp`

- `llptrto.h`

- `llqueuedthread.cpp`

- `llqueuedthread.h`

- `llrand.cpp`

- `llrand.h`

- `llrefcount.cpp`

- `llrefcount.h`

- `llregex.h`

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

- `llstacktrace.cpp`

- `llstacktrace.h`

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

- `tea.cpp`

- `tea.h`

- `threadpool.cpp`

- `threadpool.h`

- `threadpool_fwd.h`

- `threadsafeschedule.h`

- `tuple.h`

- `u64.cpp`

- `u64.h`

- `workqueue.cpp`

- `workqueue.h`


## indra/llcommon/nd/ (6 files)

- `ndetw.cpp`

- `ndetw.h`

- `ndexceptions.cpp`

- `ndexceptions.h`

- `ndlogthrottle.cpp`

- `ndlogthrottle.h`


## indra/llcommon/res/ (2 files)

- `llcommon.rc.in`

- `resource.h`


## indra/llcommon/tests/ (51 files)

- `StringVec.h`

- `apply_test.cpp`

- `bitpack_test.cpp`

- `classic_callback_test.cpp`

- `commonmisc_test.cpp`

- `fsfiletime_test.cpp`

- `lazyeventapi_test.cpp`

- `listener.h`

- `llapp_test.cpp`

- `llbase64_test.cpp`

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

- `llexception_test.cpp`

- `llfile_test.cpp`

- `llfilepaths_test.cpp`

- `llfilepaths_test.py`

- `llframetimer_test.cpp`

- `llheteromap_test.cpp`

- `llhttpdate_test.cpp`

- `llinstancetracker_test.cpp`

- `llleap_test.cpp`

- `llmainthreadtask_test.cpp`

- `llpounceable_test.cpp`

- `llprocess_test.cpp`

- `llprocessor_test.cpp`

- `llprocessstdin_test.cpp`

- `llprocinfo_test.cpp`

- `llrand_test.cpp`

- `llsd_test.cpp`

- `llsdserialize_test.cpp`

- `llsdutil_test.cpp`

- `llsingleton_test.cpp`

- `llstreamtools_test.cpp`

- `llstring_test.cpp`

- `lltrace_test.cpp`

- `lltreeiterators_test.cpp`

- `llunits_test.cpp`

- `lluri_test.cpp`

- `stringize_test.cpp`

- `threadsafeschedule_test.cpp`

- `tuple_test.cpp`

- `workqueue_test.cpp`

- `wrapllerrs.h`


## indra/llcorehttp/ (56 files)

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


## indra/llcorehttp/tests/ (18 files)

- `jsonrpcws_test.cpp`

- `llcorehttp_test.cpp`

- `llcorehttp_test.h`

- `test_allocator.cpp`

- `test_allocator.h`

- `test_bufferarray.hpp`

- `test_bufferstream.hpp`

- `test_httpheaders.hpp`

- `test_httpoperation.hpp`

- `test_httprequest.hpp`

- `test_httprequestqueue.hpp`

- `test_httpstatus.hpp`

- `test_jsonrpcws.hpp`

- `test_llcorehttp_peer.py`

- `test_refcounted.hpp`

- `test_websocketmgr.hpp`

- `testwsclient.h`

- `wsserver_test.cpp`


## indra/llcrashlogger/ (7 files)

- `CMakeLists.txt`

- `llcrashlock.cpp`

- `llcrashlock.h`

- `llcrashlogger.cpp`

- `llcrashlogger.h`

- `llcrashlookup.cpp`

- `llcrashlookup.h`


## indra/llfilesystem/ (20 files)

- `CMakeLists.txt`

- `lldir.cpp`

- `lldir.h`

- `lldir_linux.cpp`

- `lldir_linux.h`

- `lldir_mac.cpp`

- `lldir_mac.h`

- `lldir_utils_objc.h`

- `lldir_utils_objc.mm`

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


## indra/llfilesystem/tests/ (7 files)

- `llcachewatermarks_test.cpp`

- `lldir_test.cpp`

- `lldiriterator_test.cpp`

- `lldiskcache_test.cpp`

- `llnonasciipaths_test.cpp`

- `llstaticassetpaths_test.cpp`

- `path_test_support.h`


## indra/llimage/ (24 files)

- `CMakeLists.txt`

- `llimage.cpp`

- `llimage.h`

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

- `llimageworker.cpp`

- `llimageworker.h`

- `llmapimagetype.h`

- `llpngwrapper.cpp`

- `llpngwrapper.h`


## indra/llimage/tests/ (1 files)

- `llimageworker_test.cpp`


## indra/llimagej2coj/ (3 files)

- `CMakeLists.txt`

- `llimagej2coj.cpp`

- `llimagej2coj.h`


## indra/llinventory/ (41 files)

- `CMakeLists.txt`

- `llcategory.cpp`

- `llcategory.h`

- `lleconomy.cpp`

- `lleconomy.h`

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


## indra/llinventory/tests/ (5 files)

- `inventorymisc_test.cpp`

- `llparcel_test.cpp`

- `llpermissions_test.cpp`

- `llsaleinfo_test.cpp`

- `lluserrelations_test.cpp`


## indra/llkdu/ (6 files)

- `CMakeLists.txt`

- `include_kdu_xxxx.h`

- `llimagej2ckdu.cpp`

- `llimagej2ckdu.h`

- `llkdumem.cpp`

- `llkdumem.h`


## indra/llkdu/tests/ (1 files)

- `llimagej2ckdu_test.cpp`


## indra/llmath/ (78 files)

- `CMakeLists.txt`

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

- `llperlin.cpp`

- `llperlin.h`

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


## indra/llmath/nd/ (2 files)

- `ndoctreelog.cpp`

- `ndoctreelog.h`


## indra/llmath/tests/ (16 files)

- `alignment_test.cpp`

- `llbbox_test.cpp`

- `llbboxlocal_test.cpp`

- `llmodularmath_test.cpp`

- `llquaternion_test.cpp`

- `llrect_test.cpp`

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


## indra/llmeshoptimizer/ (3 files)

- `CMakeLists.txt`

- `llmeshoptimizer.cpp`

- `llmeshoptimizer.h`


## indra/llmessage/ (161 files)

- `CMakeLists.txt`

- `fscorehttputil.cpp`

- `fscorehttputil.h`

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

- `lliohttpserver.cpp`

- `lliohttpserver.h`

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

- `llnullcipher.cpp`

- `llnullcipher.h`

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

- `llservice.cpp`

- `llservice.h`

- `llservicebuilder.cpp`

- `llservicebuilder.h`

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

- `lluseroperation.cpp`

- `lluseroperation.h`

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


## indra/llmessage/tests/ (31 files)

- `commtest.h`

- `io_test.cpp`

- `llavatarnamecache_test.cpp`

- `llbuffer_test.cpp`

- `llcoproceduremanager_test.cpp`

- `lldatapacker_test.cpp`

- `llhost_test.cpp`

- `llhttpnode_stub.cpp`

- `llhttpnode_test.cpp`

- `lliohttpserver_test.cpp`

- `llmessageconfig_test.cpp`

- `llmessagetemplateparser_test.cpp`

- `llnamevalue_test.cpp`

- `llpartdata_test.cpp`

- `llpipeutil.cpp`

- `llpipeutil.h`

- `llsdmessagebuilder_test.cpp`

- `llsdmessagereader_test.cpp`

- `llservicebuilder_test.cpp`

- `lltemplatemessagebuilder_test.cpp`

- `lltemplatemessagedispatcher_test.cpp`

- `lltestmessagesender.cpp`

- `lltestmessagesender.h`

- `lltrustedmessageservice_test.cpp`

- `llxfer_file_test.cpp`

- `llxorcipher_test.cpp`

- `llzerocode_test.cpp`

- `message_test.cpp`

- `networkio.h`

- `test_llsdmessage_peer.py`

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


## indra/llplugin/slplugin/ (5 files)

- `CMakeLists.txt`

- `slplugin-objc.h`

- `slplugin-objc.mm`

- `slplugin.cpp`

- `slplugin_info.plist`


## indra/llprecompiled/ (2 files)

- `CMakeLists.txt`

- `cmake_dummy.cpp`


## indra/llprimitive/ (36 files)

- `CMakeLists.txt`

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


## indra/llprimitive/tests/ (4 files)

- `llgltfmaterial_test.cpp`

- `llmediaentry_test.cpp`

- `llmessagesystem_stub.cpp`

- `llprimitive_test.cpp`


## indra/llrender/ (51 files)

- `CMakeLists.txt`

- `llcubemap.cpp`

- `llcubemap.h`

- `llcubemaparray.cpp`

- `llcubemaparray.h`

- `llfontbitmapcache.cpp`

- `llfontbitmapcache.h`

- `llfontfreetype.cpp`

- `llfontfreetype.h`

- `llfontfreetypesvg.cpp`

- `llfontfreetypesvg.h`

- `llfontgl.cpp`

- `llfontgl.h`

- `llfontregistry.cpp`

- `llfontregistry.h`

- `llfontvertexbuffer.cpp`

- `llfontvertexbuffer.h`

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


## indra/llrender/tests/ (2 files)

- `llgltexture_test.cpp`

- `llvertexbuffer_pool_test.cpp`


## indra/llui/ (230 files)

- `CMakeLists.txt`

- `fsregistrarutils.cpp`

- `fsregistrarutils.h`

- `fssearchablecontrol.h`

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

- `llkeywords.cpp`

- `llkeywords.h`

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

- `llrngwriter.cpp`

- `llrngwriter.h`

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

- `lluiusage.cpp`

- `lluiusage.h`

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

- `llviewereventrecorder.cpp`

- `llviewereventrecorder.h`

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


## indra/llui/tests/ (3 files)

- `llurlentry_stub.cpp`

- `llurlentry_test.cpp`

- `llurlmatch_test.cpp`


## indra/llwebrtc/ (4 files)

- `CMakeLists.txt`

- `llwebrtc.cpp`

- `llwebrtc.h`

- `llwebrtc_impl.h`


## indra/llwindow/ (48 files)

- `CMakeLists.txt`

- `llappdelegate-objc.h`

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

- `llkeyboardmacosx.cpp`

- `llkeyboardmacosx.h`

- `llkeyboardsdl.cpp`

- `llkeyboardsdl.h`

- `llkeyboardsdl2.cpp`

- `llkeyboardsdl2.h`

- `llkeyboardwin32.cpp`

- `llkeyboardwin32.h`

- `llmousehandler.cpp`

- `llmousehandler.h`

- `llopenglview-objc.h`

- `llopenglview-objc.mm`

- `llpreeditor.h`

- `llsdl.cpp`

- `llsdl.h`

- `llwindow.cpp`

- `llwindow.h`

- `llwindowcallbacks.cpp`

- `llwindowcallbacks.h`

- `llwindowheadless.cpp`

- `llwindowheadless.h`

- `llwindowmacosx-objc.h`

- `llwindowmacosx-objc.mm`

- `llwindowmacosx.cpp`

- `llwindowmacosx.h`

- `llwindowmacosx_iokit.h`

- `llwindowmesaheadless.cpp`

- `llwindowmesaheadless.h`

- `llwindowsdl.cpp`

- `llwindowsdl.h`

- `llwindowwin32.cpp`

- `llwindowwin32.h`


## indra/llxml/ (9 files)

- `CMakeLists.txt`

- `llcontrol.cpp`

- `llcontrol.h`

- `llxmlnode.cpp`

- `llxmlnode.h`

- `llxmlparser.cpp`

- `llxmlparser.h`

- `llxmltree.cpp`

- `llxmltree.h`


## indra/llxml/tests/ (2 files)

- `llcontrol_test.cpp`

- `llxmlnode_test.cpp`


## indra/mac_crash_logger/ (1 files)

- `.DS_Store`


## indra/media_plugins/ (1 files)

- `CMakeLists.txt`


## indra/media_plugins/base/ (4 files)

- `CMakeLists.txt`

- `media_plugin_base.cpp`

- `media_plugin_base.exp`

- `media_plugin_base.h`


## indra/media_plugins/cef/ (9 files)

- `CMakeLists.txt`

- `linux_volume_catcher.cpp`

- `linux_volume_catcher_pa_syms.inc`

- `linux_volume_catcher_paglib_syms.inc`

- `mac_volume_catcher.cpp`

- `media_plugin_cef.cpp`

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


## indra/media_plugins/gstreamer10/ (6 files)

- `CMakeLists.txt`

- `llmediaimplgstreamer.h`

- `llmediaimplgstreamer_syms.cpp`

- `llmediaimplgstreamer_syms.h`

- `llmediaimplgstreamer_syms_raw.inc`

- `media_plugin_gstreamer10.cpp`


## indra/media_plugins/libvlc/ (2 files)

- `CMakeLists.txt`

- `media_plugin_libvlc.cpp`


## indra/newview/ (1724 files)

- `CMakeLists.txt`

- `Firestorm.xib`

- `Info-Firestorm.plist`

- `Info-SecondLife.plist`

- `LGPL-license.txt`

- `NACLantispam.cpp`

- `NACLantispam.h`

- `NACLfloaterexploresounds.cpp`

- `NACLfloaterexploresounds.h`

- `SMAAAreaTex.h`

- `SMAASearchTex.h`

- `SecondLife.xib`

- `VIEWER_VERSION.txt`

- `VIEWER_VERSION_FS.txt`

- `ViewerInstall.cmake`

- `VivoxAUP.rtf`

- `VivoxAUP.txt`

- `alfloaterregiontracker.cpp`

- `alfloaterregiontracker.h`

- `animationexplorer.cpp`

- `animationexplorer.h`

- `ao.cpp`

- `ao.h`

- `aoengine.cpp`

- `aoengine.h`

- `aoset.cpp`

- `aoset.h`

- `bugsplatattributes.cpp`

- `bugsplatattributes.h`

- `chatbar_as_cmdline.cpp`

- `chatbar_as_cmdline.h`

- `cube.dae`

- `daeexport.cpp`

- `daeexport.h`

- `desktopnotifierlinux.cpp`

- `desktopnotifierlinux.h`

- `dialogstack.cpp`

- `dialogstack.h`

- `exoflickr.cpp`

- `exoflickr.h`

- `exoflickrauth.cpp`

- `exoflickrauth.h`

- `exoflickrkeys.h.in`

- `exogroupmutelist.cpp`

- `exogroupmutelist.h`

- `featuretable.txt`

- `featuretable_linux.txt`

- `featuretable_mac.txt`

- `firestorm_icon.icns`

- `firestormos_icon.icns`

- `floatermedialists.cpp`

- `floatermedialists.h`

- `fs_viewer_manifest.py`

- `fsareasearch.cpp`

- `fsareasearch.h`

- `fsareasearchmenu.cpp`

- `fsareasearchmenu.h`

- `fsassetblacklist.cpp`

- `fsassetblacklist.h`

- `fsavatarrenderpersistence.cpp`

- `fsavatarrenderpersistence.h`

- `fsavatarsearchmenu.cpp`

- `fsavatarsearchmenu.h`

- `fsblocklistmenu.cpp`

- `fsblocklistmenu.h`

- `fschathistory.cpp`

- `fschathistory.h`

- `fschatoptionsmenu.cpp`

- `fschatoptionsmenu.h`

- `fschatparticipants.h`

- `fscommon.cpp`

- `fscommon.h`

- `fsconsoleutils.cpp`

- `fsconsoleutils.h`

- `fscontactsfriendsmenu.cpp`

- `fscontactsfriendsmenu.h`

- `fsdata.cpp`

- `fsdata.h`

- `fsdiscordconnect.cpp`

- `fsdiscordconnect.h`

- `fsdiscordkey.h.in`

- `fsdispatchclassifiedclickthrough.h`

- `fsdroptarget.cpp`

- `fsdroptarget.h`

- `fsexportperms.cpp`

- `fsexportperms.h`

- `fsfavoritegroups.cpp`

- `fsfavoritegroups.h`

- `fsfloateraddtocontactset.cpp`

- `fsfloateraddtocontactset.h`

- `fsfloaterassetblacklist.cpp`

- `fsfloaterassetblacklist.h`

- `fsfloateravataralign.cpp`

- `fsfloateravataralign.h`

- `fsfloateravatarrendersettings.cpp`

- `fsfloateravatarrendersettings.h`

- `fsfloaterbigpreview.cpp`

- `fsfloaterbigpreview.h`

- `fsfloaterblocklist.cpp`

- `fsfloaterblocklist.h`

- `fsfloatercontacts.cpp`

- `fsfloatercontacts.h`

- `fsfloatercontactsetconfiguration.cpp`

- `fsfloatercontactsetconfiguration.h`

- `fsfloaterdiscord.cpp`

- `fsfloaterdiscord.h`

- `fsfloaterexport.cpp`

- `fsfloaterexport.h`

- `fsfloatergroup.cpp`

- `fsfloatergroup.h`

- `fsfloatergrouptitles.cpp`

- `fsfloatergrouptitles.h`

- `fsfloaterim.cpp`

- `fsfloaterim.h`

- `fsfloaterimcontainer.cpp`

- `fsfloaterimcontainer.h`

- `fsfloaterimport.cpp`

- `fsfloaterimport.h`

- `fsfloaternearbychat.cpp`

- `fsfloaternearbychat.h`

- `fsfloaterpartialinventory.cpp`

- `fsfloaterpartialinventory.h`

- `fsfloaterperformance.cpp`

- `fsfloaterperformance.h`

- `fsfloaterplacedetails.cpp`

- `fsfloaterplacedetails.h`

- `fsfloaterposer.cpp`

- `fsfloaterposer.h`

- `fsfloaterposestand.cpp`

- `fsfloaterposestand.h`

- `fsfloaterprimfeed.cpp`

- `fsfloaterprimfeed.h`

- `fsfloaterprotectedfolders.cpp`

- `fsfloaterprotectedfolders.h`

- `fsfloaterradar.cpp`

- `fsfloaterradar.h`

- `fsfloatersearch.cpp`

- `fsfloatersearch.h`

- `fsfloatersplashscreensettings.cpp`

- `fsfloatersplashscreensettings.h`

- `fsfloaterstatistics.cpp`

- `fsfloaterstatistics.h`

- `fsfloaterstreamtitle.cpp`

- `fsfloaterstreamtitle.h`

- `fsfloaterteleporthistory.cpp`

- `fsfloaterteleporthistory.h`

- `fsfloatervoicecontrols.cpp`

- `fsfloatervoicecontrols.h`

- `fsfloatervolumecontrols.cpp`

- `fsfloatervolumecontrols.h`

- `fsfloatervramusage.cpp`

- `fsfloatervramusage.h`

- `fsfloaterwearablefavorites.cpp`

- `fsfloaterwearablefavorites.h`

- `fsfloaterwhitelisthelper.cpp`

- `fsfloaterwhitelisthelper.h`

- `fsgridhandler.cpp`

- `fsgridhandler.h`

- `fsgrouptitleregionmgr.cpp`

- `fsgrouptitleregionmgr.h`

- `fsinventorycustomtabs.cpp`

- `fsinventorycustomtabs.h`

- `fsjointpose.cpp`

- `fsjointpose.h`

- `fsjointrotatetool.cpp`

- `fsjointrotatetool.h`

- `fskeywords.cpp`

- `fskeywords.h`

- `fslocalmeshimportbase.cpp`

- `fslocalmeshimportbase.h`

- `fslocalmeshimportgltf.cpp`

- `fslocalmeshimportgltf.h`

- `fslslbridge.cpp`

- `fslslbridge.h`

- `fslslbridgerequest.cpp`

- `fslslbridgerequest.h`

- `fslslpreproc.cpp`

- `fslslpreproc.h`

- `fslslpreprocpath.h`

- `fslslpreprocviewer.cpp`

- `fslslpreprocviewer.h`

- `fsmaniprotatejoint.cpp`

- `fsmaniprotatejoint.h`

- `fsmaniptranslatejoint.cpp`

- `fsmaniptranslatejoint.h`

- `fsmoneytracker.cpp`

- `fsmoneytracker.h`

- `fsnamelistavatarmenu.cpp`

- `fsnamelistavatarmenu.h`

- `fsnearbychatbarlistener.cpp`

- `fsnearbychatbarlistener.h`

- `fsnearbychatcontrol.cpp`

- `fsnearbychatcontrol.h`

- `fsnearbychathub.cpp`

- `fsnearbychathub.h`

- `fsnearbychatvoicemonitor.cpp`

- `fsnearbychatvoicemonitor.h`

- `fspanelblocklist.cpp`

- `fspanelblocklist.h`

- `fspanelcontactsets.cpp`

- `fspanelcontactsets.h`

- `fspanelface.cpp`

- `fspanelface.h`

- `fspanelimcontrolpanel.cpp`

- `fspanelimcontrolpanel.h`

- `fspanellogin.cpp`

- `fspanellogin.h`

- `fspanelpreferenceuisounds.cpp`

- `fspanelpreferenceuisounds.h`

- `fspanelprefs.cpp`

- `fspanelprefs.h`

- `fspanelradar.cpp`

- `fspanelradar.h`

- `fsparticipantlist.cpp`

- `fsparticipantlist.h`

- `fspose.cpp`

- `fspose.h`

- `fsposeranimator.cpp`

- `fsposeranimator.h`

- `fsposestate.cpp`

- `fsposestate.h`

- `fsposingmotion.cpp`

- `fsposingmotion.h`

- `fsprimfeedauth.cpp`

- `fsprimfeedauth.h`

- `fsprimfeedconnect.cpp`

- `fsprimfeedconnect.h`

- `fsradar.cpp`

- `fsradar.h`

- `fsradarentry.cpp`

- `fsradarentry.h`

- `fsradarlistctrl.cpp`

- `fsradarlistctrl.h`

- `fsradarmenu.cpp`

- `fsradarmenu.h`

- `fsregioncross.cpp`

- `fsregioncross.h`

- `fsscriptlibrary.cpp`

- `fsscriptlibrary.h`

- `fsscrolllistctrl.cpp`

- `fsscrolllistctrl.h`

- `fssearchableui.cpp`

- `fssearchableui.h`

- `fsslurl.cpp`

- `fsslurl.h`

- `fsslurlcommand.cpp`

- `fsslurlcommand.h`

- `fsvirtualtrackpad.cpp`

- `fsvirtualtrackpad.h`

- `fsworldmapmessage.cpp`

- `fsworldmapmessage.h`

- `gltfscenemanager.cpp`

- `gltfscenemanager.h`

- `groupchatlistener.cpp`

- `groupchatlistener.h`

- `growlmanager.cpp`

- `growlmanager.h`

- `growlnotifier.h`

- `growlnotifierwin.cpp`

- `growlnotifierwin.h`

- `lfsimfeaturehandler.cpp`

- `lfsimfeaturehandler.h`

- `lggbeamcolormapfloater.cpp`

- `lggbeamcolormapfloater.h`

- `lggbeammapfloater.cpp`

- `lggbeammapfloater.h`

- `lggbeammaps.cpp`

- `lggbeammaps.h`

- `lggbeamscolors.cpp`

- `lggbeamscolors.h`

- `lggcontactsets.cpp`

- `lggcontactsets.h`

- `licenses-linux.txt`

- `licenses-mac.txt`

- `licenses-win32.txt`

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

- `llagentwearablesfetch.cpp`

- `llagentwearablesfetch.h`

- `llaisapi.cpp`

- `llaisapi.h`

- `llanimstatelabels.cpp`

- `llanimstatelabels.h`

- `llappcorehttp.cpp`

- `llappcorehttp.h`

- `llappdelegate-objc.mm`

- `llappearance.h`

- `llappearancelistener.cpp`

- `llappearancelistener.h`

- `llappearancemgr.cpp`

- `llappearancemgr.h`

- `llappviewer.cpp`

- `llappviewer.h`

- `llappviewerlinux.cpp`

- `llappviewerlinux.h`

- `llappviewerlistener.cpp`

- `llappviewerlistener.h`

- `llappviewermacosx-for-objc.h`

- `llappviewermacosx-objc.h`

- `llappviewermacosx-objc.mm`

- `llappviewermacosx.cpp`

- `llappviewermacosx.h`

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

- `llcallingcard.cpp`

- `llcallingcard.h`

- `llcapabilityprovider.h`

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

- `lldrawpoolsky.cpp`

- `lldrawpoolsky.h`

- `lldrawpoolterrain.cpp`

- `lldrawpoolterrain.h`

- `lldrawpooltree.cpp`

- `lldrawpooltree.h`

- `lldrawpoolwater.cpp`

- `lldrawpoolwater.h`

- `lldrawpoolwaterexclusion.cpp`

- `lldrawpoolwaterexclusion.h`

- `lldrawpoolwlsky.cpp`

- `lldrawpoolwlsky.h`

- `lldynamictexture.cpp`

- `lldynamictexture.h`

- `llemote.cpp`

- `llemote.h`

- `llenvadapters.cpp`

- `llenvadapters.h`

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

- `llfasttimerview.cpp`

- `llfasttimerview.h`

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

- `llflickrconnect.cpp`

- `llflickrconnect.h`

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

- `llfloaterflickr.cpp`

- `llfloaterflickr.h`

- `llfloaterfonttest.cpp`

- `llfloaterfonttest.h`

- `llfloaterforgetuser.cpp`

- `llfloaterforgetuser.h`

- `llfloatergesture.cpp`

- `llfloatergesture.h`

- `llfloatergestureautocompletepicker.cpp`

- `llfloatergestureautocompletepicker.h`

- `llfloatergltfasseteditor.cpp`

- `llfloatergltfasseteditor.h`

- `llfloatergodtools.cpp`

- `llfloatergodtools.h`

- `llfloatergotoline.cpp`

- `llfloatergotoline.h`

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

- `llfloaternotificationsconsole.cpp`

- `llfloaternotificationsconsole.h`

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

- `llfloaterproperties.cpp`

- `llfloaterproperties.h`

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

- `llfloaterscriptedprefs.cpp`

- `llfloaterscriptedprefs.h`

- `llfloaterscripting.cpp`

- `llfloaterscripting.h`

- `llfloaterscriptlimits.cpp`

- `llfloaterscriptlimits.h`

- `llfloaterscriptrecover.cpp`

- `llfloaterscriptrecover.h`

- `llfloatersearch.cpp`

- `llfloatersearch.h`

- `llfloatersearchreplace.cpp`

- `llfloatersearchreplace.h`

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

- `llfloateruipreview.cpp`

- `llfloateruipreview.h`

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

- `llhints.cpp`

- `llhints.h`

- `llhttpretrypolicy.cpp`

- `llhttpretrypolicy.h`

- `llhudeffect.cpp`

- `llhudeffect.h`

- `llhudeffectbeam.cpp`

- `llhudeffectbeam.h`

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

- `lllocalbitmaps.cpp`

- `lllocalbitmaps.h`

- `lllocalgltfmaterials.cpp`

- `lllocalgltfmaterials.h`

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

- `llpanelopenregionsettings.cpp`

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

- `llpatchvertexarray.cpp`

- `llpatchvertexarray.h`

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

- `llpreviewscript.cpp`

- `llpreviewscript.h`

- `llpreviewsound.cpp`

- `llpreviewsound.h`

- `llpreviewtexture.cpp`

- `llpreviewtexture.h`

- `llproductinforequest.cpp`

- `llproductinforequest.h`

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

- `llscripteditor.cpp`

- `llscripteditor.h`

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

- `llsky.cpp`

- `llsky.h`

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

- `llvoicevivox.cpp`

- `llvoicevivox.h`

- `llvoicewebrtc.cpp`

- `llvoicewebrtc.h`

- `llvoinventorylistener.cpp`

- `llvoinventorylistener.h`

- `llvopartgroup.cpp`

- `llvopartgroup.h`

- `llvosky.cpp`

- `llvosky.h`

- `llvosurfacepatch.cpp`

- `llvosurfacepatch.h`

- `llvotree.cpp`

- `llvotree.h`

- `llvovolume.cpp`

- `llvovolume.h`

- `llvowater.cpp`

- `llvowater.h`

- `llvowlsky.cpp`

- `llvowlsky.h`

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

- `llwldaycycle.cpp`

- `llwldaycycle.h`

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

- `luau.txt`

- `noise.cpp`

- `noise.h`

- `omnifilter.cpp`

- `omnifilter.h`

- `omnifilterengine.cpp`

- `omnifilterengine.h`

- `particleeditor.cpp`

- `particleeditor.h`

- `permissionstracker.cpp`

- `permissionstracker.h`

- `pieautohide.cpp`

- `pieautohide.h`

- `piemenu.cpp`

- `piemenu.h`

- `pieseparator.cpp`

- `pieseparator.h`

- `pieslice.cpp`

- `pieslice.h`

- `pipeline.cpp`

- `pipeline.h`

- `qtoolalign.cpp`

- `qtoolalign.h`

- `quickprefs.cpp`

- `quickprefs.h`

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

- `sanitycheck.cpp`

- `sanitycheck.h`

- `secondlife-i686.supp`

- `secondlife.icns`

- `secondlife_firstlook.icns`

- `slplugin.entitlements`

- `streamtitledisplay.cpp`

- `streamtitledisplay.h`

- `utilitybar.cpp`

- `utilitybar.h`

- `viewer_manifest.py`

- `vjfloaterlocalmesh.cpp`

- `vjfloaterlocalmesh.h`

- `vjlocalmesh.cpp`

- `vjlocalmesh.h`

- `vjlocalmeshimportdae.cpp`

- `vjlocalmeshimportdae.h`

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


## indra/newview/app_settings/ (39 files)

- `anim.ini`

- `autoreplace.xml`

- `client_list_v2.xml`

- `cloud.xml`

- `cmd_line.xml`

- `commands.xml`

- `emoji_groups.xml`

- `foldertypes.xml`

- `gamecontrollerdb.txt`

- `graphic_preset_controls.xml`

- `grass.xml`

- `grids.xml`

- `growl_notifications.xml`

- `ignorable_dialogs.xml`

- `key_bindings.xml`

- `keywords.ini`

- `lindenlab.pem`

- `llsd-lsl-syntax.rng`

- `llsd.xsd`

- `logcontrol.xml`

- `message.xml`

- `posestand.xml`

- `quick_preferences.xml`

- `scriptlibrary_aa.xml`

- `scriptlibrary_ossl.xml`

- `scriptlibrary_preproc.xml`

- `settings.xml`

- `settings_crash_behavior.xml`

- `settings_files.xml`

- `settings_firestorm.xml`

- `settings_hybrid.xml`

- `settings_modern.xml`

- `settings_per_account.xml`

- `settings_phoenix.xml`

- `settings_text.xml`

- `settings_v3.xml`

- `std_bump.ini`

- `trees.xml`

- `viewerart.xml`


## indra/newview/app_settings/beams/ (19 files)

- `Angry_Face.xml`

- `Black_Smile.xml`

- `Circle.xml`

- `Color_Assortment.xml`

- `Color_Wheel.xml`

- `Cross.xml`

- `Fire.xml`

- `Heart.xml`

- `LGG.xml`

- `Orbit_Rings.xml`

- `Phoenix.xml`

- `Quad_Spike.xml`

- `Solid.xml`

- `Spiral.xml`

- `Square.xml`

- `Star.xml`

- `USFlag.xml`

- `YingYang.xml`

- `ZigZag.xml`


## indra/newview/app_settings/beamsColors/ (5 files)

- `Cute.xml`

- `Fire.xml`

- `Phoenix.xml`

- `Rainbow.xml`

- `Water.xml`


## indra/newview/app_settings/camera/ (4 files)

- `Front.xml`

- `Rear.xml`

- `Side.xml`

- `TPP.xml`


## indra/newview/app_settings/filters/ (30 files)

- `Antique.xml`

- `Autocontrast.xml`

- `Badtrip.xml`

- `BlackAndWhite.xml`

- `Blownhighlights.xml`

- `Brighten.xml`

- `Cartoon.xml`

- `Colors1970.xml`

- `Darken.xml`

- `Edges.xml`

- `Focus.xml`

- `Heatwave.xml`

- `Intense.xml`

- `Julesverne.xml`

- `LensFlare.xml`

- `Lightleak.xml`

- `Linearize.xml`

- `Miniature.xml`

- `Negative.xml`

- `Newspaper.xml`

- `Overcast.xml`

- `Posterize.xml`

- `Rotatecolors180.xml`

- `Sepia.xml`

- `Sharpen.xml`

- `Softfocus.xml`

- `Spotlight.xml`

- `Thematrix.xml`

- `Toycamera.xml`

- `Video.xml`


## indra/newview/app_settings/fs_static_assets/ (11 files)

- `0b4ee516-5dfd-ef4b-4ab6-300bb44cb045.animatn`

- `2029d88f-4efc-d72d-18d1-274caf9e9bc0.animatn`

- `23f3163c-183b-dac0-0cdd-7811bcc3b5f1.animatn`

- `2cfeed25-04f9-caff-f3d2-776cddea5771.animatn`

- `3481ccd5-cc6c-65ca-c466-dc9df1bf3944.animatn`

- `6e83f685-2f53-278f-6758-b529327cce09.animatn`

- `b23c52ef-0b15-11f2-852d-8fbd33417847.animatn`

- `b2f312aa-2c1e-27b8-50fe-a0fa4ff3df4e.animatn`

- `c17677b8-9fb2-8d6e-bbbe-219edce64ef4.animatn`

- `cff5559e-c915-0b5e-d587-f789b5cc299a.animatn`

- `e14fee5f-3735-a236-2e26-94f92f366d81.animatn`


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


## indra/newview/app_settings/shaders/ (2 files)

- `errorF.glsl`

- `errorV.glsl`


## indra/newview/app_settings/shaders/class1/avatar/ (6 files)

- `avatarF.glsl`

- `avatarSkinV.glsl`

- `avatarV.glsl`

- `eyeballF.glsl`

- `eyeballV.glsl`

- `objectSkinV.glsl`


## indra/newview/app_settings/shaders/class1/deferred/ (99 files)

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

- `avatarEyesV.glsl`

- `avatarF.glsl`

- `avatarShadowF.glsl`

- `avatarShadowV.glsl`

- `avatarV.glsl`

- `blurLightF.glsl`

- `blurLightV.glsl`

- `bumpF.glsl`

- `bumpV.glsl`

- `cloudsF.glsl`

- `cloudsV.glsl`

- `cofF.glsl`

- `deferredUtil.glsl`

- `diffuseAlphaMaskF.glsl`

- `diffuseAlphaMaskIndexedF.glsl`

- `diffuseAlphaMaskNoColorF.glsl`

- `diffuseF.glsl`

- `diffuseIndexedF.glsl`

- `diffuseNoColorV.glsl`

- `diffuseV.glsl`

- `dofCombineF.glsl`

- `emissiveF.glsl`

- `emissiveV.glsl`

- `exposureF.glsl`

- `fullbrightF.glsl`

- `fullbrightShinyV.glsl`

- `fullbrightV.glsl`

- `fxaaF.glsl`

- `gbufferUtil.glsl`

- `genbrdflutF.glsl`

- `genbrdflutV.glsl`

- `globalF.glsl`

- `highlightF.glsl`

- `impostorF.glsl`

- `impostorV.glsl`

- `luminanceF.glsl`

- `materialF.glsl`

- `materialV.glsl`

- `moonF.glsl`

- `moonV.glsl`

- `normgenF.glsl`

- `normgenV.glsl`

- `pbrShadowAlphaBlendF.glsl`

- `pbrShadowAlphaMaskF.glsl`

- `pbrShadowAlphaMaskV.glsl`

- `pbralphaF.glsl`

- `pbralphaV.glsl`

- `pbrglowF.glsl`

- `pbrglowV.glsl`

- `pbropaqueF.glsl`

- `pbropaqueV.glsl`

- `pbrterrainF.glsl`

- `pbrterrainUtilF.glsl`

- `pbrterrainV.glsl`

- `postDeferredF.glsl`

- `postDeferredGammaCorrect.glsl`

- `postDeferredNoDoFF.glsl`

- `postDeferredNoTCV.glsl`

- `postDeferredTonemap.glsl`

- `postDeferredV.glsl`

- `postDeferredVisualizeBuffers.glsl`

- `rlvF.glsl`

- `rlvV.glsl`

- `screenSpaceReflUtil.glsl`

- `shadowAlphaMaskF.glsl`

- `shadowAlphaMaskV.glsl`

- `shadowCubeV.glsl`

- `shadowF.glsl`

- `shadowSkinnedV.glsl`

- `shadowUtil.glsl`

- `shadowV.glsl`

- `skyF.glsl`

- `skyV.glsl`

- `starsF.glsl`

- `starsV.glsl`

- `sunDiscF.glsl`

- `sunDiscV.glsl`

- `terrainF.glsl`

- `terrainV.glsl`

- `textureUtilV.glsl`

- `tonemapUtilF.glsl`

- `treeF.glsl`

- `treeShadowF.glsl`

- `treeShadowSkinnedV.glsl`

- `treeShadowV.glsl`

- `treeV.glsl`


## indra/newview/app_settings/shaders/class1/effects/ (4 files)

- `glowExtractF.glsl`

- `glowExtractV.glsl`

- `glowF.glsl`

- `glowV.glsl`


## indra/newview/app_settings/shaders/class1/environment/ (4 files)

- `srgbF.glsl`

- `waterF.glsl`

- `waterFogF.glsl`

- `waterV.glsl`


## indra/newview/app_settings/shaders/class1/gltf/ (2 files)

- `pbrmetallicroughnessF.glsl`

- `pbrmetallicroughnessV.glsl`


## indra/newview/app_settings/shaders/class1/interface/ (44 files)

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

- `glowcombineFXAAF.glsl`

- `glowcombineFXAAV.glsl`

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

- `occlusionSkinnedV.glsl`

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


## indra/newview/app_settings/shaders/class1/post/ (3 files)

- `exoPostBaseV.glsl`

- `exoVignetteF.glsl`

- `snapshotFrameF.glsl`


## indra/newview/app_settings/shaders/class1/windlight/ (8 files)

- `atmosphericsF.glsl`

- `atmosphericsFuncs.glsl`

- `atmosphericsHelpersF.glsl`

- `atmosphericsHelpersV.glsl`

- `atmosphericsV.glsl`

- `atmosphericsVarsF.glsl`

- `atmosphericsVarsV.glsl`

- `gammaF.glsl`


## indra/newview/app_settings/shaders/class2/deferred/ (7 files)

- `alphaF.glsl`

- `pbralphaF.glsl`

- `reflectionProbeF.glsl`

- `softenLightV.glsl`

- `sunLightF.glsl`

- `sunLightSSAOF.glsl`

- `sunLightV.glsl`


## indra/newview/app_settings/shaders/class2/interface/ (3 files)

- `irradianceGenF.glsl`

- `reflectionprobeF.glsl`

- `reflectionprobeV.glsl`


## indra/newview/app_settings/shaders/class3/deferred/ (15 files)

- `fullbrightShinyF.glsl`

- `hazeF.glsl`

- `materialF.glsl`

- `multiPointLightF.glsl`

- `multiPointLightV.glsl`

- `pointLightF.glsl`

- `pointLightV.glsl`

- `reflectionProbeF.glsl`

- `screenSpaceReflPostF.glsl`

- `screenSpaceReflPostV.glsl`

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


## indra/newview/app_settings/static_assets/ (291 files)

- `00b48fa0-ac43-fadf-d061-6b726a24a90a.gesture`

- `0247dbfa-f37e-64ab-d09f-2678884c7f4a.gesture`

- `02862ac0-a61d-94c2-5d11-5f5d319b1256.clothing`

- `02c4eae7-b6a3-b4b0-44b0-b7b29d7f913f.clothing`

- `032ac149-dacd-e88a-5397-b9996b58f278.gesture`

- `038fcec9-5ebd-8a8e-0e2e-6e71a0a1ac53.animatn`

- `0401dc30-0fdd-1fc3-3e51-c683fe117184.gesture`

- `04608b19-1668-399c-5790-b7df8d9dc9cf.gesture`

- `05ddbff8-aaa9-92a1-2b74-8fe77a29b445.animatn`

- `07d61cde-bc5b-f95f-f747-2e57eab4ef12.clothing`

- `0813d01a-d3d3-32a4-48a3-26b6e1e01e39.gesture`

- `0836b67f-7f7b-f37b-c00a-460dc1521f5a.animatn`

- `08464f78-3a8e-2944-cba5-0c94aff3af29.animatn`

- `0a3336cf-3ad1-012a-91c2-5b5620aaaef3.gesture`

- `0a9fb970-8b44-9114-d3a9-bf69cfe804d6.animatn`

- `0b29c4fd-9c3c-3047-fcb4-addd3e42a289.clothing`

- `0c5f60ae-1a54-1ee8-398d-7ed278552132.bodypart`

- `0ce71257-7a07-257f-f023-fd68575a3a4e.gesture`

- `0eb702e2-cc5a-9a88-56a5-661a55c0676a.animatn`

- `0eeb5ef7-10dd-4e4a-11a5-d053011fcdf2.gesture`

- `0f86e355-dd31-a61c-fdb0-3a96b9aad05f.animatn`

- `11000694-3f41-adc2-606b-eee1d66f3724.animatn`

- `1232da7c-3d5b-a11b-cbee-d574aedc2e59.bodypart`

- `13b0d1c4-eb3c-9b89-2f13-9c0a714aab9f.clothing`

- `149739c0-f677-4b4c-1587-e44be72dd7ef.bodypart`

- `15468e00-3400-bb66-cecc-646d7c14458e.animatn`

- `159afee8-b7bf-c8fb-9c63-98276a1d6b28.gesture`

- `15dd911d-be82-2856-26db-27659b142875.animatn`

- `16803a9f-5140-e042-4d7b-d28ba247c325.animatn`

- `16ef95d1-2fe3-d4a3-509d-f03bb2d327ca.clothing`

- `17a387e1-28c7-e24b-4bfc-527b2d377a1b.clothing`

- `17c024cc-eef2-f6a0-3527-9869876d7752.animatn`

- `18b3a4b5-b463-bd48-e4b6-71eaac76c515.animatn`

- `1910ffbd-096c-5eb7-19f5-8c99ab6a748c.gesture`

- `19999406-3a3a-d58c-a2ac-d72e555dcf51.animatn`

- `1a2bd58e-87ff-0df8-0b4c-53e047b0bb6e.animatn`

- `1a5fe8ac-a804-8a5d-7cbd-56bd83184568.animatn`

- `1ab1b236-cd08-21e6-0cbc-0d923fc6eca2.animatn`

- `1ac2c678-3ab4-410b-2aad-30a7dc9c4504.gesture`

- `1b677754-5a07-641a-e989-34dcd985af1b.clothing`

- `1c7600d6-661f-b87b-efe2-d7421eb93c86.animatn`

- `1cb562b0-ba21-2202-efb3-30f82cdf9595.animatn`

- `1f5466aa-2b68-e370-6bb5-a335e859afeb.gesture`

- `201f3fdf-cb1f-dbec-201f-7333e328ae7c.animatn`

- `205ae4a8-42c6-1c5c-b142-672864fafe8a.bodypart`

- `20f063ea-8306-2562-0b07-5c853b37b31e.animatn`

- `2305bd75-1ca9-b03b-1faa-b176b8a8c49e.animatn`

- `230ff836-fe1e-ab33-80c6-ef029c658136.gesture`

- `2408fe9e-df1d-1d7d-f4ff-1384fa7b350f.animatn`

- `245f3c54-f1c0-bf2e-811f-46d8eeb386e7.animatn`

- `25252e5b-394b-fdab-76ee-28980cd62f81.gesture`

- `252acecb-a169-eff2-4601-b06bbeb91e84.gesture`

- `26a762c3-7164-0bbf-a7d6-ea097a6d0314.bodypart`

- `26cc2407-84b5-6887-4564-85a9b0cfb01f.gesture`

- `282d67ef-942e-27f4-9c7b-818f59967743.clothing`

- `29a56cc8-3fcf-c575-02c7-14a303b12e17.clothing`

- `29f11d26-7d80-4b53-a97c-fce85d94e392.gesture`

- `2b211c3e-d7c9-9e0e-0d96-e9357699bb25.clothing`

- `2b5a38b2-5e00-3a97-a495-4c826bc443e6.animatn`

- `2ca8ddae-23ef-0132-d243-7ae953582dd0.clothing`

- `2d03fd78-92fc-ca52-aabb-a4904e1339d1.gesture`

- `2d408f13-f437-e00e-8f6d-b0857580b034.bodypart`

- `2d6daa51-3192-6794-8e2e-a15f8338ec30.animatn`

- `30047778-10ea-1af7-6881-4db7a3a5a114.animatn`

- `30c1bdb4-1f99-3ee9-2a2e-098e4a3ceda6.clothing`

- `313b9881-4302-73c0-c7d0-0e7a36b6c224.animatn`

- `3147d815-6338-b932-f011-16b56d9ac18b.animatn`

- `315c3a41-a5f3-0ba4-27da-f893f769e69b.animatn`

- `33339176-7ddc-9397-94a4-bf3403cbc8f5.animatn`

- `347df5d8-c73b-009d-f19d-df78aea8ec22.bodypart`

- `349a3801-54f9-bf2c-3bd0-1ac89772af01.animatn`

- `35db4f7e-28c2-6679-cea9-3ee108f7fc7f.animatn`

- `36f81a92-f076-5893-dc4b-7c3795e487cf.animatn`

- `370f3a20-6ca6-9971-848c-9a01bc42ae3c.animatn`

- `37ea8e97-1d16-b28d-8a48-7c88b39321cb.clothing`

- `3d6da7ba-e4a3-e08c-b52e-98a40cb4dc33.bodypart`

- `3d8a32a0-3c25-ddcc-f807-e50f796e1dde.gesture`

- `3d94bad0-c55b-7dcc-8763-033c59405d33.animatn`

- `3da1d753-028a-5446-24f3-9c9b856d9422.animatn`

- `3f1cf9b6-f52c-46cd-bcf7-ffb7c8c25aea.gesture`

- `3f258e00-f5ac-68b2-bfb0-0c3c0fa3e614.gesture`

- `3fc36cff-74b6-a980-3e4c-8f93a1dae205.clothing`

- `40b92916-8055-2562-008f-58924bd0e03c.gesture`

- `41426836-7437-7e89-025d-0aa4d10f1d69.animatn`

- `42b46214-4b44-79ae-deb8-0df61424ff4b.animatn`

- `42dd95d5-0bc6-6392-f650-777304946c0f.animatn`

- `42ecd00b-9947-a97c-400a-bbc9174c7aeb.animatn`

- `43417d10-a2f7-7727-6fd4-dd7f04ad7a13.gesture`

- `44a87e64-2d78-14b7-1cde-ac0f5031621f.gesture`

- `46bb4359-de38-4ed8-6a22-f1f52fe8f506.animatn`

- `47f5f6fb-22e5-ae44-f871-73aaaf4a6022.animatn`

- `49aea43b-5ac3-8a44-b595-96100af0beda.animatn`

- `4ae8016b-31b9-03bb-c401-b1ea941db41d.animatn`

- `4bd69a1d-1114-a0b4-625f-84e0a5237155.animatn`

- `4c450f9e-07c0-2f5a-bc89-57de56db8ba1.gesture`

- `4f23cc4a-712e-aabc-afcf-3cab4c1164ea.gesture`

- `510cdb99-1764-a0ef-a7e7-beb70e8dc4a4.clothing`

- `514af488-9051-044a-b3fc-d4dbf76377c6.animatn`

- `51f3b303-a783-f0bd-9e98-9c094be13653.bodypart`

- `522d4d1d-0f75-c3e7-af30-990e5f394438.gesture`

- `52d9684f-2dcf-c252-2360-186b4236d07e.gesture`

- `5480a924-8b06-9551-2af7-bf59452870e5.gesture`

- `55c19b40-5303-d6ab-f003-5a2d926f4738.bodypart`

- `56e0ba0d-4a9f-7f27-6117-32f2ebbf6135.animatn`

- `5725fae1-0087-ec20-a4a0-eaa82d5c121b.bodypart`

- `5747a48e-073e-c331-f6f3-7c2149613d3e.animatn`

- `57abaae6-1d17-7b1b-5f98-6d11a6411276.animatn`

- `57cbd4f1-c53e-020f-f455-5ad2a5bab98d.bodypart`

- `590b2eac-a9fc-1e22-7874-782e3ded97d2.bodypart`

- `59332ea5-2a75-9ede-9ab7-f0ae70bbffcc.clothing`

- `5a68100b-e6ba-5170-649c-80beddc67035.gesture`

- `5a977ed9-7f72-44e9-4c4c-6e913df8ae74.animatn`

- `5af7de1f-e517-ae9a-13d8-4760c1ab4cc3.bodypart`

- `5bac881c-fff8-b19a-49eb-ba253eb5af04.bodypart`

- `5c682a95-6da4-a463-0bf6-0f5b7be129d1.animatn`

- `5dde08b6-59ec-5ca3-92a0-b9d7f532a768.bodypart`

- `5ea3991f-c293-392e-6860-91dfa01278a3.animatn`

- `6061a81b-e6bf-5909-b86a-268e5c6b28c3.clothing`

- `6212ffdd-d447-a92f-18f3-8cb94a799d83.gesture`

- `62c5de58-cb33-5743-3d07-9e4cd4352864.animatn`

- `631feb23-6f72-ae9c-dd5e-51510bbe235b.clothing`

- `633b2da6-a46f-8de8-5fe6-1256fd48d991.bodypart`

- `63af4bbd-7dba-fb00-01f6-bc2126ece403.gesture`

- `666307d9-a860-572d-6fd4-c3ab8865c094.animatn`

- `66d174a6-66dc-cfe4-5b51-48b3be18d099.clothing`

- `66ecd9bd-22e1-2633-f41e-ad1a38205662.gesture`

- `6802d553-49da-0778-9f85-1599a2266526.animatn`

- `6883a61a-b27b-5914-a61e-dda118a9ee2c.animatn`

- `68efa755-f0dd-8da2-38e9-bc9ea6b4ddd6.gesture`

- `693f12af-3bd9-8dcd-0395-32a967cc812d.bodypart`

- `697ed804-815c-f195-597c-dce51b86713b.bodypart`

- `69a2052e-1777-df94-49bd-8675ca576d87.clothing`

- `6af61452-5a3b-7fd3-4604-dc397aa9184b.bodypart`

- `6b61c8e8-4747-0d75-12d7-e49ff207a4ca.animatn`

- `6bd01860-4ebd-127a-bb3d-d1427e8e0c42.animatn`

- `6ed24bd8-91aa-4b12-ccc7-c97c857ab4e0.animatn`

- `709ea28e-1573-c023-8bf8-520c8bc637fa.animatn`

- `70ea714f-3a97-d742-1b01-590a8fcd1db5.animatn`

- `72560c27-e48b-a6a5-10e3-d21dfb4bd4fb.clothing`

- `7693f268-06c7-ea71-fa21-2b30d6533f8f.animatn`

- `76d30ee1-c369-12ec-8dbc-9cf2f51120ff.gesture`

- `76f7ced2-4f91-31c8-ff7d-e76b19abfa40.gesture`

- `7700f429-88f0-7e57-7714-33c73ad1a4eb.clothing`

- `7705007b-f459-0b49-e8f3-dd4eff6f82c2.bodypart`

- `790d7d90-eba9-d269-2d38-5cd2e36e7b93.clothing`

- `792c8d21-c931-31be-0319-1779a0f8caf4.bodypart`

- `7a17b059-12b2-41b1-570a-186368b6aa6f.animatn`

- `7a4e87fe-de39-6fcb-6223-024b00893244.animatn`

- `7db00ccd-f380-f3ee-439d-61968ec69c8a.animatn`

- `7fa32e57-0b88-d0f5-37b5-65ddf513e341.clothing`

- `80700431-74ec-a008-14f8-77575e73693f.animatn`

- `81287180-509d-477c-b10d-d68e403d5bcb.clothing`

- `815c3d49-d7fa-0214-3053-8eb9e63fda4c.gesture`

- `8175bd9f-ac1a-39e6-7cc6-93ab762f49bc.clothing`

- `82e99230-c906-1403-4d9c-3889dd98daba.animatn`

- `83bf1baf-6fdc-9906-9ab7-3113a3728136.bodypart`

- `83ff59fe-2346-f236-9009-4e3608af64c1.animatn`

- `85428680-6bf9-3e64-b489-6f81087c24bd.animatn`

- `85995026-eade-5d78-d364-94a64512cb66.animatn`

- `865c5fe0-aafb-671a-8ad5-778beb24b6f8.gesture`

- `869ecdad-a44b-671e-3266-56aef2e3ac2e.animatn`

- `8868cfa3-5b82-97ab-dc38-ded906f7fd90.gesture`

- `8ac9b0b4-9409-383a-1339-5373895f5368.bodypart`

- `8b102617-bcba-037b-86c1-b76219f90c88.animatn`

- `8b753e16-bd7d-2bb3-7765-671b7b31e77c.gesture`

- `8ccf1744-1509-7537-0fb5-1d33d2eefaf8.bodypart`

- `8dbc8a59-18ec-c9c0-8edf-ddcb8a749e5f.gesture`

- `8ea9f72c-6e64-e6bf-34ed-2713f84db063.clothing`

- `90bdcd26-2c6b-44a7-aab2-18c5a04f3fc3.gesture`

- `90e38814-7029-18a2-70ea-346ca73569aa.bodypart`

- `92624d3e-1068-f1aa-a5ec-8244585193ed.animatn`

- `928cae18-e31d-76fd-9cc9-2f55160ff818.animatn`

- `944890c6-1960-b1a7-f50a-c05651720d7e.bodypart`

- `94669140-c63b-8805-5561-62f5e24206ea.bodypart`

- `951469f4-c7b2-c818-9dee-ad7eea8c30b7.animatn`

- `9583adac-bc9b-a021-ab8f-26018db46ab5.gesture`

- `97c5742d-1d74-9408-2bae-9738a9e9d084.gesture`

- `9b0c1c4e-8ac7-7969-1494-28c874c4f668.animatn`

- `9b29cd61-c45b-5689-ded2-91756b8d76a9.animatn`

- `9b37423a-caf6-3bb6-f4e8-60a11ccee1af.bodypart`

- `9ba1c942-08be-e43a-fb29-16ad440efc50.animatn`

- `9cde58a2-05ba-5c21-5c90-b76079185990.clothing`

- `9e439264-0a7b-9190-d128-995092499c28.gesture`

- `9f496bd2-589a-709f-16cc-69bf7df1d36c.animatn`

- `a00917ca-047d-a3ea-d246-63265f904a6e.bodypart`

- `a166cdc3-ea15-0c01-ca5b-d3fed6e3ca75.gesture`

- `a41965be-10f2-1625-df3b-2fe35716998b.gesture`

- `a53d49ad-d705-dd1b-318e-4d1cf3c04a11.gesture`

- `a54d8ee2-28bb-80a9-7f0c-7afbbe24a5d6.animatn`

- `a6a09cb1-0845-5ec0-051e-16bb79b30ddf.gesture`

- `a8dee56f-2eae-9e7a-05a2-6fb92b97e21e.animatn`

- `a8dee7f6-a796-12a0-91bd-abf2fff300cc.clothing`

- `a94ef3a0-7119-67b6-67e0-d93d5b08a544.gesture`

- `aa134404-7dac-7aca-2cba-435f9db875ca.animatn`

- `aa9d6d53-2647-f731-97eb-e07a47febb57.bodypart`

- `abe169ff-ee4d-0e22-aa03-19b8116fdd7a.clothing`

- `aca78492-0487-03ec-4eb5-5c8e76c837e1.gesture`

- `ad22cda1-00c1-21cc-2f35-9ea5b8636f9e.gesture`

- `ad4e858f-08a7-e67a-4d55-b0fc18b2518b.clothing`

- `ad88e068-dc0a-6ef2-5a97-929ad01d883b.gesture`

- `aec4610c-757f-bc4e-c092-c6e9caf18daf.animatn`

- `af2b8320-e579-2c41-b717-969759aeb3ca.gesture`

- `afb80807-4214-7f3c-55b8-00858f56d37a.gesture`

- `afd64d9d-572d-b4f1-69bc-a79f70768177.gesture`

- `b0dc417c-1f11-af36-2e80-7e7489fa7cdc.animatn`

- `b1709c8d-ecd3-54a1-4f28-d55ac0840782.animatn`

- `b1dc34e2-c8fb-3885-3a7e-10be1d5589dd.clothing`

- `b1ed7982-c68e-a982-7561-52a88a5298c0.animatn`

- `b312b10e-65ab-a0a4-8b3c-1326ea8e3ed9.animatn`

- `b57c996d-cb06-43c8-749d-e9ce361f172e.gesture`

- `b5b4a67d-0aee-30d2-72cd-77b333e932ef.animatn`

- `b5ea617e-47cf-612b-2d99-8c6f6dcac218.gesture`

- `b606cdd6-4c22-6cc0-4614-560e6b9beeba.clothing`

- `b68a3d7c-de9e-fc87-eec8-543d787e5b0d.animatn`

- `b6e66a0e-f8db-0d4b-9259-7e9b20562b73.bodypart`

- `b6f560d1-e2ad-24df-344c-2943c47a6775.gesture`

- `b8c8b2a3-9008-1771-3bfc-90924955ab2d.animatn`

- `b8de1c20-7eba-2101-f2e3-9ed132838dcc.bodypart`

- `b906c4ba-703b-1940-32a3-0c7f7d791510.animatn`

- `ba38eeb2-d35f-0a07-0c04-0eb42fcc6010.gesture`

- `bacd48be-6733-7842-dd1f-8802e920f3ba.bodypart`

- `bc2ff144-9a36-fdd0-316d-d86f5c9a43ac.gesture`

- `bd07ffa9-426c-69da-d27a-e54e4ebbc73c.bodypart`

- `be969774-2a2b-0534-daee-f69357ff4adf.clothing`

- `c0c4030f-c02b-49de-24ba-2331f43fe41c.animatn`

- `c1a68df8-3a01-4f17-0bab-10eb7df9c22a.clothing`

- `c1bc7f36-3ba0-d844-f93c-93be945d644f.animatn`

- `c272cb94-0081-49bb-d45e-aeda288b3c06.clothing`

- `c437fefd-6025-fd89-e65c-aec2732f3007.clothing`

- `c4ca6188-9127-4f31-0158-23c4e2f93304.animatn`

- `c4d1b050-1784-feb4-474f-ec3b1f1a29cb.clothing`

- `c521ad1f-06f0-8711-f313-5737a38f0d78.clothing`

- `c541c47f-e0c0-058b-ad1a-d6ae3a4584d9.animatn`

- `c5d0cab3-4a69-2f35-71ee-6dba0ce0c85c.bodypart`

- `c63ac707-6325-14c8-d681-54b81d0dff77.gesture`

- `c8d70bed-535b-3d97-5d17-6136a209fbe6.bodypart`

- `c8e42d32-7310-6906-c903-cab5d4a34656.animatn`

- `ca5b3f14-3194-7a2b-c894-aa699b718d1f.animatn`

- `cd28b69b-9c95-bb78-3f94-8d605ff1bb12.animatn`

- `cd55f18e-c1bf-70a5-5b53-a114fdc44930.bodypart`

- `cd7668a6-7011-d7e2-ead8-fc69eff1a104.animatn`

- `ce58f877-251f-b025-9227-4be3456faf58.bodypart`

- `cf03c095-647e-bd96-4ce2-63202cd5a171.clothing`

- `d08d1a27-9410-dbd7-cc4f-ae1a8837b49d.bodypart`

- `d1b530a9-b4c8-aeaf-9300-9b9d30c715d1.clothing`

- `d26fbcbc-1985-92ef-0cf0-7148b7ed0c08.gesture`

- `d2f2ee58-8ad1-06c9-d8d3-3827ba31567a.animatn`

- `d40491cc-3629-a090-d11f-ee947d9125a8.bodypart`

- `d53b27ad-73b9-8ea4-0896-7890b57dd8ed.clothing`

- `d60c41d2-7c24-7074-d3fa-6101cea22a51.animatn`

- `d6c00693-90e0-cbbd-cd3d-3a6ccd510f14.clothing`

- `d83fa0e5-97ed-7eb2-e798-7bd006215cb4.animatn`

- `d918a0d8-7291-ce83-762f-3f68dcc7402d.gesture`

- `d973aaf2-ff8d-3b05-8c81-48305210b3bf.clothing`

- `db84829b-462c-ee83-1e27-9bbee66bd624.animatn`

- `dbd054f1-132b-cc22-e46a-bad83c230c91.gesture`

- `ddcd68c1-0cb9-4b32-a475-f2b9b96ec8d5.clothing`

- `df074f93-968a-2588-8ef5-7db3b21dff6d.bodypart`

- `e04d450d-fdb5-0432-fd68-818aaf5935f8.animatn`

- `e2efe57f-70e8-35e5-b92c-280e3e9c6e1f.clothing`

- `e4485e5d-6bcc-e5ca-96fd-303227e93d6c.gesture`

- `e5c8f3c2-9e65-5c4b-03c4-d8205f626b37.bodypart`

- `e7135c15-a7bc-637e-2664-b6fbdc22428c.gesture`

- `e7263f17-46cf-5deb-7e5a-ecc0776f5241.clothing`

- `e7584536-86f2-c962-405d-d14adff71f38.gesture`

- `ea633413-8006-180a-c3ba-96dd1d756720.animatn`

- `ea9ab69b-c2c7-3e18-a50b-37a9cfe457cd.gesture`

- `eae8905b-271a-99e2-4c0e-31106afd100c.animatn`

- `ec952cca-61ef-aa3b-2789-4d1344f016de.animatn`

- `eefc79be-daae-a239-8c04-890f5d23654a.animatn`

- `ef62d355-c815-4816-2474-b1acc21094a6.animatn`

- `efdc1727-8b8a-c800-4077-975fc27ee2f2.animatn`

- `f061723d-0a18-754f-66ee-29a44795a32f.animatn`

- `f22fed8b-a5ed-2c93-64d5-bdd8b93c889f.animatn`

- `f2483d55-bc31-38c0-65b2-9f7e87fce5c4.gesture`

- `f2bed5f9-9d44-39af-b0cd-257b2a17fe40.animatn`

- `f3061aa3-0069-96b4-67b5-e16633a2ef30.clothing`

- `f3300ad9-3462-1d07-2044-0fef80062da0.animatn`

- `f4714624-bdc5-f596-5c6f-789b438becf9.bodypart`

- `f4f00d6e-b9fe-9292-f4cb-0ae06ea58d57.animatn`

- `f5fc7433-043d-e819-8298-f519a119b688.animatn`

- `f67a2a68-6c1d-6fc0-29fd-7ec01c0b5946.bodypart`

- `f76e4009-1b0f-125f-1d81-e3d774f4a838.bodypart`

- `f868fcfc-1377-396a-1635-4ac71a58a4fc.bodypart`

- `fa743da9-7e6e-d88e-3e4f-143dcb4fc01b.gesture`

- `fb262981-4295-f048-c280-629081bf3b6b.gesture`

- `fc3de4b8-bd3e-662b-934c-b72714dab5bf.gesture`

- `fd037134-85d4-f241-72c6-4f42164fedee.animatn`

- `fe63b3df-0557-c6fe-836a-a353f8108660.bodypart`

- `ff1114e1-4063-3abe-de2f-6d13f6cae508.gesture`

- `ff201a24-6893-4c41-77f2-bf707481e585.gesture`


## indra/newview/app_settings/windlight/ (1 files)

- `postprocesseffects.xml`


## indra/newview/app_settings/windlight/days/ (18 files)

- `%28SS%29%20Atmos%206.xml`

- `%28SS%29%20Atmospheric%20Daycycle%20Clear.xml`

- `%28SS%29%20Atmospheric%20Daycycle%20Cloudy.xml`

- `%28SS%29%20Atmospheric%20Daycycle%20Cloudy2.xml`

- `%5BNB%5D%20Aftermath.xml`

- `%5BNB%5D%20P-Haze.xml`

- `%5BNB%5D%20Sepia.xml`

- `%5BNB%5D-MistyDay.xml`

- `Anime%20Daze.xml`

- `Colder%20Tones.xml`

- `Default.xml`

- `Dynamic%20Richness.xml`

- `FALLOUT%20SL%201.0.xml`

- `Hyborian%20Coast.xml`

- `Pirate%27s%20Dream.xml`

- `Psycho%20Strobe%21.xml`

- `Tropicalia.xml`

- `Weird-O.xml`


## indra/newview/app_settings/windlight/skies/ (769 files)

- `%28SS%29%20Atmos%2000%3A00%202.xml`

- `%28SS%29%20Atmos%2001%3A00%201.xml`

- `%28SS%29%20Atmos%2002%3A00%202.xml`

- `%28SS%29%20Atmos%2004%3A00%201.xml`

- `%28SS%29%20Atmos%2006%3A00%201.xml`

- `%28SS%29%20Atmos%2007%3A00%201.xml`

- `%28SS%29%20Atmos%2008%3A00%201.xml`

- `%28SS%29%20Atmos%2012%3A00%201.xml`

- `%28SS%29%20Atmos%2013%3A00%201.xml`

- `%28SS%29%20Atmos%2014%3A00%201.xml`

- `%28SS%29%20Atmos%2015%3A00%201.xml`

- `%28SS%29%20Atmos%2016%3A00%201.xml`

- `%28SS%29%20Atmos%2017%3A00%201.xml`

- `%28SS%29%20Atmos%2018%3A00%201.xml`

- `%28SS%29%20Atmos%2019%3A00%201.xml`

- `%28SS%29%20Atmos%2020%3A00%201.xml`

- `%28SS%29%20Atmos%2023%2E30%202.xml`

- `%28SS%29%20Atmospheric%2000%3A00b.xml`

- `%28SS%29%20Atmospheric%2000%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2000%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2004%3A00b.xml`

- `%28SS%29%20Atmospheric%2004%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2004%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2006%3A00%206b.xml`

- `%28SS%29%20Atmospheric%2006%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2006%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2007%3A00b.xml`

- `%28SS%29%20Atmospheric%2007%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2007%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2008%3A00b.xml`

- `%28SS%29%20Atmospheric%2008%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2008%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2012%3A00%20midday6b.xml`

- `%28SS%29%20Atmospheric%2012%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2012%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2013%3A00b.xml`

- `%28SS%29%20Atmospheric%2013%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2013%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2014%3A00b.xml`

- `%28SS%29%20Atmospheric%2014%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2014%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2015%3A00b.xml`

- `%28SS%29%20Atmospheric%2015%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2015%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2016%3A00b.xml`

- `%28SS%29%20Atmospheric%2016%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2016%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2017%3A00b.xml`

- `%28SS%29%20Atmospheric%2017%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2017%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2018%3A00b.xml`

- `%28SS%29%20Atmospheric%2018%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2018%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2019%3A00b.xml`

- `%28SS%29%20Atmospheric%2019%3A00cloudy.xml`

- `%28SS%29%20Atmospheric%2019%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric%2020%3A00b.xml`

- `%28SS%29%20Atmospheric%2020%3A00cloudy2.xml`

- `%28SS%29%20Atmospheric20%3A00cloudy.xml`

- `%2ACanimod.xml`

- `%2AStarley%2A%20Settings%202.xml`

- `%5BAnaLu%5D%20AvatarOpt%20%28Caliah%29%20whiter.xml`

- `%5BAnaLu%5D%20AvatarOpt%20%28Caliah%29.xml`

- `%5BAnaLu%5D%20Studio%20Light%20%28Gillian%29.xml`

- `%5BAnaLu%5D%20default1.xml`

- `%5BAnaLu%5D%20default2.xml`

- `%5BAnaLu%5D%20default3.xml`

- `%5BAnaLu%5D%20neutral.xml`

- `%5BAnaLu%5D%20outdoor%20city%20weirdlights.xml`

- `%5BAnaLu%5D%20outdoor%20city.xml`

- `%5BAnaLu%5D%20outdoor%20night.xml`

- `%5BAnaLu%5D%20shadows.xml`

- `%5BAnaLu%5D%20studio1.xml`

- `%5BAnaLu%5D%20studio2.xml`

- `%5BAnaLu%5D%20studio3.xml`

- `%5BAnaLu%5D%20studio4.xml`

- `%5BAnaLu%5D%20studio5.xml`

- `%5BAnaLu%5D%20studio6.xml`

- `%5BAnaLu%5D%20studio7.xml`

- `%5BAnaLu%5D%20studio8.xml`

- `%5BAnaLu%5D%20studio9.xml`

- `%5BCB%5D%20Rouge%201.xml`

- `%5BCB%5D%20Rouge%202.xml`

- `%5BCB%5D%20Rouge%203.xml`

- `%5BCB%5D%20Rouge%204.xml`

- `%5BCB%5D%20Rouge%205.xml`

- `%5BCB%5D%20Rouge%206.xml`

- `%5BEUPHORIA%5D%20Plum%20sunset.xml`

- `%5BEUPHORIA%5D%20air%20pollution%202.xml`

- `%5BEUPHORIA%5D%20bergamot%20%26%20rosemary.xml`

- `%5BEUPHORIA%5D%20day%20of%20the%20end.xml`

- `%5BEUPHORIA%5D%20fin%20de%20siecle.xml`

- `%5BEUPHORIA%5D%20hello%20gaia.xml`

- `%5BEUPHORIA%5D%20low%20saturation%20dull%20deposit.xml`

- `%5BEUPHORIA%5D%20monochrome.xml`

- `%5BEUPHORIA%5D%20natural%20high.xml`

- `%5BEUPHORIA%5D%20realm.xml`

- `%5BEUPHORIA%5D%20rotten%20melon.xml`

- `%5BEUPHORIA%5D%20sleep%20warm.xml`

- `%5BEUPHORIA%5D%20smoky%20blue%20sky%20%3A%20reverse.xml`

- `%5BEUPHORIA%5D%20smoky%20blue%20sky.xml`

- `%5BEUPHORIA%5D%20sunset%201.xml`

- `%5BEUPHORIA%5D%20sunset%202.xml`

- `%5BEUPHORIA%5D%20that%20day.xml`

- `%5BEUPHORIA%7D%20air%20pollution%201.xml`

- `%5BNB%5D%20Aftermath%200000.xml`

- `%5BNB%5D%20Aftermath%200500.xml`

- `%5BNB%5D%20Aftermath%201200.xml`

- `%5BNB%5D%20Aftermath%201630.xml`

- `%5BNB%5D%20Aftermath%201750.xml`

- `%5BNB%5D%20Aftermath%202000.xml`

- `%5BNB%5D%20Alpine%2Dskinlight%20RGB.xml`

- `%5BNB%5D%20P%2DHaze%200000.xml`

- `%5BNB%5D%20P%2DHaze%200430.xml`

- `%5BNB%5D%20P%2DHaze%200800.xml`

- `%5BNB%5D%20P%2DHaze%201200.xml`

- `%5BNB%5D%20P%2DHaze%201700.xml`

- `%5BNB%5D%20P%2DHaze%201800.xml`

- `%5BNB%5D%20P%2DHaze%201900.xml`

- `%5BNB%5D%20P%2DHaze%202000.xml`

- `%5BNB%5D%20Sepia%200000.xml`

- `%5BNB%5D%20Sepia%200430.xml`

- `%5BNB%5D%20Sepia%200800.xml`

- `%5BNB%5D%20Sepia%201200.xml`

- `%5BNB%5D%20Sepia%201700.xml`

- `%5BNB%5D%20Sepia%201800.xml`

- `%5BNB%5D%20Sepia%202000.xml`

- `%5BNB%5D%2DMistyDay%2D12am.xml`

- `%5BNB%5D%2DMistyDay%2D12pm.xml`

- `%5BNB%5D%2DMistyDay%2D4am.xml`

- `%5BNB%5D%2DMistyDay%2D4pm.xml`

- `%5BNB%5D%2DMistyDay%2D5am.xml`

- `%5BNB%5D%2DMistyDay%2D5pm.xml`

- `%5BNB%5D%2DMistyDay%2D6am.xml`

- `%5BNB%5D%2DMistyDay%2D6pm.xml`

- `%5BNB%5D%2DMistyDay%2D7pm.xml`

- `%5BNB%5D%2DMistyDay%2D8am.xml`

- `%5BNB%5D%2DMistyDay%2D9pm.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Awwyeah.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Eats%20night.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Good%20for%20marriage.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Good%20for%20warm%20sailing.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Impires.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Raylanta.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Safarion.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Slastlevania.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Slips%20through%20walls%201.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Slips%20through%20walls%202.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Slips%20through%20walls%203.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Slips%20through%20walls%204.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Slips%20through%20walls%205.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Slips%20through%20walls%206.xml`

- `%5BTOR%5D%20BIG%20SUN%20%2D%20Variationz.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Apts.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Beachin%27.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Blue%20hour.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Briony.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Burnt%20hope.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Fairytale%20glow.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Patriotix.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Sepia%27ed.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Siennarel.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Smolder.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Somber%20rose.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Strummer.xml`

- `%5BTOR%5D%20DUSK%20%2D%20Vision%20of%20something.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Catastrophe.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Chouchou%20rockets.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Das%20fog.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Fogvari.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Golden%20glow.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Lollitudes.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Melon%20chapterhouse.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Mint%20teahouse.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Peach%20Peche.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Rose%2Dtinted.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Sad%20purple.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Silent%20heck.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Southern%20delite.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20Terpsa%20bonne.xml`

- `%5BTOR%5D%20FOGGY%20%2D%20The%20pink%20tower.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Asian%20red.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Bloody%20moon.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Castle%20vain.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Commie%20skies.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Darkside%20tales.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Dawnbreaker.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Dullard.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Evil%20machinery.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Land%20of%20rising.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Monochrome%20redflog.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Namob%20islet.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Profondo%20rosso.xml`

- `%5BTOR%5D%20HORROR%20%2D%20Rancid%20milk.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20An%20incongruent%20truth.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Anime%20Ciel.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Azure%20desertation.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Baskaholic.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Beachin%27.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Character.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Cheery%20cyan.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Coral%20reef.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Herr%20Gracken.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Londonisk.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Maldives.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Morally%20satisfied.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20My%20noon.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Nostalgika.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Pleasantrie.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Precision%20blue.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Quiet%20confidence.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Rebranded%20skies.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Salmon.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Touch%20o%27%20purple.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Vintage%20Village.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Why%20so%20blue%3F%201.xml`

- `%5BTOR%5D%20MIDDAY%20%2D%20Why%20so%20blue%3F%202.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Anwar.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Bright%20blue%20horizon.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Brighter.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Dark%20came%20over.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Faux%20moon.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Flyer.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Mighty%20moon.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Moony.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Nocturne.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Our%20together.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20That%20spells%20moon%201.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20That%20spells%20moon%202.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20That%20spells%20moon%203.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20That%20spells%20moon%204.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Twilight%20rider.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Under%20a%20yellow%20moon.xml`

- `%5BTOR%5D%20NIGHT%20%2D%20Wuxia.xml`

- `%5BTOR%5D%20NIGHT%2D%20Northern%20lite.xml`

- `%5BTOR%5D%20SCIFI%20%2D%202012.xml`

- `%5BTOR%5D%20SCIFI%20%2D%202013.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Albedo%200%2E39.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Alien%20planet.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Arid%20nestler.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Arrakissed%201.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Arrakissed%202.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Awesome%20atmo%201.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Awesome%20atmo%202.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Awesome%20atmo%203.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Awesome%20atmo%204.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Beautiful%20again.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Big%20pink.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Blue%20highline.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Blue%20skies%20LOL.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Blue%20sun%20warmed.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Bridge%20opera%201.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Bridge%20opera%202.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20CGAtrope.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Chinese%20legacy.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Climacontrasty.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Conciergist.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Cragelica.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Cranched.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Eno%20would%20be%20proud.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Evocrads%27lime.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Fog%20mystic%201.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Fog%20mystic%202.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Gelatto.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Gelding%20morose.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Gimler%20gronchi.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Golden.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Green%20whirl.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Grit%20%26%20shame.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Hong%20Kong%20planet.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Kelf%20shelf.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Lilack.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Lords%20of%20Barsoom.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Lunar%20kuwang.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Lydian%20dinosaurs.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Martian%20meat.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Metal%20Gear%20Solid.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Military%20camo.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Moon%20goons.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Morphirizon.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20New%20romantic.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Non%2Dgeneric%20fantasy.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Noxumic.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Orange%20balm.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Oyster%20Bay.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Phlogiston.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Planet%20Xmas.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Polaron%20charge%201.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Polaron%20charge%202.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Port%20skies.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Purple%20wisps%20%26%20egg%20yolk.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Railingz%201.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Railingz%202.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Rainbowtek.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Ramshagguld%201.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Ramshagguld%202.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Rezzable%20Hallucinogen.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Rimmerthal.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Sailor%20moon.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Scanning%20aliens.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Shilarto.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Shine%20on%20my%20friends.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Sky%20as%20canvas.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Sparz%20puft.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Spiceflow.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Stay%20stonkin%27.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Suppression%20band.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Teak%20weak.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20This%20alien%20life.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Touchness.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Un%20Peinture.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Unorthodox%20happy.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Use%20on%20fine%20ships.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Watermelon%2Dish.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Whirld%20spinnin.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Wild%20Palms.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Yo%20pirates%21.xml`

- `%5BTOR%5D%20SCIFI%20%2D%20Yolka%20loka.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Blacklight.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Dreamwalker.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Green%20highlighter.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Heaven.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Light%20thru%20veins.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Posture%20eyes.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Puur.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Rightvision.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Threshold.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Use%20with%20full%20bright.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20Watermelon.xml`

- `%5BTOR%5D%20SPECIAL%20%2D%20What%20I%20am%20thinking.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Across%20process.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Asiatix.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Baffin.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Barcelon%201.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Barcelon%202.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Breaking%20firmament.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Brillianter%20sunrise.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Bubble%20sun%20severance.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Canyon%20dreams%20red.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Canyon%20dreams.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Chernoble.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Clouds%20indifferent.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Coastal%201.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Coastal%202.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Coastal%203.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Cobraring%201.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Cobraring%202.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Deep%20blue%20sky%202.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Defenderz%201.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Defenderz%202.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Desert.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Eye%20of%20Mowron.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Farmatronic%20sepia.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Fine%20Scottish%20day.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Frenlite.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Hot.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Island%20cusp.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Lemon%2Dpeach%20smoothie.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Liz%20gluft.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Lonely%20cyberpunks.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Moon%20berries.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Teaching.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Tortoise%20isle.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Turtle%20island.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Tusken.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Twisted%20pixels.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Ultimate%21.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20We%27re%20so%20vane.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Whisked.xml`

- `%5BTOR%5D%20SUNRISE%20%2D%20Wonderzan.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Azure%20desertation%202.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Bangko%201.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Bangko%202.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Blue%20inspiration.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Brouhatta%20charme.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Buccaneers%20of%20the%20coast.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Camp%20champ.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Damage%20down.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Desert.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Early%20warning.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Eggdrop.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Endgame.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Garrigal%20moscheles%201.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Garrigal%20moscheles%202.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Holy%20romance.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Ivory%20flowers.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Kyrosonatine.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Langnun.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Malts.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Ominox.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Oriental%20delight%201.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Oriental%20delight%202.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Pale%20incabon.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Pevensie.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Pink%20sink.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Pinker.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Ravenelle%27s%20choice.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Red%20city.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Silhouetta.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Stark%20epiphany.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Study%20vessels.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Vacation.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Vehicle%20Sandbox.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Verdancy.xml`

- `%5BTOR%5D%20SUNSET%20%2D%20Warmer.xml`

- `80%27s%20Wave.xml`

- `A%2D12AM.xml`

- `A%2D12PM.xml`

- `A%2D3AM.xml`

- `A%2D3PM.xml`

- `A%2D6AM.xml`

- `A%2D6PM.xml`

- `A%2D9AM.xml`

- `A%2D9PM.xml`

- `AM%20Radio%27s%20Nostalgia.xml`

- `Alchemy%20Immortalis%20%2D%20Dark%20Misty%20Night.xml`

- `Alchemy%20Immortalis%20%2D%20Fog%20Lifting.xml`

- `Alchemy%20Immortalis%20%2D%20Foggy%20Morning.xml`

- `Ambient%20Dark.xml`

- `Ambient%20Grey.xml`

- `Ambient%20White.xml`

- `AnaLu%20%2Astudio%2A%205.xml`

- `AnaLu%20%2D%20outdoor%20city%20night.xml`

- `AnaLu%20%2D%20outdoor%20city.xml`

- `AnaLu%20%2D%20outdoor%20night.xml`

- `AnaLutetia%20%2D%20AvatarOpt.xml`

- `AnaLutetia%20%2D%20AvatarOpt2%20whiter.xml`

- `AnaLutetia%20%2D%20STUDIO2.xml`

- `AnaLutetia%20%2D%20STUDIO3.xml`

- `AnaLutetia%20%2D%20Studio%20Light.xml`

- `AnaLutetia%20%2D%20outdoor.xml`

- `AnaLutetia%2Ddefault.xml`

- `AnaLutetia%2Doutdoor2.xml`

- `AnaLutetia%2Dstudio.xml`

- `AnaLutetia.xml`

- `Anime%20%2D%2012AM.xml`

- `Anime%20%2D%2012PM.xml`

- `Anime%20%2D%203AM.xml`

- `Anime%20%2D%203PM.xml`

- `Anime%20%2D%205%3A30AM.xml`

- `Anime%20%2D%206%3A30AM.xml`

- `Anime%20%2D%206%3A30PM.xml`

- `Anime%20%2D%206AM.xml`

- `Anime%20%2D%206PM.xml`

- `Anime%20%2D%209AM.xml`

- `Anime%20%2D%209PM.xml`

- `Annan%20Adored%20Dark%20Red%20sky.xml`

- `Annan%20Adored%20Darkness.xml`

- `Annan%20Adored%20Dusty.xml`

- `Annan%20Adored%20Light%20Explosion%20II.xml`

- `Annan%20Adored%20Light%20Explosion%20III.xml`

- `Annan%20Adored%20Light%20Explosion.xml`

- `Annan%20Adored%20Optimal%20Skin%20%28no%20shadows%29.xml`

- `Annan%20Adored%20Realistic%20ambient.xml`

- `Annan%20Adored%20Red%20moments.xml`

- `Annan%20Adored%20Tan%20Skin.xml`

- `Annyka%27s%20Soft%20Lavender%20Day.xml`

- `AvatarOpt.xml`

- `B5%2DShadowDancing.xml`

- `Barcelona.xml`

- `Blizzard.xml`

- `Blue%20Midday.xml`

- `Bree%27s%20appleblossom.xml`

- `Bright2.xml`

- `Bristol.xml`

- `Bryn%20Oh%27s%20Annas%20Many%20Murders.xml`

- `Bryn%20Oh%27s%20BLUNIVERSE.xml`

- `Bryn%20Oh%27s%20BOX%20MetaLES.xml`

- `Bryn%20Oh%27s%20Condos%20in%20Heaven%20sky%20%232.xml`

- `Bryn%20Oh%27s%20Condos%20in%20Heaven%20sky.xml`

- `Bryn%20Oh%27s%20Immersiva%20Grey%20Dust.xml`

- `Bryn%20Oh%27s%20Mayfly.xml`

- `Bryn%20Oh%27s%20Rusted%20Gears.xml`

- `Bryn%20Oh%27s%20Virginia%20Alone.xml`

- `CB%27s%20Rouge%201.xml`

- `CB%27s%20Rouge%202.xml`

- `CB%27s%20Rouge%203.xml`

- `CB%27s%20Rouge%204.xml`

- `CB%27s%20Rouge%205.xml`

- `CB%27s%20Rouge%206.xml`

- `CalWL.xml`

- `Coastal%20Afternoon.xml`

- `Coastal%20Sunset.xml`

- `Creepy%20Pyri.xml`

- `Daytime%20shadows.xml`

- `Default.xml`

- `Desert%20Sunset.xml`

- `Doomed%20Spaceship.xml`

- `Dusty.xml`

- `FALLOUT%20%2D%2012AM.xml`

- `FALLOUT%20%2D%2012PM.xml`

- `FALLOUT%20%2D%203AM.xml`

- `FALLOUT%20%2D%203PM.xml`

- `FALLOUT%20%2D%205AM.xml`

- `FALLOUT%20%2D%206AM.xml`

- `FALLOUT%20%2D%206PM.xml`

- `FALLOUT%20%2D%209AM.xml`

- `FALLOUT%20%2D%209PM.xml`

- `FSOriginal.xml`

- `Fairy%20blue%20%28Paulina%29.xml`

- `Fairy%20dark%20blue%20%28Paulina%29.xml`

- `Fairy%20light%20pink%20%28Paulina%29.xml`

- `Fairy%20warm%20pinks%20%28Paulina%29.xml`

- `Fine%20Day.xml`

- `Fluffy%20Big%20Clouds.xml`

- `Foggy.xml`

- `Free%27s%20Sunset.xml`

- `Funky%20Funky%20Funky.xml`

- `Funky%20Funky.xml`

- `Gelatto.xml`

- `Ghost.xml`

- `Glowing%20Sea.xml`

- `Gwen%27s%20Light.xml`

- `Hyborian%20Age%20%2D%20Water%20E%20%2D%20evening.xml`

- `Hyborian%20Age%20%2D%20Water%20E%20%2D%20morning.xml`

- `Hyborian%20Age%20%2D%20Water%20F%20%2D%20noon.xml`

- `Hyborian%20Dawn%20B%20%2D%20midnight.xml`

- `Incongruent%20Truths.xml`

- `Jean%27s%20Gothic%20Moon%2001.xml`

- `Jean%27s%20Gothic%20Moon%2002.xml`

- `Jean%27s%20Gothic%20Wasteland.xml`

- `Jean%27s%20Gothic%20Winter.xml`

- `London2026.xml`

- `London2050.xml`

- `Lunar%20Morning%207.xml`

- `Magic%20Hour.xml`

- `Maroon.xml`

- `Midday%201.xml`

- `Midday%202.xml`

- `Midday%203.xml`

- `Midday%204.xml`

- `Midday.xml`

- `Midnight.xml`

- `MorningGlory.xml`

- `Nacon%27s%20Afternoon.xml`

- `Nacon%27s%20Dawn.xml`

- `Nacon%27s%20Day%20Mood.xml`

- `Nacon%27s%20Day%20Mood2.xml`

- `Nacon%27s%20Fog.xml`

- `Nacon%27s%20Ghost.xml`

- `Nacon%27s%20Morning.xml`

- `Nacon%27s%20Morning2.xml`

- `Nacon%27s%20Natural%2010am.xml`

- `Nacon%27s%20Natural%204%3A30am.xml`

- `Nacon%27s%20Natural%205am%20END.xml`

- `Nacon%27s%20Natural%205am%20START.xml`

- `Nacon%27s%20Natural%205am.xml`

- `Nacon%27s%20Natural%207%3A30pm.xml`

- `Nacon%27s%20Natural%208%3A30am.xml`

- `Nacon%27s%20Natural%208am.xml`

- `Nacon%27s%20Natural%20Dark%20START.xml`

- `Nacon%27s%20Natural%20Midnight.xml`

- `Nacon%27s%20Natural%20Night.xml`

- `Nacon%27s%20Natural%20Noon.xml`

- `Nacon%27s%20Natural%20Sunrise%3A%20%2DA.xml`

- `Nacon%27s%20Natural%20Sunrise%3A%20A.xml`

- `Nacon%27s%20Natural%20Sunrise%3A%20B.xml`

- `Nacon%27s%20Natural%20Sunrise%3A%20C.xml`

- `Nacon%27s%20Natural%20Sunrise%3A%20D.xml`

- `Nacon%27s%20Natural%20Sunrise%3A%20E.xml`

- `Nacon%27s%20Natural%20Sunrise%3A%20F.xml`

- `Nacon%27s%20Natural%20Sunset%3A%20A.xml`

- `Nacon%27s%20Natural%20Sunset%3A%20B.xml`

- `Nacon%27s%20Natural%20Sunset%3A%20C.xml`

- `Nacon%27s%20Natural%20Sunset%3A%20D.xml`

- `Nacon%27s%20Nighty%20Fog.xml`

- `Nacon%27s%20O%2D6am.xml`

- `Nacon%27s%20Rise.xml`

- `Nacon%27s%20Rosy%20Morning.xml`

- `Nacon%27s%20Sweet%20Dawn.xml`

- `Nacon%27s%20Sweet%20Morning.xml`

- `Nacon%27s%20Test.xml`

- `Nam%27s%20Beach%20Scene.xml`

- `Nam%27s%20Optimal%20Skin%201.xml`

- `Nam%27s%20Optimal%20Skin%202.xml`

- `Nam%27s%20Optimal%20Skin%20and%20Prim.xml`

- `Nam%27s%20Robots%20of%20Dawn.xml`

- `Night.xml`

- `Oceane%27s%20Body%20Designs.xml`

- `Orac%20%2D%20Black%20fog%201.xml`

- `Orac%20%2D%20Black%20fog%202.xml`

- `Orac%20%2D%20Drawing%20blue.xml`

- `Orac%20%2D%20Drawing%20extreme.xml`

- `Orac%20%2D%20Drawing%20green.xml`

- `Orac%20%2D%20Drawing%20red.xml`

- `Orac%20%2D%20Drawing%20underground%20comic.xml`

- `Orac%20%2D%20fog.xml`

- `Orac%20%2D%20gray.xml`

- `Orac%20%2D%20green.xml`

- `Orange%20Incubus.xml`

- `PaperSnow.xml`

- `Phototools%2D%20Absinthe%20Light%20.xml`

- `Phototools%2D%20Andi%20Light%20.xml`

- `Phototools%2D%20Angles%20Light%2001.xml`

- `Phototools%2D%20B%2FW%20Light%20%2008.xml`

- `Phototools%2D%20B%2FW%20Light%2001.xml`

- `Phototools%2D%20B%2FW%20Light%2002.xml`

- `Phototools%2D%20B%2FW%20Light%2003.xml`

- `Phototools%2D%20B%2FW%20Light%2004.xml`

- `Phototools%2D%20B%2FW%20Light%2005.xml`

- `Phototools%2D%20B%2FW%20Light%2006.xml`

- `Phototools%2D%20B%2FW%20Light%2007.xml`

- `Phototools%2D%20B%2FW%20Light%2008.xml`

- `Phototools%2D%20B%2FW%20Light%2009.xml`

- `Phototools%2D%20B%2FW%20Light%2010.xml`

- `Phototools%2D%20B%2FW%20Light%2011.xml`

- `Phototools%2D%20B%2FW%20Light%2012.xml`

- `Phototools%2D%20B%2FW%20Light%2013.xml`

- `Phototools%2D%20Boken%20Lines%20Light%2001.xml`

- `Phototools%2D%20Breakwave%20Building%20Light.xml`

- `Phototools%2D%20Build%20002%20Light.xml`

- `Phototools%2D%20Build%20003%20Light.xml`

- `Phototools%2D%20Build%20005%20Light.xml`

- `Phototools%2D%20Build%20007%20Light.xml`

- `Phototools%2D%20Cafe%20Light%2001.xml`

- `Phototools%2D%20Calima%20Light%2001.xml`

- `Phototools%2D%20Charolotte%20Light.xml`

- `Phototools%2D%20Cloud%20Credit%20Light.xml`

- `Phototools%2D%20Cloud%20Light%2001.xml`

- `Phototools%2D%20Dead%20End%20Sky%2001.xml`

- `Phototools%2D%20Dorm%20Light%2001.xml`

- `Phototools%2D%20Dream%20Book%20Light%2001.xml`

- `Phototools%2D%20Dream%20Book%20Light%2002.xml`

- `Phototools%2D%20Dream%20Book%20Light%2003.xml`

- `Phototools%2D%20Dream%20Book%20Light%2004.xml`

- `Phototools%2D%20Epi%20Vintage%20Light.xml`

- `Phototools%2D%20Fashion%20Path%20Light%2001.xml`

- `Phototools%2D%20Got%20It%20Light%20.xml`

- `Phototools%2D%20Horizon%20Building%20Light%2001.xml`

- `Phototools%2D%20Horizon%20Building%20Light%2002.xml`

- `Phototools%2D%20Horizon%20Building%20Light.xml`

- `Phototools%2D%20Hospital%20Light%2001.xml`

- `Phototools%2D%20Hufflepuff%20Light%2001.xml`

- `Phototools%2D%20Hufflepuff%20Light%2002.xml`

- `Phototools%2D%20Hufflepuff%20Light%2003.xml`

- `Phototools%2D%20Jessica%20Light%2001.xml`

- `Phototools%2D%20Jessica%20Light%2002.xml`

- `Phototools%2D%20Jessica%20Light%2003.xml`

- `Phototools%2D%20Jessica%20Light%2004.xml`

- `Phototools%2D%20Jim%20Light%2001.xml`

- `Phototools%2D%20Jim%20Light%2002.xml`

- `Phototools%2D%20July%20Light%2001.xml`

- `Phototools%2D%20July%20Light%2002.xml`

- `Phototools%2D%20July%20Light%2003.xml`

- `Phototools%2D%20Landar%20Light%2001.xml`

- `Phototools%2D%20Lo%20%20Gun%20Light.xml`

- `Phototools%2D%20Lo%20Light%2001.xml`

- `Phototools%2D%20Lo%20Light%2002.xml`

- `Phototools%2D%20Lo%20Light%2003.xml`

- `Phototools%2D%20Lo%20Light%2004.xml`

- `Phototools%2D%20Lo%20Light%2005.xml`

- `Phototools%2D%20Lo%20Moves%20Light.xml`

- `Phototools%2D%20Lo%20Music%20Light%2001.xml`

- `Phototools%2D%20Mavi%20Light%2001.xml`

- `Phototools%2D%20Mavi%20Light%2002.xml`

- `Phototools%2D%20Mavi%20Light%2003.xml`

- `Phototools%2D%20Me%20Love%20Light.xml`

- `Phototools%2D%20Me%20Mine%20Light.xml`

- `Phototools%2D%20Meni%20Light%2001.xml`

- `Phototools%2D%20Miaa%20light%2001.xml`

- `Phototools%2D%20Moon%20Light%2001.xml`

- `Phototools%2D%20Moon%20Light%2002.xml`

- `Phototools%2D%20Moon%20Light%2003.xml`

- `Phototools%2D%20Moon%20Light%2004.xml`

- `Phototools%2D%20Moon%20Light%2005.xml`

- `Phototools%2D%20Moon%20Light%2006.xml`

- `Phototools%2D%20Moon%20Light%2007.xml`

- `Phototools%2D%20Moon%20Light%2008.xml`

- `Phototools%2D%20Never%20Night%20Light.xml`

- `Phototools%2D%20No%20Light.xml`

- `Phototools%2D%20Owlery%20Light.xml`

- `Phototools%2D%20Puppy%20Light.xml`

- `Phototools%2D%20Queen%20Light%2001.xml`

- `Phototools%2D%20Quidditch%20Light.xml`

- `Phototools%2D%20Save%20Me%20Light%20.xml`

- `Phototools%2D%20Shadow%20Testing%20Light.xml`

- `Phototools%2D%20Still%20Life.xml`

- `Phototools%2D%20Thalia%20Light%2001.xml`

- `Phototools%2D%20Thalia%20Light%2002.xml`

- `Phototools%2D%20Trilogy%20Rain%2001.xml`

- `Phototools%2D%20Trilogy%20Rain%2002.xml`

- `Phototools%2D%20White%20Fire%20Sky%2001.xml`

- `Phototools%2D%20White%20Fire%20Sky%2002.xml`

- `Phototools%2D%20White%20Fire%20Sky%2003.xml`

- `Phototools%2D%20Yellow%20Stars%2001.xml`

- `Phototools%2D%20rara%20Fall%20Home%20Light.xml`

- `Pirate.xml`

- `Places%20Abracadabra.xml`

- `Places%20Abracadabra2.xml`

- `Places%20Abracadabra3.xml`

- `Places%20Annamaria.xml`

- `Places%20Astryls%20Wild.xml`

- `Places%20Babbage.xml`

- `Places%20Beach%20Cay%20Surreal.xml`

- `Places%20Beach%20Cay.xml`

- `Places%20Bentham.xml`

- `Places%20Cornfield.xml`

- `Places%20Cromac.xml`

- `Places%20Crucible.xml`

- `Places%20District8.xml`

- `Places%20Duskwood.xml`

- `Places%20Eridu.xml`

- `Places%20Erie.xml`

- `Places%20Eugene%202.xml`

- `Places%20Eugene%20BL.xml`

- `Places%20Greed.xml`

- `Places%20Greed2.xml`

- `Places%20Imagine.xml`

- `Places%20Kingsport.xml`

- `Places%20Kunming.xml`

- `Places%20Las%20Legunas.xml`

- `Places%20Legacies.xml`

- `Places%20Midian.xml`

- `Places%20Mother.xml`

- `Places%20Old%20New%20York.xml`

- `Places%20Paris%202.xml`

- `Places%20Paris.xml`

- `Places%20Pathfinder.xml`

- `Places%20Sand.xml`

- `Places%20Terre%20Des%20Mortes.xml`

- `Places%20Urbania.xml`

- `Places%20Wiccan.xml`

- `Places%20alirium.xml`

- `Places%2DEmbryo.xml`

- `Purple.xml`

- `Raymond%27s%20Bright%20%26%20Hazy%20Day.xml`

- `Raymond%27s%20Brighter%20Day.xml`

- `Raymond%27s%20Day.xml`

- `Raymond%27s%20Night.xml`

- `Raymond%27s%20Sunrise.xml`

- `Riverrock%20Night.xml`

- `Rot.xml`

- `Sailor%27s%20Delight.xml`

- `Shadow1.xml`

- `ShadowSet.xml`

- `Shadows%20Bright%20day.xml`

- `Sheer%20Surreality.xml`

- `ShepherdsDelight.xml`

- `Silent%20Hill.xml`

- `StrawberrySingh%2Ecom%20%2D%20Closeups.xml`

- `StrawberrySingh%2Ecom%20%2D%20Headshots.xml`

- `Studio%20Light.xml`

- `Sunrise.xml`

- `Sunset%20Pink%20%28Paulina%29.xml`

- `Sunset.xml`

- `Surreal%20%2D%20Brazil%20%28Paulina%29.xml`

- `Surreal%20%2D%20Fire%20%28Paulina%29.xml`

- `Surreal%20%2D%20Flirt%20%28Paulina%29.xml`

- `Surreal%20%2D%20Night%20%28Paulina%29.xml`

- `Surreal%20%2D%20Summer%20%28Paulina%29.xml`

- `Synthwave.xml`

- `The%20Shed.xml`

- `Torie%20Senne%20WL%20settings.xml`

- `Tron%20Legacy%20clean.xml`

- `Tron%20Legacy%20extreme.xml`

- `Tron%20Legacy%20hard.xml`

- `Tron%20Legacy%20soft.xml`

- `Verdigris.xml`

- `Wastes%2012pm.xml`

- `Wastes%20Midnight.xml`

- `Wastes%20Morning.xml`

- `blackskymoon.xml`

- `greyskymoon.xml`

- `names.txt`

- `neutral.xml`

- `pinkpurple.xml`

- `predawnmoon.xml`

- `purplebluenight.xml`

- `wastelands.xml`


## indra/newview/app_settings/windlight/water/ (58 files)

- `%5BNB%5D%20Hidden%20Depths.xml`

- `%5BNB%5D%20Sparkling%20Depths.xml`

- `%5BNB%5D%20Turbid%20Reflections.xml`

- `%5BTOR%5D%20Arrakissed%20variation.xml`

- `%5BTOR%5D%20Atomist%202.xml`

- `%5BTOR%5D%20Atomist.xml`

- `%5BTOR%5D%20Bayouette.xml`

- `%5BTOR%5D%20Chivandria%20clair.xml`

- `%5BTOR%5D%20Claira.xml`

- `%5BTOR%5D%20Coral%20reef.xml`

- `%5BTOR%5D%20Crosshatched%20plans.xml`

- `%5BTOR%5D%20Eyeballin%27.xml`

- `%5BTOR%5D%20Fantastuck.xml`

- `%5BTOR%5D%20Featuresque.xml`

- `%5BTOR%5D%20Freak%2DA%2Ddermia.xml`

- `%5BTOR%5D%20Glaznost.xml`

- `%5BTOR%5D%20Grantamount.xml`

- `%5BTOR%5D%20Hpmod.xml`

- `%5BTOR%5D%20Ice%2Dlike.xml`

- `%5BTOR%5D%20Impure.xml`

- `%5BTOR%5D%20Linear%20puddles.xml`

- `%5BTOR%5D%20Listeryne.xml`

- `%5BTOR%5D%20Liz%20Taylor.xml`

- `%5BTOR%5D%20Maldives.xml`

- `%5BTOR%5D%20Meridian%20verde.xml`

- `%5BTOR%5D%20Negative%20ultraspace.xml`

- `%5BTOR%5D%20Placida%20brite.xml`

- `%5BTOR%5D%20Pretty%20placid.xml`

- `%5BTOR%5D%20Raw%20sewage.xml`

- `%5BTOR%5D%20Showing%20age.xml`

- `%5BTOR%5D%20Soldier%27s%20legacy.xml`

- `%5BTOR%5D%20Subtleties.xml`

- `%5BTOR%5D%20Trandshan.xml`

- `%5BTOR%5D%20Watermelon%20juice.xml`

- `%5BTOR%5D%20Waterslides.xml`

- `%5BTOR%5D%20What%27s%20on%20TV.xml`

- `%5BTOR%5D%20Wickedly.xml`

- `%5BTOR%5D%20You%27re%20in%20luck.xml`

- `%5BTOR%5D%20Yung%20buk.xml`

- `Blackwater.xml`

- `Default.xml`

- `Glassy.xml`

- `Lassies%20Clearwater.xml`

- `Murky.xml`

- `Nacon%27s%20Lake%20Water.xml`

- `Nacon%27s%20Water.xml`

- `Nam%27s%20beach%20Scene.xml`

- `Phototools%2D%20Black%20Default%20.xml`

- `Phototools%2D%20Breakwave%20Building%20Water.xml`

- `Phototools%2D%20Chandra%20Sea.xml`

- `Phototools%2D%20Gallery%20Water%2001.xml`

- `Phototools%2D%20Ship%20Light.xml`

- `Pond.xml`

- `Raymond%27s%20Water%20At%20Night.xml`

- `Raymond%27s%20Water.xml`

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


## indra/newview/cursors_mac/ (40 files)

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

- `UI_CURSOR_TOOLBUY_LEGACY.tif`

- `UI_CURSOR_TOOLCAMERA.tif`

- `UI_CURSOR_TOOLCREATE.tif`

- `UI_CURSOR_TOOLFOCUS.tif`

- `UI_CURSOR_TOOLGRAB.tif`

- `UI_CURSOR_TOOLLAND.tif`

- `UI_CURSOR_TOOLMEDIAOPEN.tif`

- `UI_CURSOR_TOOLOPEN.tif`

- `UI_CURSOR_TOOLOPEN_LEGACY.tif`

- `UI_CURSOR_TOOLPAN.tif`

- `UI_CURSOR_TOOLPAUSE.tif`

- `UI_CURSOR_TOOLPAY_LEGACY.tif`

- `UI_CURSOR_TOOLPICKOBJECT3.tif`

- `UI_CURSOR_TOOLPLAY.tif`

- `UI_CURSOR_TOOLROTATE.tif`

- `UI_CURSOR_TOOLSCALE.tif`

- `UI_CURSOR_TOOLSIT.tif`

- `UI_CURSOR_TOOLSIT_LEGACY.tif`

- `UI_CURSOR_TOOLTRANSLATE.tif`

- `UI_CURSOR_TOOLZOOMIN.tif`

- `UI_CURSOR_TOOLZOOMOUT.tif`

- `UI_CURSOR_WORKING.tif`


## indra/newview/da.lproj/ (1 files)

- `language.txt`


## indra/newview/es.lproj/ (1 files)

- `language.txt`


## indra/newview/fonts/ (79 files)

- `CascadiaCode-Light.ttf`

- `CascadiaCodeFONTLOG.txt`

- `CascadiaCodeLICENSE.txt`

- `CelestiaMediumRedux-NOTICE.txt`

- `CelestiaMediumRedux1.55.ttf`

- `DejaVuSansAllCaps-Bold.ttf`

- `DejaVuSansAllCaps-BoldOblique.ttf`

- `DejaVuSansAllCaps-Oblique.ttf`

- `DejaVuSansAllCaps.ttf`

- `DejaVuSansAllCapsMono.ttf`

- `Droid-License.txt`

- `DroidSans-Bold.ttf`

- `DroidSans.ttf`

- `DroidSansMono.ttf`

- `DroidSerif-Bold.ttf`

- `DroidSerif-BoldItalic.ttf`

- `DroidSerif-Italic.ttf`

- `DroidSerif.ttf`

- `LiberationAUTHORS`

- `LiberationCOPYING`

- `LiberationChangeLog`

- `LiberationLicense.txt`

- `LiberationMono-Regular.ttf`

- `LiberationREADME`

- `LiberationSans-Bold.ttf`

- `LiberationSans-BoldItalic.ttf`

- `LiberationSans-Italic.ttf`

- `LiberationSans-Regular.ttf`

- `LiberationTODO`

- `MobiSans-Bold.ttf`

- `MobiSans-BoldItalic.ttf`

- `MobiSans-Italic.ttf`

- `MobiSans.ttf`

- `MobiSansMono.ttf`

- `NotoFSREADME.txt`

- `NotoLICENSE_OFL.txt`

- `NotoMono-Regular.ttf`

- `NotoSans-Bold.ttf`

- `NotoSans-BoldItalic.ttf`

- `NotoSans-Italic.ttf`

- `NotoSansCombined-Regular.ttf`

- `Roboto-Bold.ttf`

- `Roboto-BoldItalic.ttf`

- `Roboto-Italic.ttf`

- `Roboto-NOTICE.txt`

- `Roboto-Regular.ttf`

- `SourceCodePro-Regular.ttf`

- `SourceCodePro-license.txt`

- `Ubuntu-M.ttf`

- `Ubuntu-MI.ttf`

- `Ubuntu-R.ttf`

- `Ubuntu-RI.ttf`

- `UbuntuCONTRIBUTING.txt`

- `UbuntuFONTLOG.txt`

- `UbuntuLICENCE-FAQ.txt`

- `UbuntuLICENCE.txt`

- `UbuntuMono-R.ttf`

- `UbuntuREADME.txt`

- `UbuntuTRADEMARKS.txt`

- `Ubuntucopyright.txt`

- `fonts.xml`

- `fonts_cascadia_code.xml`

- `fonts_celestia_medium_redux.xml`

- `fonts_deja_vu.xml`

- `fonts_deja_vu_all_caps.xml`

- `fonts_droid.xml`

- `fonts_dyslexia.xml`

- `fonts_inter_tight.xml`

- `fonts_liberation.xml`

- `fonts_mobi.xml`

- `fonts_noto.xml`

- `fonts_roboto.xml`

- `fonts_ubuntu.xml`

- `ocra.ttf`

- `opendyslexic-bold.ttf`

- `opendyslexic-bolditalic.ttf`

- `opendyslexic-italic.ttf`

- `opendyslexic-mono.ttf`

- `opendyslexic.ttf`


## indra/newview/fr.lproj/ (1 files)

- `language.txt`


## indra/newview/fs_resources/ (3 files)

- `EBEDD1D2-A320-43f5-88CF-DD47BBCA5DFB.lsltxt`

- `cube_phys.dae`

- `hex_phys.dae`


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


## indra/newview/icons/beta/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/beta-os/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/development/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/development-os/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/nightly/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/nightly-os/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/private/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/private-os/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/project/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/project-os/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/release/ (11 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`

- `secondlife_1024.png`

- `secondlife_256.png`


## indra/newview/icons/release-os/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/release/secondlife.iconset/ (10 files)

- `icon_128x128.png`

- `icon_128x128@2x.png`

- `icon_16x16.png`

- `icon_16x16@2x.png`

- `icon_256x256.png`

- `icon_256x256@2x.png`

- `icon_32x32.png`

- `icon_32x32@2x.png`

- `icon_512x512.png`

- `icon_512x512@2x.png`


## indra/newview/icons/test/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/icons/test-os/ (9 files)

- `firestorm_128.png`

- `firestorm_16.png`

- `firestorm_256.bmp`

- `firestorm_256.png`

- `firestorm_32.png`

- `firestorm_48.png`

- `firestorm_512.png`

- `firestorm_icon.icns`

- `firestorm_icon.ico`


## indra/newview/installers/darwin/ (4 files)

- `apple-notarize.sh`

- `dmg-cleanup.applescript`

- `fix_application_icon_position.sh`

- `installer-dmg.applescript`


## indra/newview/installers/darwin/firestorm-beta-dmg/ (4 files)

- `Applications-alias.r`

- `_DS_Store`

- `_VolumeIcon.icns`

- `background.png`


## indra/newview/installers/darwin/firestorm-nightly-dmg/ (4 files)

- `Applications-alias.r`

- `_DS_Store`

- `_VolumeIcon.icns`

- `background.png`


## indra/newview/installers/darwin/firestorm-private-dmg/ (4 files)

- `Applications-alias.r`

- `_DS_Store`

- `_VolumeIcon.icns`

- `background.png`


## indra/newview/installers/darwin/firestorm-release-dmg/ (4 files)

- `Applications-alias.r`

- `_DS_Store`

- `_VolumeIcon.icns`

- `background.png`


## indra/newview/installers/darwin/firestormos-beta-dmg/ (4 files)

- `Applications-alias.r`

- `_DS_Store`

- `_VolumeIcon.icns`

- `background.png`


## indra/newview/installers/darwin/firestormos-nightly-dmg/ (4 files)

- `Applications-alias.r`

- `_DS_Store`

- `_VolumeIcon.icns`

- `background.png`


## indra/newview/installers/darwin/firestormos-private-dmg/ (4 files)

- `Applications-alias.r`

- `_DS_Store`

- `_VolumeIcon.icns`

- `background.png`


## indra/newview/installers/darwin/firestormos-release-dmg/ (4 files)

- `Applications-alias.r`

- `_DS_Store`

- `_VolumeIcon.icns`

- `background.png`


## indra/newview/installers/linux/ (1 files)

- `firestorm.desktop`


## indra/newview/installers/windows/ (23 files)

- `FILES_ARE_UNICODE_UTF-16LE.txt`

- `firestorm_icon.BMP`

- `firestorm_icon.ico`

- `firestorm_icon_os.ico`

- `firestorm_icon_small.BMP`

- `install_icon.BMP`

- `install_icon.ico`

- `installer_template.nsi`

- `lang_da.nsi`

- `lang_de.nsi`

- `lang_en-us.nsi`

- `lang_es.nsi`

- `lang_fr.nsi`

- `lang_it.nsi`

- `lang_ja.nsi`

- `lang_pl.nsi`

- `lang_pt-br.nsi`

- `lang_ru.nsi`

- `lang_tr.nsi`

- `lang_zh.nsi`

- `language_menu.nsi`

- `uninstall_icon.BMP`

- `uninstall_icon.ico`


## indra/newview/it.lproj/ (1 files)

- `language.txt`


## indra/newview/linux_tools/ (7 files)

- `FIRESTORM_DESKTOPINSTALL.txt`

- `handle_secondlifeprotocol.sh`

- `install.sh`

- `refresh_desktop_app_entry.sh`

- `register_hopprotocol.sh`

- `register_secondlifeprotocol.sh`

- `wrapper.sh`


## indra/newview/linux_tools/tests/ (3 files)

- `CMakeLists.txt`

- `README.md`

- `test_wrapper.py`


## indra/newview/nl.lproj/ (1 files)

- `language.txt`


## indra/newview/pl.lproj/ (1 files)

- `language.txt`


## indra/newview/pt.lproj/ (1 files)

- `language.txt`


## indra/newview/res/ (53 files)

- `arrow.cur`

- `arrowcop.cur`

- `arrowcopmulti.cur`

- `arrowdrag.cur`

- `bitmap2.bmp`

- `circleandline.cur`

- `firestorm_icon.png`

- `have_artwork_bundle.marker`

- `icon1.ico`

- `install_icon.BMP`

- `ll_icon_small.ico`

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

- `toolbuy-legacy.cur`

- `toolbuy.cur`

- `toolmediaopen.cur`

- `toolopen-legacy.cur`

- `toolopen.cur`

- `toolpause.cur`

- `toolpay-legacy.cur`

- `toolpickobject.cur`

- `toolpickobject2.cur`

- `toolpickobject3.cur`

- `toolpipette.cur`

- `toolplay.cur`

- `toolsit-legacy.cur`

- `toolsit.cur`

- `uninstall_icon.BMP`

- `viewerRes.rc`


## indra/newview/res-sdl/ (54 files)

- `arrow.BMP`

- `arrowcop.BMP`

- `arrowcopmulti.BMP`

- `arrowdrag.BMP`

- `circleandline.BMP`

- `cross.BMP`

- `firestorm_icon.png`

- `firestorm_icon128.png`

- `hand.BMP`

- `ibeam.BMP`

- `llarrow.BMP`

- `llarrowdrag.BMP`

- `llarrowdragmulti.BMP`

- `llarrowlocked.BMP`

- `llgrablocked.BMP`

- `llno.BMP`

- `llnolocked.BMP`

- `lltoolcamera.BMP`

- `lltoolcreate.BMP`

- `lltoolfocus.BMP`

- `lltoolgrab.BMP`

- `lltoolland.BMP`

- `lltoolpan.BMP`

- `lltoolpathfinding.BMP`

- `lltoolpathfindingpathend.BMP`

- `lltoolpathfindingpathendadd.BMP`

- `lltoolpathfindingpathstart.BMP`

- `lltoolpathfindingpathstartadd.BMP`

- `lltoolpipette.BMP`

- `lltoolrotate.BMP`

- `lltoolscale.BMP`

- `lltooltranslate.BMP`

- `lltoolzoomin.BMP`

- `lltoolzoomout.BMP`

- `sizeall.BMP`

- `sizenesw.BMP`

- `sizens.BMP`

- `sizenwse.BMP`

- `sizewe.BMP`

- `toolbuy-legacy.BMP`

- `toolbuy.BMP`

- `toolmediaopen.BMP`

- `toolopen-legacy.BMP`

- `toolopen.BMP`

- `toolpause.BMP`

- `toolpay-legacy.BMP`

- `toolpickobject.BMP`

- `toolpickobject2.BMP`

- `toolpickobject3.BMP`

- `toolplay.BMP`

- `toolsit-legacy.BMP`

- `toolsit.BMP`

- `wait.BMP`

- `working.BMP`


## indra/newview/ru.lproj/ (1 files)

- `language.txt`


## indra/newview/skins/ (1 files)

- `skins.xml`


## indra/newview/skins/ansastorm/ (1 files)

- `colors.xml`


## indra/newview/skins/ansastorm/textures/ (2 files)

- `tabarea.tga`

- `textures.xml`


## indra/newview/skins/ansastorm/textures/bottomtray/ (9 files)

- `BottomTray_BG.png`

- `Cam_Rotate_Center.png`

- `Cam_Rotate_In.png`

- `Cam_Tracking_Center.png`

- `Cam_Tracking_In.png`

- `ChatBarHandle.png`

- `Unread_Msg.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`


## indra/newview/skins/ansastorm/textures/containers/ (35 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/ansastorm/textures/icons/ (11 files)

- `Icon_DialogStack.png`

- `Info_Over.png`

- `Radar_Voice_Lvl1.png`

- `Radar_Voice_Lvl2.png`

- `Radar_Voice_Lvl3.png`

- `Radar_Voice_Off.png`

- `Radar_Voice_On.png`

- `back_arrow_press.png`

- `green_square.png`

- `green_yellow_square.png`

- `yellow_square.png`


## indra/newview/skins/ansastorm/textures/legacy/ (3 files)

- `icon_avatar_online_list.tga`

- `payment_info_filled.tga`

- `payment_info_used.tga`


## indra/newview/skins/ansastorm/textures/navbar/ (32 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/ansastorm/textures/widgets/ (152 files)

- `Arrow_Down.png`

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

- `Checkbox_Transparent_Disabled.png`

- `Checkbox_Transparent_Off.png`

- `Checkbox_Transparent_On.png`

- `Checkbox_Transparent_On_Disabled.png`

- `ComboButton_Disabled.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

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

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

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

- `SegmentedBtn_Middle_Press.png`

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

- `SliderTrack_Vert.pdn`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Highlight.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`


## indra/newview/skins/ansastorm/textures/windows/ (9 files)

- `Inspector_Background.png`

- `Inspector_I.png`

- `TimeBasedMediaBackground.png`

- `Volume_Background.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_background.png`


## indra/newview/skins/ansastorm/themes/blood/ (1 files)

- `colors.xml`


## indra/newview/skins/ansastorm/themes/blood/textures/ (1 files)

- `tabarea.tga`


## indra/newview/skins/ansastorm/themes/blood/textures/bottomtray/ (6 files)

- `Cam_Rotate_Center.png`

- `Cam_Rotate_In.png`

- `Cam_Tracking_Center.png`

- `Cam_Tracking_In.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`


## indra/newview/skins/ansastorm/themes/blood/textures/containers/ (12 files)

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Selected.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Selected.png`


## indra/newview/skins/ansastorm/themes/blood/textures/icons/ (3 files)

- `Icon_DialogStack.png`

- `Info_Over.png`

- `back_arrow_press.png`


## indra/newview/skins/ansastorm/themes/blood/textures/navbar/ (2 files)

- `FileMenu_BarSelect.png`

- `Row_Selection.png`


## indra/newview/skins/ansastorm/themes/blood/textures/widgets/ (100 files)

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Press.png`

- `Checkbox_Press.png`

- `Checkbox_Transparent_Disabled.png`

- `Checkbox_Transparent_Off.png`

- `Checkbox_Transparent_On.png`

- `Checkbox_Transparent_On_Disabled.png`

- `ComboButton_Disabled.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `Linden_Dollar_Alert.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

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

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

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

- `SegmentedBtn_Middle_Press.png`

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

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Highlight.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`


## indra/newview/skins/ansastorm/themes/blood/textures/windows/ (9 files)

- `Inspector_Background.png`

- `Inspector_I.png`

- `TimeBasedMediaBackground.png`

- `Volume_Background.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_background.png`


## indra/newview/skins/ansastorm/themes/blood/textures/world/ (1 files)

- `NoEntryLines.png`


## indra/newview/skins/ansastorm/themes/classic_brown/ (1 files)

- `colors.xml`


## indra/newview/skins/ansastorm/themes/classic_brown/textures/bottomtray/ (6 files)

- `Cam_Rotate_Center.png`

- `Cam_Rotate_In.png`

- `Cam_Tracking_Center.png`

- `Cam_Tracking_In.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`


## indra/newview/skins/ansastorm/themes/classic_brown/textures/containers/ (12 files)

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Selected.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Selected.png`


## indra/newview/skins/ansastorm/themes/classic_brown/textures/icons/ (3 files)

- `Icon_DialogStack.png`

- `Info_Over.png`

- `back_arrow_press.png`


## indra/newview/skins/ansastorm/themes/classic_brown/textures/navbar/ (2 files)

- `FileMenu_BarSelect.png`

- `Row_Selection.png`


## indra/newview/skins/ansastorm/themes/classic_brown/textures/widgets/ (30 files)

- `ComboButton_On.png`

- `DropDown_On.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Press.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Selected_Press.png`

- `TextField_Search_Highlight.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`


## indra/newview/skins/ansastorm/themes/classic_brown/textures/windows/ (1 files)

- `Inspector_I.png`


## indra/newview/skins/ansastorm/themes/ectoplasma/ (1 files)

- `colors.xml`


## indra/newview/skins/ansastorm/themes/ectoplasma/textures/ (1 files)

- `tabarea.tga`


## indra/newview/skins/ansastorm/themes/ectoplasma/textures/bottomtray/ (6 files)

- `Cam_Rotate_Center.png`

- `Cam_Rotate_In.png`

- `Cam_Tracking_Center.png`

- `Cam_Tracking_In.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`


## indra/newview/skins/ansastorm/themes/ectoplasma/textures/containers/ (12 files)

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Selected.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Selected.png`


## indra/newview/skins/ansastorm/themes/ectoplasma/textures/icons/ (3 files)

- `Icon_DialogStack.png`

- `Info_Over.png`

- `back_arrow_press.png`


## indra/newview/skins/ansastorm/themes/ectoplasma/textures/navbar/ (2 files)

- `FileMenu_BarSelect.png`

- `Row_Selection.png`


## indra/newview/skins/ansastorm/themes/ectoplasma/textures/widgets/ (100 files)

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Press.png`

- `Checkbox_Press.png`

- `Checkbox_Transparent_Disabled.png`

- `Checkbox_Transparent_Off.png`

- `Checkbox_Transparent_On.png`

- `Checkbox_Transparent_On_Disabled.png`

- `ComboButton_Disabled.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `Linden_Dollar_Alert.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

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

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

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

- `SegmentedBtn_Middle_Press.png`

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

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Highlight.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`


## indra/newview/skins/ansastorm/themes/ectoplasma/textures/windows/ (9 files)

- `Inspector_Background.png`

- `Inspector_I.png`

- `TimeBasedMediaBackground.png`

- `Volume_Background.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_background.png`


## indra/newview/skins/ansastorm/themes/ectoplasma/textures/world/ (1 files)

- `NoEntryLines.png`


## indra/newview/skins/ansastorm/xui/de/ (17 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm/xui/en/ (34 files)

- `floater_camera.xml`

- `floater_my_appearance.xml`

- `floater_my_inventory.xml`

- `floater_preview_texture.xml`

- `panel_button_checkbox.xml`

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

- `panel_fs_contacts_friends.xml`

- `panel_fs_radar.xml`

- `panel_group_info_sidetray.xml`

- `panel_main_inventory.xml`

- `panel_outfit_edit.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_toolbar_view.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`


## indra/newview/skins/ansastorm/xui/en/widgets/ (7 files)

- `avatar_list_item.xml`

- `filter_editor.xml`

- `floater.xml`

- `search_combo_box.xml`

- `search_editor.xml`

- `toolbar.xml`

- `toolbar_vertical.xml`


## indra/newview/skins/ansastorm/xui/es/ (16 files)

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm/xui/it/ (17 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm/xui/ja/ (18 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_wearable.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm/xui/pl/ (17 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm/xui/pt/ (18 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_group_info_sidetray.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm/xui/ru/ (17 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm/xui/zh/ (17 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm_modern/ (1 files)

- `colors.xml`


## indra/newview/skins/ansastorm_modern/textures/ (1 files)

- `textures.xml`


## indra/newview/skins/ansastorm_modern/textures/bottomtray/ (28 files)

- `BottomTray_BG.png`

- `Cam_Rotate_Center.png`

- `Cam_Rotate_In.png`

- `Cam_Tracking_Center.png`

- `Cam_Tracking_In.png`

- `ChatBarHandle.png`

- `Movement_Backward_On.png`

- `Movement_Down_Off.png`

- `Movement_Down_On.png`

- `Movement_Forward_Off.png`

- `Movement_Forward_On.png`

- `Movement_Left_Off.png`

- `Movement_Left_On.png`

- `Movement_Right_Off.png`

- `Movement_Right_On.png`

- `Movement_TurnLeft_On.png`

- `Movement_TurnRight_On.png`

- `Movement_Up_On.png`

- `Object_View_On.png`

- `Unread_Chiclet.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`


## indra/newview/skins/ansastorm_modern/textures/build/ (15 files)

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


## indra/newview/skins/ansastorm_modern/textures/containers/ (21 files)

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `TabLeft_Flat_Off.png`

- `TabLeft_Flat_Selected.png`

- `TabTop_First_Flat_Off.png`

- `TabTop_First_Flat_Selected.png`

- `TabTop_Last_Flat_Off.png`

- `TabTop_Last_Flat_Selected.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Flat_Off.png`

- `TabTop_Middle_Flat_Selected.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Selected.png`


## indra/newview/skins/ansastorm_modern/textures/icons/ (21 files)

- `Icon_DialogStack.png`

- `Info_Over.png`

- `Presets_Icon.png`

- `Presets_Icon_Graphic.png`

- `Profile_Friend_Offline.png`

- `Profile_Friend_Online.png`

- `Radar_Voice_Lvl1.png`

- `Radar_Voice_Lvl2.png`

- `Radar_Voice_Lvl3.png`

- `Radar_Voice_Off.png`

- `Radar_Voice_On.png`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `check_mark.png`

- `green_square.png`

- `green_yellow_square.png`

- `hand.png`

- `pop_up_caution.png`

- `see_me_online.png`

- `yellow_square.png`


## indra/newview/skins/ansastorm_modern/textures/legacy/ (3 files)

- `icon_avatar_online_list.tga`

- `payment_info_filled.tga`

- `payment_info_used.tga`


## indra/newview/skins/ansastorm_modern/textures/navbar/ (15 files)

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`


## indra/newview/skins/ansastorm_modern/textures/widgets/ (151 files)

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Press.png`

- `Checkbox_Press.png`

- `Checkbox_Transparent_Disabled.png`

- `Checkbox_Transparent_Off.png`

- `Checkbox_Transparent_On.png`

- `Checkbox_Transparent_On_Disabled.png`

- `ComboButton_Disabled.png`

- `ComboButton_Hover.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

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

- `PushButton_On_Disabled.png`

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

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

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

- `SegmentedBtn_Middle_Press.png`

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

- `SliderTrack_Vert.pdn`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

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

- `Tooltip.png`

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


## indra/newview/skins/ansastorm_modern/textures/windows/ (40 files)

- `Dragbar.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

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

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`


## indra/newview/skins/ansastorm_modern/xui/de/ (17 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm_modern/xui/en/ (35 files)

- `floater_camera.xml`

- `floater_fs_contacts.xml`

- `floater_my_appearance.xml`

- `floater_my_inventory.xml`

- `floater_preview_texture.xml`

- `panel_button_checkbox.xml`

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

- `panel_fs_contacts_friends.xml`

- `panel_fs_radar.xml`

- `panel_group_info_sidetray.xml`

- `panel_main_inventory.xml`

- `panel_outfit_edit.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_toolbar_view.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`


## indra/newview/skins/ansastorm_modern/xui/en/widgets/ (13 files)

- `avatar_list_item.xml`

- `button.xml`

- `filter_editor.xml`

- `floater.xml`

- `folder_view_item.xml`

- `line_editor.xml`

- `progress_bar.xml`

- `search_combo_box.xml`

- `search_editor.xml`

- `simple_text_editor.xml`

- `tab_container.xml`

- `toolbar.xml`

- `toolbar_vertical.xml`


## indra/newview/skins/ansastorm_modern/xui/es/ (16 files)

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm_modern/xui/it/ (17 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm_modern/xui/ja/ (19 files)

- `floater_camera.xml`

- `floater_fs_contacts.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_edit_wearable.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm_modern/xui/pl/ (17 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm_modern/xui/pt/ (18 files)

- `floater_camera.xml`

- `floater_fs_contacts.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm_modern/xui/ru/ (17 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/ansastorm_modern/xui/zh/ (17 files)

- `floater_camera.xml`

- `floater_preview_texture.xml`

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

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_main_inventory.xml`


## indra/newview/skins/default/ (4 files)

- `colors.xml`

- `default_languages.xml`

- `settings.xml`

- `toolbars.xml`


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


## indra/newview/skins/default/textures/ (147 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Console_Background.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_up.tga`

- `avatar_thumb_bkgrnd.png`

- `badge_note.j2c`

- `badge_ok.j2c`

- `badge_warn.j2c`

- `beam_phoenix.png`

- `beam_rainbow.png`

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

- `firestorm_icon.png`

- `flatnormal.tga`

- `flyout_btn_left.tga`

- `flyout_btn_left_disabled.tga`

- `flyout_btn_left_selected.tga`

- `flyout_btn_right.tga`

- `flyout_btn_right_disabled.tga`

- `flyout_btn_right_selected.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `glowtouchables.tga`

- `green_checkmark.png`

- `green_dot.tga`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-call-end.tga`

- `icn_voice-call-start.tga`

- `icn_voice-localchat.tga`

- `icn_voice_ptt-off.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on-lvl3.tga`

- `icn_voice_ptt-on.tga`

- `icon_auction.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_day_cycle_12am.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_group.png`

- `icon_legacy_event.tga`

- `icon_legacy_event_adult.tga`

- `icon_legacy_event_mature.tga`

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

- `map_avatar_unknown.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_32.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_ui_collapse_icon.png`

- `map_ui_expand_icon.png`

- `materials_ui_x_24.png`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `payment_info_used.tga`

- `pixiesmall.j2c`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `red_x.png`

- `rounded_square.j2c`

- `salt_and_pepper.jpg`

- `script_error.j2c`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `snapshot_flickr.png`

- `spacer24-2.tga`

- `spacer24.tga`

- `square_selection.png`

- `tabarea.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `textures.xml`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/default/textures/3p_icons/ (3 files)

- `fmod_logo.png`

- `havok_logo.png`

- `vivox_logo.png`


## indra/newview/skins/default/textures/bottomtray/ (99 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_Center.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_Center.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Dpad.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Off.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl1_Dark.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl2_Dark.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Lvl3_Dark.png`

- `VoicePTT_Off.png`

- `VoicePTT_Off_Dark.png`

- `VoicePTT_On.png`

- `VoicePTT_On_Dark.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `camera_load.png`

- `camera_store.png`

- `chatbar_18.png`

- `coalesced_18.png`

- `inventory_18.png`

- `show_filters_18.png`


## indra/newview/skins/default/textures/build/ (42 files)

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

- `PhysicsView_Off.png`

- `PhysicsView_On.png`

- `Tool_Create.png`

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/default/textures/containers/ (47 files)

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

- `TabTop_Divider.png`

- `TabTop_First_Flat_Off.png`

- `TabTop_First_Flat_Selected.png`

- `TabTop_Last_Flat_Off.png`

- `TabTop_Last_Flat_Selected.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Flat_Off.png`

- `TabTop_Middle_Flat_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Flashing.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_IM_Unselected.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_IM_Unselected.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_IM_Unselected.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/default/textures/icons/ (428 files)

- `AddItem_Disabled.png`

- `AddItem_Menu.png`

- `AddItem_Off.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Press.png`

- `Camera_Off.png`

- `Camera_Over.png`

- `Camera_Press.png`

- `Chat_History.png`

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

- `Conv_toolbar_plus.png`

- `Conv_toolbar_sort.png`

- `Copy.png`

- `CopyBright.png`

- `Default_Outfit_Photo.png`

- `DownArrow_Off.png`

- `Edit_Flip_X.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Facebook.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Friends_Icon_24x24.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Group_Notices.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_Attachment_Large.png`

- `Icon_Attachment_Small.png`

- `Icon_Color_Palette.png`

- `Icon_DialogStack.png`

- `Icon_Font_Size.png`

- `Icon_For_Sale.png`

- `Icon_Notification_Condense.png`

- `Icon_Notification_Expand.png`

- `Icon_Pointer.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Alpha_Link.png`

- `Inv_Animation.png`

- `Inv_Animation_Link.png`

- `Inv_BodyShape.png`

- `Inv_BodyShape_Link.png`

- `Inv_CallingCard.png`

- `Inv_CallingCard_Link.png`

- `Inv_Clothing.png`

- `Inv_Clothing_Link.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_Eye_Link.png`

- `Inv_Favorite_Star_Content.png`

- `Inv_Favorite_Star_Full.png`

- `Inv_FolderClosed.png`

- `Inv_FolderClosed_Link.png`

- `Inv_FolderOpen.png`

- `Inv_FolderOpen_Link.png`

- `Inv_Gesture.png`

- `Inv_Gesture_Link.png`

- `Inv_Gloves.png`

- `Inv_Gloves_Link.png`

- `Inv_Hair.png`

- `Inv_Hair_Link.png`

- `Inv_Invalid.png`

- `Inv_Jacket.png`

- `Inv_Jacket_Link.png`

- `Inv_Landmark.png`

- `Inv_Landmark_Link.png`

- `Inv_Link.png`

- `Inv_LinkFolder.png`

- `Inv_LinkFolder_Link.png`

- `Inv_LinkItem.png`

- `Inv_LinkItem_Broken.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderClosed_Link.png`

- `Inv_LookFolderOpen.png`

- `Inv_LookFolderOpen_Link.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Material.png`

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Notecard_Link.png`

- `Inv_Object.png`

- `Inv_Object_Link.png`

- `Inv_Object_Multi.png`

- `Inv_Object_Multi_Link.png`

- `Inv_Pants.png`

- `Inv_Pants_Link.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Script_Link.png`

- `Inv_Script_Luau.png`

- `Inv_Settings.png`

- `Inv_SettingsDay.png`

- `Inv_SettingsSky.png`

- `Inv_SettingsWater.png`

- `Inv_Shirt.png`

- `Inv_Shirt_Link.png`

- `Inv_Shoe.png`

- `Inv_Shoe_Link.png`

- `Inv_Skin.png`

- `Inv_Skin_Link.png`

- `Inv_Skirt.png`

- `Inv_Skirt_Link.png`

- `Inv_Snapshot.png`

- `Inv_Snapshot_Link.png`

- `Inv_Socks.png`

- `Inv_Socks_Link.png`

- `Inv_Sound.png`

- `Inv_Sound_Link.png`

- `Inv_StockFolderClosed.png`

- `Inv_StockFolderOpen.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Tattoo_Link.png`

- `Inv_Texture.png`

- `Inv_Texture_Link.png`

- `Inv_Toolbar_SearchVisibility.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Underpants_Link.png`

- `Inv_Undershirt.png`

- `Inv_Undershirt_Link.png`

- `Inv_Universal.png`

- `Inv_UnknownObject.png`

- `Inv_VersionFolderClosed.png`

- `Inv_VersionFolderOpen.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `Music_Off.png`

- `Music_Over.png`

- `Music_Press.png`

- `Muted_Chat.png`

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

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Paste.png`

- `Pathfinding_Dirty.png`

- `Pathfinding_Dirty_Light.png`

- `Pathfinding_Disabled.png`

- `Pathfinding_Disabled_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

- `PowerOff_Off.png`

- `PowerOff_Over.png`

- `PowerOff_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `ProgressLarge_1.png`

- `ProgressLarge_10.png`

- `ProgressLarge_11.png`

- `ProgressLarge_12.png`

- `ProgressLarge_2.png`

- `ProgressLarge_3.png`

- `ProgressLarge_4.png`

- `ProgressLarge_5.png`

- `ProgressLarge_6.png`

- `ProgressLarge_7.png`

- `ProgressLarge_8.png`

- `ProgressLarge_9.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

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

- `TrashItem_Menu.png`

- `TrashItem_Off.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `Video_URL_Off.png`

- `VoiceMute_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `add_icon.png`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `call_end_icon_24x24.png`

- `call_icon_24x24.png`

- `check_mark.png`

- `collapse_to_one_line.png`

- `copy_clipboard.png`

- `delete_icon.png`

- `edit_mine.png`

- `edit_mine_h.png`

- `edit_theirs.png`

- `edit_theirs_h.png`

- `emoji_picker_icon.png`

- `expand_one_liner.png`

- `file_upload.png`

- `fstrusted.png`

- `genie_icon_24x24.png`

- `gift_icon_24x24.png`

- `green_square.png`

- `green_yellow_square.png`

- `hand.png`

- `map_placeholder.png`

- `multi_folder_mode.png`

- `nearby_chat_icon.png`

- `object_icon.png`

- `paste_clipboard.png`

- `pop_up_caution.png`

- `primfeed.png`

- `primfeed_white.png`

- `profile_badge_beta.png`

- `profile_badge_beta_lifetime.png`

- `profile_badge_lifetime.png`

- `profile_badge_linden.png`

- `profile_badge_pplus_lifetime.png`

- `profile_badge_premium_lifetime.png`

- `profile_badge_team.png`

- `profile_group_visibility_eye_off.png`

- `profile_group_visibility_eye_off_pressed.png`

- `profile_group_visibility_eye_on.png`

- `profile_group_visibility_eye_on_pressed.png`

- `profile_icon_24x24.png`

- `radar_b.png`

- `radar_n.png`

- `radar_p.png`

- `radar_s.png`

- `radar_t.png`

- `red_square.png`

- `remove_icon.png`

- `sale_icon_24x24.png`

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

- `see_me_online.png`

- `see_me_online_h.png`

- `see_on_map.png`

- `see_on_map_h.png`

- `single_folder_back.png`

- `single_folder_forward.png`

- `single_folder_mode.png`

- `single_folder_up.png`

- `snapshot_icon.png`

- `status_script_debug.tga`

- `teleport_menu.png`

- `texture_icon.png`

- `thumbnail_fallback_icon.png`

- `unknown_icon.png`

- `visual_pose_enabled.png`

- `yellow_square.png`


## indra/newview/skins/default/textures/legacy/ (97 files)

- `LICENSE-logos.txt`

- `Pathfinding_Dirty_Light.png`

- `Pathfinding_Disabled_Light.png`

- `active_voice_tab.tga`

- `ff_edit_mine.tga`

- `ff_edit_mine_button.tga`

- `ff_edit_theirs.tga`

- `ff_edit_theirs_button.tga`

- `ff_online_status_button.tga`

- `ff_visible_map.tga`

- `ff_visible_map_button.tga`

- `ff_visible_map_button_theirs.tga`

- `ff_visible_map_theirs.tga`

- `ff_visible_online.tga`

- `ff_visible_online_button.tga`

- `ff_visible_online_button_theirs.tga`

- `ff_visible_online_theirs.tga`

- `icon_avatar_online.tga`

- `icon_avatar_online_h.tga`

- `inv_folder_RLVa.tga`

- `inv_folder_animation.tga`

- `inv_folder_bodypart.tga`

- `inv_folder_callingcard.tga`

- `inv_folder_clothing.tga`

- `inv_folder_favorite.tga`

- `inv_folder_firestorm.tga`

- `inv_folder_gesture.tga`

- `inv_folder_inbox.tga`

- `inv_folder_landmark.tga`

- `inv_folder_lostandfound.tga`

- `inv_folder_materials.tga`

- `inv_folder_meshes.tga`

- `inv_folder_notecard.tga`

- `inv_folder_object.tga`

- `inv_folder_outfit.tga`

- `inv_folder_phoenix.tga`

- `inv_folder_plain_closed.tga`

- `inv_folder_plain_open.tga`

- `inv_folder_script.tga`

- `inv_folder_settings.tga`

- `inv_folder_snapshot.tga`

- `inv_folder_sound.tga`

- `inv_folder_stock_closed.tga`

- `inv_folder_stock_open.tga`

- `inv_folder_suitcase.tga`

- `inv_folder_texture.tga`

- `inv_folder_trash.tga`

- `inv_folder_version_closed.tga`

- `inv_folder_version_open.tga`

- `inv_item_alpha.tga`

- `inv_item_animation.tga`

- `inv_item_attach.tga`

- `inv_item_callingcard_offline.tga`

- `inv_item_callingcard_online.tga`

- `inv_item_clothing.tga`

- `inv_item_eyes.tga`

- `inv_item_gesture.tga`

- `inv_item_gloves.tga`

- `inv_item_hair.tga`

- `inv_item_jacket.tga`

- `inv_item_landmark.tga`

- `inv_item_landmark_visited.tga`

- `inv_item_mesh.tga`

- `inv_item_notecard.tga`

- `inv_item_object.tga`

- `inv_item_object_multi.tga`

- `inv_item_pants.tga`

- `inv_item_script.tga`

- `inv_item_script_dangerous.tga`

- `inv_item_shape.tga`

- `inv_item_shirt.tga`

- `inv_item_shoes.tga`

- `inv_item_skin.tga`

- `inv_item_skirt.tga`

- `inv_item_snapshot.tga`

- `inv_item_socks.tga`

- `inv_item_sound.tga`

- `inv_item_tattoo.tga`

- `inv_item_texture.tga`

- `inv_item_underpants.tga`

- `inv_item_undershirt.tga`

- `inv_item_universal.tga`

- `payment_info_filled.tga`

- `payment_info_used.tga`

- `status_SeeAVsOff.tga`

- `status_build.png`

- `status_buy_land.tga`

- `status_fly.png`

- `status_health.tga`

- `status_no_build.tga`

- `status_no_fly.tga`

- `status_no_push.tga`

- `status_no_scripts.tga`

- `status_no_voice.png`

- `status_push.png`

- `status_scripts.png`

- `status_voice.png`


## indra/newview/skins/default/textures/model_wizard/ (2 files)

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/default/textures/navbar/ (33 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Landmarks.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/default/textures/skinspreview/ (22 files)

- `ansa_blood.jpg`

- `ansa_blue.jpg`

- `ansa_brown.jpg`

- `ansa_ecto.jpg`

- `ansa_modern_blue.jpg`

- `fs_blue.jpg`

- `fs_contrast.jpg`

- `fs_ctrlaltstudio.jpg`

- `fs_dark.jpg`

- `fs_grey.jpg`

- `meta_appalachia.jpg`

- `meta_blackglass.jpg`

- `meta_coolocean.jpg`

- `scui_dark.jpg`

- `scui_light.jpg`

- `slight_mteal.jpg`

- `slight_nblue.jpg`

- `slight_orange.jpg`

- `slight_sblue.jpg`

- `slight_spink.jpg`

- `slight_teal.jpg`

- `vintage_classic.jpg`


## indra/newview/skins/default/textures/taskpanel/ (34 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`

- `translate_icon_24x24.png`


## indra/newview/skins/default/textures/toolbar_icons/ (73 files)

- `360_capture.png`

- `RFO_OFF.png`

- `RFO_ON.png`

- `animation_override.png`

- `appearance.png`

- `areasearch.png`

- `asset_blacklist.png`

- `avatars.png`

- `beacons.png`

- `blocklist.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `chat.png`

- `compass.png`

- `contact_sets.png`

- `destinations.png`

- `discord.png`

- `environments.png`

- `facebook.png`

- `facenearest.png`

- `flickr.png`

- `gestures.png`

- `grid_status.png`

- `groundsit.png`

- `group_titles.png`

- `highlighting.png`

- `highlighting_selected.png`

- `inventory.png`

- `land.png`

- `landmark_here.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `mktlistings.png`

- `mouselook.png`

- `move.png`

- `movelock.png`

- `nearbychat.png`

- `nearbyvoice.png`

- `omnifilter.png`

- `outbox.png`

- `people.png`

- `performance.png`

- `phoenix.png`

- `phototools.png`

- `phototools_cam.png`

- `picks.png`

- `places.png`

- `poser.png`

- `posestand.png`

- `preferences.png`

- `profile.png`

- `radar.png`

- `region.png`

- `regiontracker.png`

- `report_abuse.png`

- `resync_animations.png`

- `search.png`

- `settings_debug.png`

- `snapshot.png`

- `snapshot_to_disk.png`

- `sound_explorer.png`

- `speak.png`

- `statistics.png`

- `stop_animations.png`

- `teleporthistory.png`

- `twitter.png`

- `view.png`

- `wearable_favorites.png`

- `www.png`


## indra/newview/skins/default/textures/widgets/ (178 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

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

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_Transparent.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

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

- `PushButton_On_Disabled.png`

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

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

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

- `SegmentedBtn_Middle_Press.png`

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

- `SliderTrack_Vert.pdn`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

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


## indra/newview/skins/default/textures/windows/ (55 files)

- `Dragbar.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Snooze_Foreground.png`

- `Icon_Snooze_Press.png`

- `Icon_Undock_Foreground.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

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

- `login_fs_logo.png`

- `login_sl_logo.png`

- `login_sl_logo_horizontal.png`

- `login_sl_logo_small.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/default/textures/world/ (10 files)

- `BeaconArrow.png`

- `CameraDragDot.png`

- `NoEntryLines.png`

- `NoEntryPassLines.png`

- `Overhead_Arrow_L.png`

- `Overhead_Arrow_M.png`

- `Overhead_Arrow_S.png`

- `Overhead_L.png`

- `Overhead_M.png`

- `Overhead_S.png`


## indra/newview/skins/default/themes/textures/ (1 files)

- `placeholder.tga`


## indra/newview/skins/default/xui/az/ (547 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `floater_360capture.xml`

- `floater_NACL_explore_sounds.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_add_payment_method.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_beamcolor.xml`

- `floater_beamshape.xml`

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

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_avatar_render_settings.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_blocklist.xml`

- `floater_fs_camera_small.xml`

- `floater_fs_contact_add.xml`

- `floater_fs_contact_set_configuration.xml`

- `floater_fs_contacts.xml`

- `floater_fs_discord.xml`

- `floater_fs_export.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_partial_inventory.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_posestand.xml`

- `floater_fs_protectedfolders.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_fs_vram_usage.xml`

- `floater_fs_wearable_favorites.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_how_to.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notification.xml`

- `floater_notifications_console.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_particle_editor.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_performance.xml`

- `floater_perms_default.xml`

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_region_tracker.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_script_recover.xml`

- `floater_search_replace.xml`

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

- `floater_ui_preview.xml`

- `floater_url_entry.xml`

- `floater_vj_local_mesh.xml`

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

- `menu_classifieds.xml`

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

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_asset_blacklist.xml`

- `menu_fs_avatar_render_setting.xml`

- `menu_fs_avatar_search.xml`

- `menu_fs_avatar_search_multiselect.xml`

- `menu_fs_block_list.xml`

- `menu_fs_bump_list.xml`

- `menu_fs_chat_options.xml`

- `menu_fs_contacts_friends.xml`

- `menu_fs_contacts_friends_multiselect.xml`

- `menu_fs_im_teleport.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_inspect_options.xml`

- `menu_fs_moneytracker_list.xml`

- `menu_fs_namelist_avatar.xml`

- `menu_fs_namelist_avatar_multiselect.xml`

- `menu_fs_profile_image_actions.xml`

- `menu_fs_profile_name_field.xml`

- `menu_fs_profile_overflow.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_fs_wearable_favorites.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

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

- `menu_people_contact_sets_add.xml`

- `menu_people_contact_sets_gear.xml`

- `menu_people_contact_sets_remove.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_perf_avatar_rendering_settings.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_mute_particle.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

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

- `menu_teleport_history_timezone.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `panel_ao.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_contacts_sets.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

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

- `panel_notifications_channel.xml`

- `panel_notify_textbox.xml`

- `panel_outfit_edit.xml`

- `panel_outfit_gallery.xml`

- `panel_outfit_snapshot_inventory.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_people_contact_sets.xml`

- `panel_performance_autotune.xml`

- `panel_performance_complexity.xml`

- `panel_performance_huds.xml`

- `panel_performance_nearby.xml`

- `panel_performance_preferences.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

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

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

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

- `panel_sys_well_item.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

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


## indra/newview/skins/default/xui/az/widgets/ (11 files)

- `bodyparts_list_item.xml`

- `clothing_list_item.xml`

- `deletable_wearable_list_item.xml`

- `density_ctrl.xml`

- `dummy_clothing_list_item.xml`

- `flat_list_view.xml`

- `inbox_folder_view_folder.xml`

- `inbox_folder_view_item.xml`

- `name_editor.xml`

- `person_view.xml`

- `sun_moon_trackball.xml`


## indra/newview/skins/default/xui/da/ (260 files)

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

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_critical.xml`

- `floater_display_name.xml`

- `floater_event.xml`

- `floater_font_test.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_voice_controls.xml`

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

- `floater_inventory_item_properties.xml`

- `floater_inventory_view_finder.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_live_lsleditor.xml`

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

- `floater_script_preview.xml`

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

- `menu_gesture_gear.xml`

- `menu_group_plus.xml`

- `menu_hide_navbar.xml`

- `menu_imchiclet_adhoc.xml`

- `menu_imchiclet_group.xml`

- `menu_imchiclet_p2p.xml`

- `menu_inspect_avatar_gear.xml`

- `menu_inspect_object_gear.xml`

- `menu_inspect_self_gear.xml`

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

- `panel_fs_login.xml`

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

- `panel_script_ed.xml`

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

- `xui_version.xml`


## indra/newview/skins/default/xui/de/ (604 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_flycam.xml`

- `control_table_contents_game_control.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `floater_360capture.xml`

- `floater_NACL_explore_sounds.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_add_payment_method.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_align.xml`

- `floater_avatar_align_mini.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_avatar_welcome_pack.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_beamcolor.xml`

- `floater_beamshape.xml`

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

- `floater_chat_mention_picker.xml`

- `floater_choose_group.xml`

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

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_avatar_render_settings.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_blocklist.xml`

- `floater_fs_camera_small.xml`

- `floater_fs_contact_add.xml`

- `floater_fs_contact_set_configuration.xml`

- `floater_fs_contacts.xml`

- `floater_fs_discord.xml`

- `floater_fs_export.xml`

- `floater_fs_fixedenvironment.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_partial_inventory.xml`

- `floater_fs_performance.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_poser.xml`

- `floater_fs_posestand.xml`

- `floater_fs_protectedfolders.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_streamtitle.xml`

- `floater_fs_streamtitlehistory.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_fs_vram_usage.xml`

- `floater_fs_wearable_favorites.xml`

- `floater_gesture.xml`

- `floater_gesture_autocomplete_picker.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_live_material_editor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_maturity_dialog.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notification.xml`

- `floater_notifications_console.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_omnifilter.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_particle_editor.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_primfeed.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restart_schedule.xml`

- `floater_region_restarting.xml`

- `floater_region_tracker.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_script_recover.xml`

- `floater_search.xml`

- `floater_search_replace.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_color.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_simple_snapshot.xml`

- `floater_snapshot.xml`

- `floater_snapshot_guide_settings.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_task_properties.xml`

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

- `floater_vj_local_mesh.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `game_control_table_camera_rows.xml`

- `game_control_table_rows.xml`

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

- `menu_classifieds.xml`

- `menu_cof_attachment.xml`

- `menu_cof_body_part.xml`

- `menu_cof_clothing.xml`

- `menu_cof_gear.xml`

- `menu_conversation.xml`

- `menu_conversation_log_gear.xml`

- `menu_conversation_log_view.xml`

- `menu_dir_people.xml`

- `menu_edit.xml`

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_asset_blacklist.xml`

- `menu_fs_avatar_render_setting.xml`

- `menu_fs_avatar_search.xml`

- `menu_fs_avatar_search_multiselect.xml`

- `menu_fs_block_list.xml`

- `menu_fs_bump_list.xml`

- `menu_fs_chat_options.xml`

- `menu_fs_contacts_friends.xml`

- `menu_fs_contacts_friends_multiselect.xml`

- `menu_fs_im_teleport.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_inspect_options.xml`

- `menu_fs_moneytracker_list.xml`

- `menu_fs_namelist_avatar.xml`

- `menu_fs_namelist_avatar_multiselect.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_fs_profile_image_actions.xml`

- `menu_fs_profile_name_field.xml`

- `menu_fs_profile_overflow.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_fs_wearable_favorites.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_custom_tab.xml`

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

- `menu_nearby_media.xml`

- `menu_notification_well_button.xml`

- `menu_object.xml`

- `menu_object_icon.xml`

- `menu_outfit_gallery_sort.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_list_sort.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_contact_sets_add.xml`

- `menu_people_contact_sets_gear.xml`

- `menu_people_contact_sets_remove.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_perf_avatar_rendering_settings.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_mute_particle.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

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

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `panel_ao.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_contacts_sets.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_fs_performance_autotune.xml`

- `panel_fs_performance_complexity.xml`

- `panel_fs_performance_huds.xml`

- `panel_fs_performance_nearby.xml`

- `panel_fs_performance_preferences.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

- `panel_fs_settings_sky_atmos.xml`

- `panel_fs_settings_sky_clouds.xml`

- `panel_fs_settings_sky_sunmoon.xml`

- `panel_fs_settings_water.xml`

- `panel_fs_tools_texture.xml`

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

- `panel_instant_message.xml`

- `panel_inventory_gallery.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

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

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notifications_channel.xml`

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

- `panel_people_contact_sets.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_game_control.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_primfeed_account.xml`

- `panel_primfeed_photo.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_region_terrain_texture_transform.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

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

- `panel_toolbar_view.xml`

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

- `xui_version.xml`


## indra/newview/skins/default/xui/de/widgets/ (13 files)

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

- `person_view.xml`

- `sun_moon_trackball.xml`

- `texture_picker.xml`


## indra/newview/skins/default/xui/en/ (693 files)

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

- `floater_NACL_explore_sounds.xml`

- `floater_aaa.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_align.xml`

- `floater_avatar_align_mini.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_avatar_welcome_pack.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_beamcolor.xml`

- `floater_beamshape.xml`

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

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fbc_web.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_avatar_render_settings.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_blocklist.xml`

- `floater_fs_camera_small.xml`

- `floater_fs_contact_add.xml`

- `floater_fs_contact_set_configuration.xml`

- `floater_fs_contacts.xml`

- `floater_fs_discord.xml`

- `floater_fs_export.xml`

- `floater_fs_fixedenvironment.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_partial_inventory.xml`

- `floater_fs_performance.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_poser.xml`

- `floater_fs_posestand.xml`

- `floater_fs_protectedfolders.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_streamtitle.xml`

- `floater_fs_streamtitlehistory.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_fs_vram_usage.xml`

- `floater_fs_wearable_favorites.xml`

- `floater_gesture.xml`

- `floater_gesture_autocomplete_picker.xml`

- `floater_gltf_asset_editor.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_grid_status.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_join.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_live_material_editor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_maturity_dialog.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_my_web_profile.xml`

- `floater_new_feature_notification.xml`

- `floater_notification.xml`

- `floater_notifications_console.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_omnifilter.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_particle_editor.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_performance.xml`

- `floater_perms_default.xml`

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_primfeed.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restart_schedule.xml`

- `floater_region_restarting.xml`

- `floater_region_tracker.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_script_recover.xml`

- `floater_scripting_settings.xml`

- `floater_search.xml`

- `floater_search_replace.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_color.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_side_bar_tab.xml`

- `floater_simple_snapshot.xml`

- `floater_snapshot.xml`

- `floater_snapshot_guide_settings.xml`

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

- `floater_ui_preview.xml`

- `floater_url_entry.xml`

- `floater_vj_local_mesh.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_web_modal.xml`

- `floater_web_profile.xml`

- `floater_whitelist.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

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

- `menu_attachment_other.xml`

- `menu_attachment_self.xml`

- `menu_avatar_icon.xml`

- `menu_avatar_other.xml`

- `menu_avatar_rendering_settings.xml`

- `menu_avatar_rendering_settings_add.xml`

- `menu_avatar_self.xml`

- `menu_classifieds.xml`

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

- `menu_dir_people.xml`

- `menu_edit.xml`

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_asset_blacklist.xml`

- `menu_fs_avatar_render_setting.xml`

- `menu_fs_avatar_search.xml`

- `menu_fs_avatar_search_multiselect.xml`

- `menu_fs_block_list.xml`

- `menu_fs_bump_list.xml`

- `menu_fs_chat_options.xml`

- `menu_fs_contacts_friends.xml`

- `menu_fs_contacts_friends_multiselect.xml`

- `menu_fs_im_teleport.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_inspect_options.xml`

- `menu_fs_moneytracker_list.xml`

- `menu_fs_namelist_avatar.xml`

- `menu_fs_namelist_avatar_multiselect.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_fs_profile_image_actions.xml`

- `menu_fs_profile_name_field.xml`

- `menu_fs_profile_overflow.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_fs_wearable_favorites.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_custom_tab.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_inventory_view_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_lsl_font_size.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

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

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_contact_sets_add.xml`

- `menu_people_contact_sets_gear.xml`

- `menu_people_contact_sets_remove.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_perf_avatar_rendering_settings.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_mute_particle.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

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

- `menu_teleport_history_timezone.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `notification_visibility.xml`

- `notifications.xml`

- `outfit_accordion_tab.xml`

- `panel_active_object_row.xml`

- `panel_ao.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

- `panel_block_list_sidetray.xml`

- `panel_blocked_list_item.xml`

- `panel_body_parts_list_item.xml`

- `panel_bodyparts_list_button_bar.xml`

- `panel_button_checkbox.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_activeim_row.xml`

- `panel_fs_adhoc_control_panel.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_contacts_sets.xml`

- `panel_fs_group_control_panel.xml`

- `panel_fs_im_control_panel.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_fs_performance_autotune.xml`

- `panel_fs_performance_complexity.xml`

- `panel_fs_performance_huds.xml`

- `panel_fs_performance_nearby.xml`

- `panel_fs_performance_preferences.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

- `panel_fs_settings_sky_atmos.xml`

- `panel_fs_settings_sky_clouds.xml`

- `panel_fs_settings_sky_sunmoon.xml`

- `panel_fs_settings_water.xml`

- `panel_fs_tools_texture.xml`

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

- `panel_group_list_separator.xml`

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

- `panel_notification.xml`

- `panel_notification_list_item.xml`

- `panel_notification_script.xml`

- `panel_notifications_channel.xml`

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

- `panel_people_contact_sets.xml`

- `panel_performance_autoadjustments.xml`

- `panel_performance_autotune.xml`

- `panel_performance_complexity.xml`

- `panel_performance_huds.xml`

- `panel_performance_nearby.xml`

- `panel_performance_preferences.xml`

- `panel_pick_list_item.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_game_control.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_preferences_voice.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_primfeed_account.xml`

- `panel_primfeed_photo.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_region_terrain_texture_transform.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

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

- `panel_toolbar_view.xml`

- `panel_tools_texture.xml`

- `panel_topinfo_bar.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `rlva_strings.xml`

- `role_actions.xml`

- `script_editor.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`

- `xui_version.xml`


## indra/newview/skins/default/xui/en/widgets/ (110 files)

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

- `clothing_list_item.xml`

- `cof_wearable_list_item.xml`

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

- `fs_chat_history.xml`

- `fs_chiclet_im_adhoc.xml`

- `fs_chiclet_im_group.xml`

- `fs_chiclet_im_p2p.xml`

- `fs_nearby_chat_control.xml`

- `fs_nearby_chat_voice_monitor.xml`

- `fs_virtual_trackpad.xml`

- `gesture_combo_list.xml`

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

- `panel.xml`

- `panel_camera_item.xml`

- `person_tab_view.xml`

- `person_view.xml`

- `progress_bar.xml`

- `radio_group.xml`

- `radio_item.xml`

- `recent_inventory_panel.xml`

- `scroll_bar.xml`

- `scroll_column_header.xml`

- `scroll_container.xml`

- `scroll_list.xml`

- `scrolling_panel_list.xml`

- `search_combo_box.xml`

- `search_editor.xml`

- `side_tray.xml`

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

- `textbase.xml`

- `texture_picker.xml`

- `time.xml`

- `toggleable_menu.xml`

- `tool_tip.xml`

- `toolbar.xml`

- `toolbar_vertical.xml`

- `ui_ctrl.xml`

- `view_border.xml`

- `wearable_outfit_list_item.xml`

- `web_browser.xml`

- `window_shade.xml`

- `worn_inventory_panel.xml`

- `xy_vector.xml`


## indra/newview/skins/default/xui/es/ (473 files)

- `emoji_categories.xml`

- `floater_NACL_explore_sounds.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

- `floater_ao.xml`

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

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_contacts.xml`

- `floater_fs_export.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_posestand.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_notification.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_particle_editor.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_locks.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_script_recover.xml`

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

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_custom_tab.xml`

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

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

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

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `panel_ao.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_login.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

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

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notifications_channel.xml`

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

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

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

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

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

- `panel_toolbar_view.xml`

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

- `xui_version.xml`


## indra/newview/skins/default/xui/es/widgets/ (11 files)

- `bodyparts_list_item.xml`

- `clothing_list_item.xml`

- `deletable_wearable_list_item.xml`

- `density_ctrl.xml`

- `dummy_clothing_list_item.xml`

- `flat_list_view.xml`

- `inbox_folder_view_folder.xml`

- `inbox_folder_view_item.xml`

- `name_editor.xml`

- `person_view.xml`

- `texture_picker.xml`


## indra/newview/skins/default/xui/fr/ (623 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `floater_360capture.xml`

- `floater_NACL_explore_sounds.xml`

- `floater_aaa.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_add_payment_method.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_align.xml`

- `floater_avatar_align_mini.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_avatar_welcome_pack.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_beamcolor.xml`

- `floater_beamshape.xml`

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

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_avatar_render_settings.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_blocklist.xml`

- `floater_fs_camera_small.xml`

- `floater_fs_contact_add.xml`

- `floater_fs_contact_set_configuration.xml`

- `floater_fs_contacts.xml`

- `floater_fs_discord.xml`

- `floater_fs_export.xml`

- `floater_fs_fixedenvironment.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_partial_inventory.xml`

- `floater_fs_performance.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_poser.xml`

- `floater_fs_posestand.xml`

- `floater_fs_protectedfolders.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_streamtitle.xml`

- `floater_fs_streamtitlehistory.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_fs_vram_usage.xml`

- `floater_fs_wearable_favorites.xml`

- `floater_gesture.xml`

- `floater_gesture_autocomplete_picker.xml`

- `floater_gltf_asset_editor.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_live_material_editor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_maturity_dialog.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_new_feature_notification.xml`

- `floater_notification.xml`

- `floater_notifications_console.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_omnifilter.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_particle_editor.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_primfeed.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restart_schedule.xml`

- `floater_region_restarting.xml`

- `floater_region_tracker.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_script_recover.xml`

- `floater_scripting_settings.xml`

- `floater_search.xml`

- `floater_search_replace.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_color.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_simple_snapshot.xml`

- `floater_snapshot.xml`

- `floater_snapshot_guide_settings.xml`

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

- `floater_test_radiogroup.xml`

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

- `floater_ui_preview.xml`

- `floater_url_entry.xml`

- `floater_vj_local_mesh.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist.xml`

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

- `menu_classifieds.xml`

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

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_asset_blacklist.xml`

- `menu_fs_avatar_render_setting.xml`

- `menu_fs_avatar_search.xml`

- `menu_fs_avatar_search_multiselect.xml`

- `menu_fs_block_list.xml`

- `menu_fs_bump_list.xml`

- `menu_fs_chat_options.xml`

- `menu_fs_contacts_friends.xml`

- `menu_fs_contacts_friends_multiselect.xml`

- `menu_fs_im_teleport.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_inspect_options.xml`

- `menu_fs_moneytracker_list.xml`

- `menu_fs_namelist_avatar.xml`

- `menu_fs_namelist_avatar_multiselect.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_fs_profile_image_actions.xml`

- `menu_fs_profile_name_field.xml`

- `menu_fs_profile_overflow.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_fs_wearable_favorites.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_custom_tab.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_inventory_view_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_lsl_font_size.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

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

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_contact_sets_add.xml`

- `menu_people_contact_sets_gear.xml`

- `menu_people_contact_sets_remove.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_perf_avatar_rendering_settings.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_mute_particle.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

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

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `panel_ao.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_contacts_sets.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_fs_performance_autotune.xml`

- `panel_fs_performance_complexity.xml`

- `panel_fs_performance_huds.xml`

- `panel_fs_performance_nearby.xml`

- `panel_fs_performance_preferences.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

- `panel_fs_settings_sky_atmos.xml`

- `panel_fs_settings_sky_clouds.xml`

- `panel_fs_settings_sky_sunmoon.xml`

- `panel_fs_settings_water.xml`

- `panel_fs_tools_texture.xml`

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

- `panel_inventory_gallery.xml`

- `panel_inventory_gallery_item.xml`

- `panel_landmark_info.xml`

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

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notifications_channel.xml`

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

- `panel_people_contact_sets.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_preferences_voice.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_primfeed_account.xml`

- `panel_primfeed_photo.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_region_terrain_texture_transform.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_scrolling_param.xml`

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

- `xui_version.xml`


## indra/newview/skins/default/xui/fr/widgets/ (13 files)

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

- `person_view.xml`

- `sun_moon_trackball.xml`

- `texture_picker.xml`


## indra/newview/skins/default/xui/it/ (567 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `floater_360capture.xml`

- `floater_NACL_explore_sounds.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_beamcolor.xml`

- `floater_beamshape.xml`

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

- `floater_choose_group.xml`

- `floater_color_picker.xml`

- `floater_combobox_ok_cancel.xml`

- `floater_conversation_log.xml`

- `floater_conversation_preview.xml`

- `floater_create_landmark.xml`

- `floater_critical.xml`

- `floater_delete_pref_preset.xml`

- `floater_destinations.xml`

- `floater_display_name.xml`

- `floater_edit_ext_day_cycle.xml`

- `floater_edit_hover_height.xml`

- `floater_emoji_picker.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_avatar_render_settings.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_blocklist.xml`

- `floater_fs_camera_small.xml`

- `floater_fs_contact_add.xml`

- `floater_fs_contact_set_configuration.xml`

- `floater_fs_contacts.xml`

- `floater_fs_export.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_partial_inventory.xml`

- `floater_fs_performance.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_poser.xml`

- `floater_fs_posestand.xml`

- `floater_fs_protectedfolders.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_streamtitle.xml`

- `floater_fs_streamtitlehistory.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_fs_wearable_favorites.xml`

- `floater_gesture.xml`

- `floater_gltf_asset_editor.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_live_material_editor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_new_feature_notification.xml`

- `floater_notification.xml`

- `floater_notifications_console.xml`

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

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restart_schedule.xml`

- `floater_region_restarting.xml`

- `floater_region_tracker.xml`

- `floater_report_abuse.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_search_replace.xml`

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

- `floater_vj_local_mesh.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist.xml`

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

- `menu_classifieds.xml`

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

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_avatar_render_setting.xml`

- `menu_fs_avatar_search.xml`

- `menu_fs_avatar_search_multiselect.xml`

- `menu_fs_block_list.xml`

- `menu_fs_chat_options.xml`

- `menu_fs_contacts_friends.xml`

- `menu_fs_contacts_friends_multiselect.xml`

- `menu_fs_im_teleport.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_inspect_options.xml`

- `menu_fs_namelist_avatar.xml`

- `menu_fs_namelist_avatar_multiselect.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_fs_profile_image_actions.xml`

- `menu_fs_profile_name_field.xml`

- `menu_fs_profile_overflow.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_fs_wearable_favorites.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_custom_tab.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_inventory_view_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_lsl_font_size.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

- `menu_mini_map.xml`

- `menu_model_import_gear_default.xml`

- `menu_mute_particle.xml`

- `menu_navbar.xml`

- `menu_nearby_chat.xml`

- `menu_nearby_media.xml`

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

- `menu_people_contact_sets_add.xml`

- `menu_people_contact_sets_gear.xml`

- `menu_people_contact_sets_remove.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_perf_avatar_rendering_settings.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

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

- `menu_teleport_history_timezone.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `panel_ao.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_contacts_sets.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_fs_performance_autotune.xml`

- `panel_fs_performance_complexity.xml`

- `panel_fs_performance_huds.xml`

- `panel_fs_performance_nearby.xml`

- `panel_fs_performance_preferences.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

- `panel_fs_tools_texture.xml`

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

- `panel_instant_message.xml`

- `panel_inventory_item.xml`

- `panel_landmark_info.xml`

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

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notifications_channel.xml`

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

- `panel_people_contact_sets.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

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

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_region_terrain_texture_transform.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

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

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

- `panel_toolbar_view.xml`

- `panel_tools_texture.xml`

- `panel_topinfo_bar.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `role_actions.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`


## indra/newview/skins/default/xui/it/widgets/ (12 files)

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

- `person_view.xml`

- `sun_moon_trackball.xml`


## indra/newview/skins/default/xui/ja/ (637 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `floater_360capture.xml`

- `floater_NACL_explore_sounds.xml`

- `floater_aaa.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_align.xml`

- `floater_avatar_align_mini.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_avatar_welcome_pack.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_beamcolor.xml`

- `floater_beamshape.xml`

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

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_avatar_render_settings.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_blocklist.xml`

- `floater_fs_camera_small.xml`

- `floater_fs_contact_add.xml`

- `floater_fs_contact_set_configuration.xml`

- `floater_fs_contacts.xml`

- `floater_fs_discord.xml`

- `floater_fs_export.xml`

- `floater_fs_fixedenvironment.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_partial_inventory.xml`

- `floater_fs_performance.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_poser.xml`

- `floater_fs_posestand.xml`

- `floater_fs_protectedfolders.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_streamtitle.xml`

- `floater_fs_streamtitlehistory.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_fs_vram_usage.xml`

- `floater_fs_wearable_favorites.xml`

- `floater_gesture.xml`

- `floater_gesture_autocomplete_picker.xml`

- `floater_gltf_asset_editor.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_live_material_editor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_maturity_dialog.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_new_feature_notification.xml`

- `floater_notification.xml`

- `floater_notifications_console.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_omnifilter.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_particle_editor.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_performance.xml`

- `floater_perms_default.xml`

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_primfeed.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restart_schedule.xml`

- `floater_region_restarting.xml`

- `floater_region_tracker.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_script_recover.xml`

- `floater_search.xml`

- `floater_search_replace.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_color.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_simple_snapshot.xml`

- `floater_snapshot.xml`

- `floater_snapshot_guide_settings.xml`

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

- `floater_ui_preview.xml`

- `floater_url_entry.xml`

- `floater_vj_local_mesh.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist.xml`

- `floater_whitelist_entry.xml`

- `floater_window_size.xml`

- `floater_world_map.xml`

- `fonts.xml`

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

- `menu_classifieds.xml`

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

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_asset_blacklist.xml`

- `menu_fs_avatar_render_setting.xml`

- `menu_fs_avatar_search.xml`

- `menu_fs_avatar_search_multiselect.xml`

- `menu_fs_block_list.xml`

- `menu_fs_bump_list.xml`

- `menu_fs_chat_options.xml`

- `menu_fs_contacts_friends.xml`

- `menu_fs_contacts_friends_multiselect.xml`

- `menu_fs_im_teleport.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_inspect_options.xml`

- `menu_fs_moneytracker_list.xml`

- `menu_fs_namelist_avatar.xml`

- `menu_fs_namelist_avatar_multiselect.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_fs_profile_image_actions.xml`

- `menu_fs_profile_name_field.xml`

- `menu_fs_profile_overflow.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_fs_wearable_favorites.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_custom_tab.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_inventory_view_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_lsl_font_size.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

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

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_contact_sets_add.xml`

- `menu_people_contact_sets_gear.xml`

- `menu_people_contact_sets_remove.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_perf_avatar_rendering_settings.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_mute_particle.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

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

- `menu_teleport_history_timezone.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `panel_ao.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_contacts_sets.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_fs_performance_autotune.xml`

- `panel_fs_performance_complexity.xml`

- `panel_fs_performance_huds.xml`

- `panel_fs_performance_nearby.xml`

- `panel_fs_performance_preferences.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

- `panel_fs_settings_sky_atmos.xml`

- `panel_fs_settings_sky_clouds.xml`

- `panel_fs_settings_sky_sunmoon.xml`

- `panel_fs_settings_water.xml`

- `panel_fs_tools_texture.xml`

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

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification.xml`

- `panel_notification_list_item.xml`

- `panel_notification_script.xml`

- `panel_notifications_channel.xml`

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

- `panel_people_contact_sets.xml`

- `panel_performance_autoadjustments.xml`

- `panel_performance_autotune.xml`

- `panel_performance_complexity.xml`

- `panel_performance_huds.xml`

- `panel_performance_nearby.xml`

- `panel_performance_preferences.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_primfeed_account.xml`

- `panel_primfeed_photo.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_region_terrain_texture_transform.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_script_question_toast.xml`

- `panel_scrolling_param.xml`

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


## indra/newview/skins/default/xui/ja/widgets/ (17 files)

- `bodyparts_list_item.xml`

- `clothing_list_item.xml`

- `deletable_wearable_list_item.xml`

- `density_ctrl.xml`

- `dummy_clothing_list_item.xml`

- `flat_list_view.xml`

- `inbox_folder_view_folder.xml`

- `inbox_folder_view_item.xml`

- `inventory_list_item.xml`

- `menu_item_separator.xml`

- `menu_item_tear_off.xml`

- `name_editor.xml`

- `panel_camera_item.xml`

- `person_view.xml`

- `sun_moon_trackball.xml`

- `wearable_outfit_list_item.xml`

- `xy_vector.xml`


## indra/newview/skins/default/xui/pl/ (605 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `floater_360capture.xml`

- `floater_NACL_explore_sounds.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_align.xml`

- `floater_avatar_align_mini.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_avatar_welcome_pack.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_beamcolor.xml`

- `floater_beamshape.xml`

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

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_avatar_render_settings.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_blocklist.xml`

- `floater_fs_camera_small.xml`

- `floater_fs_contact_add.xml`

- `floater_fs_contact_set_configuration.xml`

- `floater_fs_contacts.xml`

- `floater_fs_discord.xml`

- `floater_fs_export.xml`

- `floater_fs_fixedenvironment.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_partial_inventory.xml`

- `floater_fs_performance.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_poser.xml`

- `floater_fs_posestand.xml`

- `floater_fs_protectedfolders.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_streamtitle.xml`

- `floater_fs_streamtitlehistory.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_fs_vram_usage.xml`

- `floater_fs_wearable_favorites.xml`

- `floater_gesture.xml`

- `floater_gesture_autocomplete_picker.xml`

- `floater_gltf_asset_editor.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_live_material_editor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_maturity_dialog.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_new_feature_notification.xml`

- `floater_notification.xml`

- `floater_notifications_console.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_omnifilter.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_particle_editor.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_perms_default.xml`

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_primfeed.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restart_schedule.xml`

- `floater_region_restarting.xml`

- `floater_region_tracker.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_script_recover.xml`

- `floater_scripting_settings.xml`

- `floater_search.xml`

- `floater_search_replace.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_color.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_simple_snapshot.xml`

- `floater_snapshot.xml`

- `floater_snapshot_guide_settings.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_task_properties.xml`

- `floater_telehub.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_url_entry.xml`

- `floater_vj_local_mesh.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist.xml`

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

- `menu_classifieds.xml`

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

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_asset_blacklist.xml`

- `menu_fs_avatar_render_setting.xml`

- `menu_fs_avatar_search.xml`

- `menu_fs_avatar_search_multiselect.xml`

- `menu_fs_block_list.xml`

- `menu_fs_bump_list.xml`

- `menu_fs_chat_options.xml`

- `menu_fs_contacts_friends.xml`

- `menu_fs_contacts_friends_multiselect.xml`

- `menu_fs_im_teleport.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_inspect_options.xml`

- `menu_fs_moneytracker_list.xml`

- `menu_fs_namelist_avatar.xml`

- `menu_fs_namelist_avatar_multiselect.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_fs_profile_image_actions.xml`

- `menu_fs_profile_name_field.xml`

- `menu_fs_profile_overflow.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_fs_wearable_favorites.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_custom_tab.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_inventory_view_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_lsl_font_size.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

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

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_contact_sets_add.xml`

- `menu_people_contact_sets_gear.xml`

- `menu_people_contact_sets_remove.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_perf_avatar_rendering_settings.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_mute_particle.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

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

- `menu_teleport_history_timezone.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `panel_ao.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_contacts_sets.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_fs_performance_autotune.xml`

- `panel_fs_performance_complexity.xml`

- `panel_fs_performance_huds.xml`

- `panel_fs_performance_nearby.xml`

- `panel_fs_performance_preferences.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

- `panel_fs_settings_sky_atmos.xml`

- `panel_fs_settings_sky_clouds.xml`

- `panel_fs_settings_sky_sunmoon.xml`

- `panel_fs_settings_water.xml`

- `panel_fs_tools_texture.xml`

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

- `panel_inventory_gallery.xml`

- `panel_landmark_info.xml`

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

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notifications_channel.xml`

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

- `panel_people_contact_sets.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_preferences_voice.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_primfeed_account.xml`

- `panel_primfeed_photo.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_region_terrain_texture_transform.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

- `panel_script_experience.xml`

- `panel_script_limits_my_avatar.xml`

- `panel_script_limits_region_memory.xml`

- `panel_scrolling_param.xml`

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

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

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


## indra/newview/skins/default/xui/pl/widgets/ (11 files)

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

- `person_view.xml`


## indra/newview/skins/default/xui/pt/ (628 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `floater_360capture.xml`

- `floater_NACL_explore_sounds.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_add_payment_method.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_align.xml`

- `floater_avatar_align_mini.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_avatar_welcome_pack.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_beamcolor.xml`

- `floater_beamshape.xml`

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

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_avatar_render_settings.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_blocklist.xml`

- `floater_fs_camera_small.xml`

- `floater_fs_contact_add.xml`

- `floater_fs_contact_set_configuration.xml`

- `floater_fs_contacts.xml`

- `floater_fs_discord.xml`

- `floater_fs_export.xml`

- `floater_fs_fixedenvironment.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_partial_inventory.xml`

- `floater_fs_performance.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_poser.xml`

- `floater_fs_posestand.xml`

- `floater_fs_protectedfolders.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_streamtitle.xml`

- `floater_fs_streamtitlehistory.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_fs_vram_usage.xml`

- `floater_fs_wearable_favorites.xml`

- `floater_gesture.xml`

- `floater_gesture_autocomplete_picker.xml`

- `floater_gltf_asset_editor.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_live_material_editor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_maturity_dialog.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_new_feature_notification.xml`

- `floater_notification.xml`

- `floater_notifications_console.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_omnifilter.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_particle_editor.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_performance.xml`

- `floater_perms_default.xml`

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_primfeed.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restart_schedule.xml`

- `floater_region_restarting.xml`

- `floater_region_tracker.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_debug_panel.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_script_recover.xml`

- `floater_scripting_settings.xml`

- `floater_search.xml`

- `floater_search_replace.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_color.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_simple_snapshot.xml`

- `floater_snapshot.xml`

- `floater_snapshot_guide_settings.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_task_properties.xml`

- `floater_telehub.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_ui_preview.xml`

- `floater_url_entry.xml`

- `floater_vj_local_mesh.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist.xml`

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

- `menu_classifieds.xml`

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

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_asset_blacklist.xml`

- `menu_fs_avatar_render_setting.xml`

- `menu_fs_avatar_search.xml`

- `menu_fs_avatar_search_multiselect.xml`

- `menu_fs_block_list.xml`

- `menu_fs_bump_list.xml`

- `menu_fs_chat_options.xml`

- `menu_fs_contacts_friends.xml`

- `menu_fs_contacts_friends_multiselect.xml`

- `menu_fs_im_teleport.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_inspect_options.xml`

- `menu_fs_moneytracker_list.xml`

- `menu_fs_namelist_avatar.xml`

- `menu_fs_namelist_avatar_multiselect.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_fs_profile_image_actions.xml`

- `menu_fs_profile_name_field.xml`

- `menu_fs_profile_overflow.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_fs_wearable_favorites.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_custom_tab.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_inventory_view_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_lsl_font_size.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

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

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_contact_sets_add.xml`

- `menu_people_contact_sets_gear.xml`

- `menu_people_contact_sets_remove.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_perf_avatar_rendering_settings.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_mute_particle.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

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

- `menu_teleport_history_timezone.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `panel_ao.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_contacts_sets.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_fs_performance_autotune.xml`

- `panel_fs_performance_complexity.xml`

- `panel_fs_performance_huds.xml`

- `panel_fs_performance_nearby.xml`

- `panel_fs_performance_preferences.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

- `panel_fs_settings_sky_atmos.xml`

- `panel_fs_settings_sky_clouds.xml`

- `panel_fs_settings_sky_sunmoon.xml`

- `panel_fs_settings_water.xml`

- `panel_fs_tools_texture.xml`

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

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notifications_channel.xml`

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

- `panel_people_contact_sets.xml`

- `panel_performance_autoadjustments.xml`

- `panel_performance_autotune.xml`

- `panel_performance_complexity.xml`

- `panel_performance_huds.xml`

- `panel_performance_nearby.xml`

- `panel_performance_preferences.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_preferences_voice.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_primfeed_account.xml`

- `panel_primfeed_photo.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_region_terrain_texture_transform.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

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

- `panel_toolbar_view.xml`

- `panel_tools_texture.xml`

- `panel_topinfo_bar.xml`

- `panel_volume_pulldown.xml`

- `panel_world_map.xml`

- `rlva_strings.xml`

- `role_actions.xml`

- `settings_comments.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_item_info.xml`

- `sidepanel_task_info.xml`

- `strings.xml`

- `teleport_strings.xml`

- `xui_version.xml`


## indra/newview/skins/default/xui/pt/widgets/ (13 files)

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

- `person_view.xml`

- `sun_moon_trackball.xml`

- `texture_picker.xml`


## indra/newview/skins/default/xui/ru/ (579 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `floater_360capture.xml`

- `floater_NACL_explore_sounds.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_add_payment_method.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

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

- `floater_beamcolor.xml`

- `floater_beamshape.xml`

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

- `floater_change_item_thumbnail.xml`

- `floater_chat_mention_picker.xml`

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

- `floater_emoji_picker.xml`

- `floater_event.xml`

- `floater_experience_search.xml`

- `floater_experienceprofile.xml`

- `floater_experiences.xml`

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_avatar_render_settings.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_blocklist.xml`

- `floater_fs_camera_small.xml`

- `floater_fs_contact_add.xml`

- `floater_fs_contact_set_configuration.xml`

- `floater_fs_contacts.xml`

- `floater_fs_discord.xml`

- `floater_fs_export.xml`

- `floater_fs_fixedenvironment.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_partial_inventory.xml`

- `floater_fs_performance.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_poser.xml`

- `floater_fs_posestand.xml`

- `floater_fs_protectedfolders.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_streamtitle.xml`

- `floater_fs_streamtitlehistory.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_fs_vram_usage.xml`

- `floater_fs_wearable_favorites.xml`

- `floater_gesture.xml`

- `floater_gltf_asset_editor.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_new_feature_notification.xml`

- `floater_notification.xml`

- `floater_notifications_console.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_particle_editor.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_performance.xml`

- `floater_perms_default.xml`

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_primfeed.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restarting.xml`

- `floater_region_tracker.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_script_recover.xml`

- `floater_search_replace.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

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

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_ui_preview.xml`

- `floater_url_entry.xml`

- `floater_vj_local_mesh.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist.xml`

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

- `menu_classifieds.xml`

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

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_asset_blacklist.xml`

- `menu_fs_avatar_render_setting.xml`

- `menu_fs_avatar_search.xml`

- `menu_fs_avatar_search_multiselect.xml`

- `menu_fs_block_list.xml`

- `menu_fs_bump_list.xml`

- `menu_fs_chat_options.xml`

- `menu_fs_contacts_friends.xml`

- `menu_fs_contacts_friends_multiselect.xml`

- `menu_fs_im_teleport.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_inspect_options.xml`

- `menu_fs_moneytracker_list.xml`

- `menu_fs_namelist_avatar.xml`

- `menu_fs_namelist_avatar_multiselect.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_fs_profile_image_actions.xml`

- `menu_fs_profile_name_field.xml`

- `menu_fs_profile_overflow.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_fs_wearable_favorites.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_custom_tab.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_inventory_view_default.xml`

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

- `menu_outfit_gallery_sort.xml`

- `menu_outfit_gear.xml`

- `menu_outfit_list_sort.xml`

- `menu_outfit_tab.xml`

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_contact_sets_add.xml`

- `menu_people_contact_sets_gear.xml`

- `menu_people_contact_sets_remove.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_perf_avatar_rendering_settings.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_mute_particle.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

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

- `menu_teleport_history_timezone.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `panel_ao.xml`

- `panel_avatar_list_item.xml`

- `panel_avatar_tag.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_contacts_sets.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_fs_performance_autotune.xml`

- `panel_fs_performance_complexity.xml`

- `panel_fs_performance_huds.xml`

- `panel_fs_performance_nearby.xml`

- `panel_fs_performance_preferences.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

- `panel_fs_settings_sky_atmos.xml`

- `panel_fs_settings_sky_clouds.xml`

- `panel_fs_settings_sky_sunmoon.xml`

- `panel_fs_settings_water.xml`

- `panel_fs_tools_texture.xml`

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

- `panel_inventory_gallery.xml`

- `panel_inventory_gallery_item.xml`

- `panel_landmark_info.xml`

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

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notifications_channel.xml`

- `panel_notify_textbox.xml`

- `panel_outfit_edit.xml`

- `panel_outfit_gallery.xml`

- `panel_outfit_snapshot_inventory.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_inventory_gear_default.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_people_contact_sets.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_primfeed_account.xml`

- `panel_primfeed_photo.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

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

- `panel_sys_well_item.xml`

- `panel_teleport_history.xml`

- `panel_teleport_history_item.xml`

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


## indra/newview/skins/default/xui/ru/widgets/ (11 files)

- `bodyparts_list_item.xml`

- `clothing_list_item.xml`

- `deletable_wearable_list_item.xml`

- `density_ctrl.xml`

- `dummy_clothing_list_item.xml`

- `flat_list_view.xml`

- `inbox_folder_view_folder.xml`

- `inbox_folder_view_item.xml`

- `name_editor.xml`

- `person_view.xml`

- `sun_moon_trackball.xml`


## indra/newview/skins/default/xui/tr/ (389 files)

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

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_voice_controls.xml`

- `floater_gesture.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_live_lsleditor.xml`

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

- `floater_notification.xml`

- `floater_notifications_console.xml`

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

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

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

- `menu_inspect_self_gear.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_login.xml`

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

- `panel_script_ed.xml`

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


## indra/newview/skins/default/xui/zh/ (623 files)

- `control_table_contents_camera.xml`

- `control_table_contents_columns_basic.xml`

- `control_table_contents_editing.xml`

- `control_table_contents_media.xml`

- `control_table_contents_movement.xml`

- `emoji_categories.xml`

- `floater_360capture.xml`

- `floater_NACL_explore_sounds.xml`

- `floater_about.xml`

- `floater_about_land.xml`

- `floater_activeim.xml`

- `floater_adjust_environment.xml`

- `floater_animation_anim_preview.xml`

- `floater_animation_bvh_preview.xml`

- `floater_animation_explorer.xml`

- `floater_ao.xml`

- `floater_associate_listing.xml`

- `floater_auction.xml`

- `floater_autoreplace.xml`

- `floater_avatar.xml`

- `floater_avatar_align.xml`

- `floater_avatar_align_mini.xml`

- `floater_avatar_picker.xml`

- `floater_avatar_render_settings.xml`

- `floater_avatar_textures.xml`

- `floater_avatar_welcome_pack.xml`

- `floater_ban_duration.xml`

- `floater_beacons.xml`

- `floater_beamcolor.xml`

- `floater_beamshape.xml`

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

- `floater_export_collada.xml`

- `floater_fast_timers.xml`

- `floater_fixedenvironment.xml`

- `floater_flickr.xml`

- `floater_font_test.xml`

- `floater_forget_user.xml`

- `floater_fs_area_search.xml`

- `floater_fs_asset_blacklist.xml`

- `floater_fs_avatar_render_settings.xml`

- `floater_fs_big_preview.xml`

- `floater_fs_blocklist.xml`

- `floater_fs_camera_small.xml`

- `floater_fs_contact_add.xml`

- `floater_fs_contact_set_configuration.xml`

- `floater_fs_contacts.xml`

- `floater_fs_discord.xml`

- `floater_fs_export.xml`

- `floater_fs_fixedenvironment.xml`

- `floater_fs_group.xml`

- `floater_fs_group_titles.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_import.xml`

- `floater_fs_money_tracker.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_partial_inventory.xml`

- `floater_fs_performance.xml`

- `floater_fs_placedetails.xml`

- `floater_fs_poser.xml`

- `floater_fs_posestand.xml`

- `floater_fs_protectedfolders.xml`

- `floater_fs_radar.xml`

- `floater_fs_search.xml`

- `floater_fs_splash_screen_settings.xml`

- `floater_fs_streamtitle.xml`

- `floater_fs_streamtitlehistory.xml`

- `floater_fs_teleporthistory.xml`

- `floater_fs_voice_controls.xml`

- `floater_fs_volume_controls.xml`

- `floater_fs_vram_usage.xml`

- `floater_fs_wearable_favorites.xml`

- `floater_gesture.xml`

- `floater_gesture_autocomplete_picker.xml`

- `floater_gltf_asset_editor.xml`

- `floater_god_tools.xml`

- `floater_goto_line.xml`

- `floater_help_browser.xml`

- `floater_hud.xml`

- `floater_im_container.xml`

- `floater_im_session.xml`

- `floater_image_preview.xml`

- `floater_import_collada.xml`

- `floater_incoming_call.xml`

- `floater_inspect.xml`

- `floater_inventory_item_properties.xml`

- `floater_inventory_settings.xml`

- `floater_inventory_thumbnails_helper.xml`

- `floater_inventory_view_finder.xml`

- `floater_item_properties.xml`

- `floater_joystick.xml`

- `floater_lagmeter.xml`

- `floater_land_holdings.xml`

- `floater_linkreplace.xml`

- `floater_live_lsleditor.xml`

- `floater_live_material_editor.xml`

- `floater_load_pref_preset.xml`

- `floater_lsl_guide.xml`

- `floater_map.xml`

- `floater_marketplace.xml`

- `floater_marketplace_listings.xml`

- `floater_marketplace_validation.xml`

- `floater_material_editor.xml`

- `floater_maturity_dialog.xml`

- `floater_media_browser.xml`

- `floater_media_lists.xml`

- `floater_media_settings.xml`

- `floater_mem_leaking.xml`

- `floater_model_preview.xml`

- `floater_moveview.xml`

- `floater_mute_object.xml`

- `floater_my_appearance.xml`

- `floater_my_environments.xml`

- `floater_my_inventory.xml`

- `floater_my_scripts.xml`

- `floater_new_feature_notification.xml`

- `floater_notification.xml`

- `floater_notifications_console.xml`

- `floater_notifications_tabbed.xml`

- `floater_object_weights.xml`

- `floater_omnifilter.xml`

- `floater_openobject.xml`

- `floater_outfit_save_as.xml`

- `floater_outgoing_call.xml`

- `floater_particle_editor.xml`

- `floater_pathfinding_characters.xml`

- `floater_pathfinding_console.xml`

- `floater_pathfinding_linksets.xml`

- `floater_pay.xml`

- `floater_pay_object.xml`

- `floater_people.xml`

- `floater_performance.xml`

- `floater_perms_default.xml`

- `floater_phototools.xml`

- `floater_phototools_camera.xml`

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

- `floater_primfeed.xml`

- `floater_profile.xml`

- `floater_profile_permissions.xml`

- `floater_profile_texture.xml`

- `floater_publish_classified.xml`

- `floater_quickprefs.xml`

- `floater_region_debug_console.xml`

- `floater_region_info.xml`

- `floater_region_restart_schedule.xml`

- `floater_region_restarting.xml`

- `floater_region_tracker.xml`

- `floater_report_abuse.xml`

- `floater_rlv_behaviours.xml`

- `floater_rlv_console.xml`

- `floater_rlv_locks.xml`

- `floater_rlv_strings.xml`

- `floater_save_camera_preset.xml`

- `floater_save_pref_preset.xml`

- `floater_scene_load_stats.xml`

- `floater_script_debug.xml`

- `floater_script_ed_prefs.xml`

- `floater_script_limits.xml`

- `floater_script_preview.xml`

- `floater_script_queue.xml`

- `floater_script_recover.xml`

- `floater_scripting_settings.xml`

- `floater_search.xml`

- `floater_search_replace.xml`

- `floater_select_key.xml`

- `floater_sell_land.xml`

- `floater_settings_color.xml`

- `floater_settings_debug.xml`

- `floater_settings_picker.xml`

- `floater_simple_snapshot.xml`

- `floater_snapshot.xml`

- `floater_snapshot_guide_settings.xml`

- `floater_sound_preview.xml`

- `floater_spellcheck.xml`

- `floater_spellcheck_import.xml`

- `floater_stats.xml`

- `floater_sys_well.xml`

- `floater_task_properties.xml`

- `floater_telehub.xml`

- `floater_test_layout_stacks.xml`

- `floater_test_text_vertical_aligment.xml`

- `floater_texture_ctrl.xml`

- `floater_tools.xml`

- `floater_top_objects.xml`

- `floater_tos.xml`

- `floater_toybox.xml`

- `floater_translation_settings.xml`

- `floater_ui_preview.xml`

- `floater_url_entry.xml`

- `floater_vj_local_mesh.xml`

- `floater_voice_chat_volume.xml`

- `floater_voice_volume.xml`

- `floater_web_content.xml`

- `floater_whitelist.xml`

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

- `menu_classifieds.xml`

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

- `menu_embedded_item.xml`

- `menu_favorites.xml`

- `menu_fs_area_search.xml`

- `menu_fs_asset_blacklist.xml`

- `menu_fs_avatar_render_setting.xml`

- `menu_fs_avatar_search.xml`

- `menu_fs_avatar_search_multiselect.xml`

- `menu_fs_block_list.xml`

- `menu_fs_bump_list.xml`

- `menu_fs_chat_options.xml`

- `menu_fs_contacts_friends.xml`

- `menu_fs_contacts_friends_multiselect.xml`

- `menu_fs_im_teleport.xml`

- `menu_fs_im_well_button.xml`

- `menu_fs_imchiclet_adhoc.xml`

- `menu_fs_imchiclet_group.xml`

- `menu_fs_imchiclet_p2p.xml`

- `menu_fs_inspect_options.xml`

- `menu_fs_moneytracker_list.xml`

- `menu_fs_namelist_avatar.xml`

- `menu_fs_namelist_avatar_multiselect.xml`

- `menu_fs_poser_poses_btn.xml`

- `menu_fs_profile_image_actions.xml`

- `menu_fs_profile_name_field.xml`

- `menu_fs_profile_overflow.xml`

- `menu_fs_radar.xml`

- `menu_fs_radar_multiselect.xml`

- `menu_fs_radar_options.xml`

- `menu_fs_wearable_favorites.xml`

- `menu_gallery_inventory.xml`

- `menu_gallery_outfit_tab.xml`

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

- `menu_inspect_self_gear.xml`

- `menu_inv_offer_chiclet.xml`

- `menu_inventory.xml`

- `menu_inventory_add.xml`

- `menu_inventory_custom_tab.xml`

- `menu_inventory_gear_default.xml`

- `menu_inventory_search_visibility.xml`

- `menu_inventory_view_default.xml`

- `menu_land.xml`

- `menu_landmark.xml`

- `menu_login.xml`

- `menu_lsl_font_size.xml`

- `menu_marketplace_view.xml`

- `menu_media_ctrl.xml`

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

- `menu_participant_list.xml`

- `menu_participant_view.xml`

- `menu_people_blocked_gear.xml`

- `menu_people_blocked_plus.xml`

- `menu_people_blocked_view.xml`

- `menu_people_contact_sets_add.xml`

- `menu_people_contact_sets_gear.xml`

- `menu_people_contact_sets_remove.xml`

- `menu_people_friends_view.xml`

- `menu_people_groups.xml`

- `menu_people_groups_view.xml`

- `menu_people_nearby.xml`

- `menu_people_nearby_multiselect.xml`

- `menu_people_nearby_view.xml`

- `menu_people_recent_view.xml`

- `menu_perf_avatar_rendering_settings.xml`

- `menu_picks.xml`

- `menu_picks_plus.xml`

- `menu_pie_attachment_other.xml`

- `menu_pie_attachment_self.xml`

- `menu_pie_avatar_other.xml`

- `menu_pie_avatar_self.xml`

- `menu_pie_land.xml`

- `menu_pie_mute_particle.xml`

- `menu_pie_object.xml`

- `menu_place.xml`

- `menu_place_add_button.xml`

- `menu_places_gear_folder.xml`

- `menu_places_gear_landmark.xml`

- `menu_places_gear_sorting.xml`

- `menu_profile_other.xml`

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

- `menu_teleport_history_timezone.xml`

- `menu_text_editor.xml`

- `menu_toolbars.xml`

- `menu_toolbars_horizontal.xml`

- `menu_toolbars_vertical.xml`

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

- `panel_ao.xml`

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

- `panel_flickr_account.xml`

- `panel_flickr_photo.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_contacts_groups.xml`

- `panel_fs_contacts_sets.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_fs_performance_autotune.xml`

- `panel_fs_performance_complexity.xml`

- `panel_fs_performance_huds.xml`

- `panel_fs_performance_nearby.xml`

- `panel_fs_performance_preferences.xml`

- `panel_fs_radar.xml`

- `panel_fs_search_legacy_classifieds.xml`

- `panel_fs_search_legacy_events.xml`

- `panel_fs_search_legacy_groups.xml`

- `panel_fs_search_legacy_land.xml`

- `panel_fs_search_legacy_people.xml`

- `panel_fs_search_legacy_places.xml`

- `panel_fs_search_legacy_web.xml`

- `panel_fs_settings_sky_atmos.xml`

- `panel_fs_settings_sky_clouds.xml`

- `panel_fs_settings_sky_sunmoon.xml`

- `panel_fs_settings_water.xml`

- `panel_fs_tools_texture.xml`

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

- `panel_nearby_chat_bar.xml`

- `panel_nearby_media.xml`

- `panel_notification_list_item.xml`

- `panel_notifications_channel.xml`

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

- `panel_people_contact_sets.xml`

- `panel_performance_autoadjustments.xml`

- `panel_performance_autotune.xml`

- `panel_performance_complexity.xml`

- `panel_performance_huds.xml`

- `panel_performance_nearby.xml`

- `panel_performance_preferences.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_postcard_message.xml`

- `panel_postcard_settings.xml`

- `panel_preferences_UI.xml`

- `panel_preferences_advanced.xml`

- `panel_preferences_alerts.xml`

- `panel_preferences_backup.xml`

- `panel_preferences_chat.xml`

- `panel_preferences_colors.xml`

- `panel_preferences_controls.xml`

- `panel_preferences_crashreports.xml`

- `panel_preferences_firestorm.xml`

- `panel_preferences_general.xml`

- `panel_preferences_graphics1.xml`

- `panel_preferences_move.xml`

- `panel_preferences_opensim.xml`

- `panel_preferences_privacy.xml`

- `panel_preferences_setup.xml`

- `panel_preferences_skins.xml`

- `panel_preferences_sound.xml`

- `panel_preferences_uploads.xml`

- `panel_preferences_voice.xml`

- `panel_presets_camera_pulldown.xml`

- `panel_presets_pulldown.xml`

- `panel_prim_media_controls.xml`

- `panel_primfeed_account.xml`

- `panel_primfeed_photo.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_firstlife.xml`

- `panel_profile_notes.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_profile_web.xml`

- `panel_progress.xml`

- `panel_progress_mini.xml`

- `panel_quickprefs_item.xml`

- `panel_region_access.xml`

- `panel_region_covenant.xml`

- `panel_region_debug.xml`

- `panel_region_environment.xml`

- `panel_region_estate.xml`

- `panel_region_experiences.xml`

- `panel_region_general.xml`

- `panel_region_open_region_settings.xml`

- `panel_region_terrain.xml`

- `panel_region_terrain_texture_transform.xml`

- `panel_rlv_locks.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

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

- `xui_version.xml`


## indra/newview/skins/default/xui/zh/widgets/ (12 files)

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

- `person_view.xml`

- `sun_moon_trackball.xml`


## indra/newview/skins/firestorm/ (1 files)

- `colors.xml`


## indra/newview/skins/firestorm/textures/ (2 files)

- `tabarea.tga`

- `textures.xml`


## indra/newview/skins/firestorm/textures/bottomtray/ (2 files)

- `BottomTray_BG.png`

- `Unread_Msg.png`


## indra/newview/skins/firestorm/textures/navbar/ (2 files)

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`


## indra/newview/skins/firestorm/textures/widgets/ (2 files)

- `Tooltip.png`

- `bevel_background.png`


## indra/newview/skins/firestorm/textures/windows/ (6 files)

- `Inspector_Background.png`

- `TimeBasedMediaBackground.png`

- `Volume_Background.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `hint_background.png`


## indra/newview/skins/firestorm/themes/blue/ (1 files)

- `colors.xml`


## indra/newview/skins/firestorm/themes/blue/textures/bottomtray/ (2 files)

- `BottomTray_BG.png`

- `Unread_Msg.png`


## indra/newview/skins/firestorm/themes/ctrlaltstudio/ (1 files)

- `colors.xml`


## indra/newview/skins/firestorm/themes/ctrlaltstudio/textures/ (2 files)

- `tabarea.tga`

- `textures.xml`


## indra/newview/skins/firestorm/themes/ctrlaltstudio/textures/bottomtray/ (2 files)

- `BottomTray_BG.png`

- `Unread_Msg.png`


## indra/newview/skins/firestorm/themes/ctrlaltstudio/textures/containers/ (6 files)

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Selected.png`


## indra/newview/skins/firestorm/themes/ctrlaltstudio/textures/icons/ (2 files)

- `Info_Over.png`

- `back_arrow_press.png`


## indra/newview/skins/firestorm/themes/ctrlaltstudio/textures/legacy/ (1 files)

- `icon_avatar_online.tga`


## indra/newview/skins/firestorm/themes/ctrlaltstudio/textures/navbar/ (2 files)

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`


## indra/newview/skins/firestorm/themes/ctrlaltstudio/textures/widgets/ (18 files)

- `DropDown_On.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Selected_Press.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`


## indra/newview/skins/firestorm/themes/ctrlaltstudio/textures/windows/ (6 files)

- `Inspector_Background.png`

- `TimeBasedMediaBackground.png`

- `Volume_Background.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `hint_background.png`


## indra/newview/skins/firestorm/themes/dark/ (1 files)

- `colors.xml`


## indra/newview/skins/firestorm/themes/dark/textures/ (1 files)

- `textures.xml`


## indra/newview/skins/firestorm/themes/dark/textures/containers/ (3 files)

- `Toolbar_Left_Flash.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Right_Flash.png`


## indra/newview/skins/firestorm/themes/dark/textures/widgets/ (7 files)

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Highlight.png`

- `TextField_Search_Off.png`


## indra/newview/skins/firestorm/themes/highcontrast/ (1 files)

- `colors.xml`


## indra/newview/skins/firestorm/themes/highcontrast/textures/icons/ (1 files)

- `Icon_DialogStack.png`


## indra/newview/skins/firestorm/themes/highcontrast/textures/widgets/ (7 files)

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `Tooltip.png`


## indra/newview/skins/firestorm/themes/highcontrast/textures/windows/ (5 files)

- `Inspector_Background.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`


## indra/newview/skins/firestorm/xui/de/ (13 files)

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`


## indra/newview/skins/firestorm/xui/en/ (18 files)

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_fs_contacts_friends.xml`

- `panel_group_info_sidetray.xml`

- `panel_instant_message.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`


## indra/newview/skins/firestorm/xui/en/widgets/ (3 files)

- `floater.xml`

- `line_editor.xml`

- `simple_text_editor.xml`


## indra/newview/skins/firestorm/xui/es/ (13 files)

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`


## indra/newview/skins/firestorm/xui/fr/ (13 files)

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`


## indra/newview/skins/firestorm/xui/it/ (13 files)

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`


## indra/newview/skins/firestorm/xui/ja/ (13 files)

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`


## indra/newview/skins/firestorm/xui/pl/ (13 files)

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`


## indra/newview/skins/firestorm/xui/pt/ (13 files)

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`


## indra/newview/skins/firestorm/xui/ru/ (13 files)

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`


## indra/newview/skins/firestorm/xui/zh/ (13 files)

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`


## indra/newview/skins/metaharper/ (2 files)

- `colors.xml`

- `toolbars.xml`


## indra/newview/skins/metaharper/textures/ (149 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `favoriteButton.tga`

- `flyout_btn_left.tga`

- `flyout_btn_left_disabled.tga`

- `flyout_btn_left_selected.tga`

- `flyout_btn_right.tga`

- `flyout_btn_right_disabled.tga`

- `flyout_btn_right_selected.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `glowtouchables.tga`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-call-end.tga`

- `icn_voice-call-start.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-off.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on-lvl3.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_day_cycle.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `rounded_square.j2c`

- `rounded_square.j2k`

- `rounded_square.jp2`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tabarea.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `transparent.j2k`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/metaharper/textures/bottomtray/ (91 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `chatbar_18.png`

- `inventory_18.png`

- `move_18.png`

- `nearbychat_18.png`

- `phoenix_18.png`

- `search_18.png`

- `view_18.png`


## indra/newview/skins/metaharper/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/metaharper/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/metaharper/textures/icons/ (261 files)

- `AddItem_Disabled.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Friends_Icon_24x24.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Alpha_Link.png`

- `Inv_Animation.png`

- `Inv_Animation_Link.png`

- `Inv_BodyShape.png`

- `Inv_BodyShape_Link.png`

- `Inv_CallingCard.png`

- `Inv_CallingCard_Link.png`

- `Inv_Clothing.png`

- `Inv_Clothing_Link.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_Eye_Link.png`

- `Inv_FolderClosed.png`

- `Inv_FolderClosed_Link.png`

- `Inv_FolderOpen.png`

- `Inv_FolderOpen_Link.png`

- `Inv_Gesture.png`

- `Inv_Gesture_Link.png`

- `Inv_Gloves.png`

- `Inv_Gloves_Link.png`

- `Inv_Hair.png`

- `Inv_Hair_Link.png`

- `Inv_Invalid.png`

- `Inv_Jacket.png`

- `Inv_Jacket_Link.png`

- `Inv_Landmark.png`

- `Inv_Landmark_Link.png`

- `Inv_Link.png`

- `Inv_LinkFolder.png`

- `Inv_LinkFolder_Link.png`

- `Inv_LinkItem.png`

- `Inv_LinkItem_Broken.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderClosed_Link.png`

- `Inv_LookFolderOpen.png`

- `Inv_LookFolderOpen_Link.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Notecard.png`

- `Inv_Notecard_Link.png`

- `Inv_Object.png`

- `Inv_Object_Link.png`

- `Inv_Object_Multi.png`

- `Inv_Object_Multi_Link.png`

- `Inv_Pants.png`

- `Inv_Pants_Link.png`

- `Inv_Script.png`

- `Inv_Script_Link.png`

- `Inv_Shirt.png`

- `Inv_Shirt_Link.png`

- `Inv_Shoe.png`

- `Inv_Shoe_Link.png`

- `Inv_Skin.png`

- `Inv_Skin_Link.png`

- `Inv_Skirt.png`

- `Inv_Skirt_Link.png`

- `Inv_Snapshot.png`

- `Inv_Snapshot_Link.png`

- `Inv_Socks.png`

- `Inv_Socks_Link.png`

- `Inv_Sound.png`

- `Inv_Sound_Link.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Tattoo_Link.png`

- `Inv_Texture.png`

- `Inv_Texture_Link.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Underpants_Link.png`

- `Inv_Undershirt.png`

- `Inv_Undershirt_Link.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `Parcel_BuildNo_Dark.png`

- `Parcel_BuildNo_Light.png`

- `Parcel_Build_Dark.png`

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Pathfinding_Dirty.png`

- `Pathfinding_Dirty_Light.png`

- `Pathfinding_Disabled.png`

- `Pathfinding_Disabled_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `PowerOff_Off.png`

- `PowerOff_Over.png`

- `PowerOff_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `TrashItem_Disabled.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `call_end_icon_24x24.png`

- `call_icon_24x24.png`

- `edit_mine.png`

- `edit_theirs.png`

- `genie_icon_24x24.png`

- `gift_icon_24x24.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `profile_icon_24x24.png`

- `sale_icon_24x24.png`

- `see_me_online.png`

- `see_on_map.png`

- `unknown_icon.png`


## indra/newview/skins/metaharper/textures/legacy/ (1 files)

- `icon_avatar_online.tga`


## indra/newview/skins/metaharper/textures/navbar/ (35 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`


## indra/newview/skins/metaharper/textures/quick_tips/ (13 files)

- `avatar_free_mode.png`

- `camera_free_mode.png`

- `camera_orbit_mode.png`

- `camera_pan_mode.png`

- `camera_preset_front_view.png`

- `camera_preset_group_view.png`

- `camera_preset_rear_view.png`

- `move_fly_first.png`

- `move_fly_second.png`

- `move_run_first.png`

- `move_run_second.png`

- `move_walk_first.png`

- `move_walk_second.png`


## indra/newview/skins/metaharper/textures/taskpanel/ (42 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`

- `translate_icon_24x24.png`


## indra/newview/skins/metaharper/textures/toolbar_icons/ (5 files)

- `build.png`

- `chat.png`

- `gestures.png`

- `map.png`

- `mini_map.png`


## indra/newview/skins/metaharper/textures/widgets/ (2 files)

- `Tooltip.png`

- `bevel_background.png`


## indra/newview/skins/metaharper/textures/windows/ (46 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/metaharper/textures/world/ (9 files)

- `BeaconArrow.png`

- `NoEntryLines.png`

- `NoEntryPassLines.png`

- `Overhead_Arrow_L.png`

- `Overhead_Arrow_M.png`

- `Overhead_Arrow_S.png`

- `Overhead_L.png`

- `Overhead_M.png`

- `Overhead_S.png`


## indra/newview/skins/metaharper/themes/appalachian_sky/ (1 files)

- `colors.xml`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/ (148 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `favoriteButton.tga`

- `flyout_btn_left.tga`

- `flyout_btn_left_disabled.tga`

- `flyout_btn_left_selected.tga`

- `flyout_btn_right.tga`

- `flyout_btn_right_disabled.tga`

- `flyout_btn_right_selected.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `glowtouchables.tga`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-call-end.tga`

- `icn_voice-call-start.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-off.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on-lvl3.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_day_cycle.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `rounded_square.j2c`

- `rounded_square.j2k`

- `rounded_square.jp2`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tabarea.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `textures.xml`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `transparent.j2k`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/bottomtray/ (91 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `hammer_18.png`

- `inventory_18.png`

- `map_18.png`

- `minimap_18.png`

- `move_18.png`

- `search_18.png`

- `view_18.png`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/icons/ (257 files)

- `AddItem_Disabled.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Friends_Icon_24x24.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Alpha_Link.png`

- `Inv_Animation.png`

- `Inv_Animation_Link.png`

- `Inv_BodyShape.png`

- `Inv_BodyShape_Link.png`

- `Inv_CallingCard.png`

- `Inv_CallingCard_Link.png`

- `Inv_Clothing.png`

- `Inv_Clothing_Link.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_Eye_Link.png`

- `Inv_FolderClosed.png`

- `Inv_FolderClosed_Link.png`

- `Inv_FolderOpen.png`

- `Inv_FolderOpen_Link.png`

- `Inv_Gesture.png`

- `Inv_Gesture_Link.png`

- `Inv_Gloves.png`

- `Inv_Gloves_Link.png`

- `Inv_Hair.png`

- `Inv_Hair_Link.png`

- `Inv_Invalid.png`

- `Inv_Jacket.png`

- `Inv_Jacket_Link.png`

- `Inv_Landmark.png`

- `Inv_Landmark_Link.png`

- `Inv_Link.png`

- `Inv_LinkFolder.png`

- `Inv_LinkFolder_Link.png`

- `Inv_LinkItem.png`

- `Inv_LinkItem_Broken.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderClosed_Link.png`

- `Inv_LookFolderOpen.png`

- `Inv_LookFolderOpen_Link.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Notecard.png`

- `Inv_Notecard_Link.png`

- `Inv_Object.png`

- `Inv_Object_Link.png`

- `Inv_Object_Multi.png`

- `Inv_Object_Multi_Link.png`

- `Inv_Pants.png`

- `Inv_Pants_Link.png`

- `Inv_Script.png`

- `Inv_Script_Link.png`

- `Inv_Shirt.png`

- `Inv_Shirt_Link.png`

- `Inv_Shoe.png`

- `Inv_Shoe_Link.png`

- `Inv_Skin.png`

- `Inv_Skin_Link.png`

- `Inv_Skirt.png`

- `Inv_Skirt_Link.png`

- `Inv_Snapshot.png`

- `Inv_Snapshot_Link.png`

- `Inv_Socks.png`

- `Inv_Socks_Link.png`

- `Inv_Sound.png`

- `Inv_Sound_Link.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Tattoo_Link.png`

- `Inv_Texture.png`

- `Inv_Texture_Link.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Underpants_Link.png`

- `Inv_Undershirt.png`

- `Inv_Undershirt_Link.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `Parcel_BuildNo_Dark.png`

- `Parcel_BuildNo_Light.png`

- `Parcel_Build_Dark.png`

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `PowerOff_Off.png`

- `PowerOff_Over.png`

- `PowerOff_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `TrashItem_Disabled.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `call_end_icon_24x24.png`

- `call_icon_24x24.png`

- `edit_mine.png`

- `edit_theirs.png`

- `genie_icon_24x24.png`

- `gift_icon_24x24.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `profile_icon_24x24.png`

- `sale_icon_24x24.png`

- `see_me_online.png`

- `see_on_map.png`

- `unknown_icon.png`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/navbar/ (35 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/quick_tips/ (13 files)

- `avatar_free_mode.png`

- `camera_free_mode.png`

- `camera_orbit_mode.png`

- `camera_pan_mode.png`

- `camera_preset_front_view.png`

- `camera_preset_group_view.png`

- `camera_preset_rear_view.png`

- `move_fly_first.png`

- `move_fly_second.png`

- `move_run_first.png`

- `move_run_second.png`

- `move_walk_first.png`

- `move_walk_second.png`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/taskpanel/ (42 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`

- `translate_icon_24x24.png`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/widgets/ (155 files)

- `Arrow_Down.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.pdn`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/windows/ (46 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/metaharper/themes/appalachian_sky/textures/world/ (9 files)

- `BeaconArrow.png`

- `NoEntryLines.png`

- `NoEntryPassLines.png`

- `Overhead_Arrow_L.png`

- `Overhead_Arrow_M.png`

- `Overhead_Arrow_S.png`

- `Overhead_L.png`

- `Overhead_M.png`

- `Overhead_S.png`


## indra/newview/skins/metaharper/themes/black_glass/ (1 files)

- `colors.xml`


## indra/newview/skins/metaharper/themes/black_glass/textures/ (8 files)

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `menu_bar.tga`

- `startup_logo.j2c`

- `tabarea.tga`

- `toggle_button_off.png`

- `toggle_button_selected.png`


## indra/newview/skins/metaharper/themes/black_glass/textures/bottomtray/ (3 files)

- `ChatBarHandle.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`


## indra/newview/skins/metaharper/themes/black_glass/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/metaharper/themes/black_glass/textures/icons/ (6 files)

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Edit_Wrench.png`

- `check_mark.png`


## indra/newview/skins/metaharper/themes/black_glass/textures/navbar/ (21 files)

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `History_Arrow.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`


## indra/newview/skins/metaharper/themes/black_glass/textures/widgets/ (150 files)

- `Arrow_Down.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`


## indra/newview/skins/metaharper/themes/black_glass/textures/windows/ (46 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/metaharper/themes/cool_ocean/ (1 files)

- `colors.xml`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/ (151 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `favoriteButton.tga`

- `flyout_btn_left.tga`

- `flyout_btn_left_disabled.tga`

- `flyout_btn_left_selected.tga`

- `flyout_btn_right.tga`

- `flyout_btn_right_disabled.tga`

- `flyout_btn_right_selected.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `glowtouchables.tga`

- `green_dot.tga`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-call-end.tga`

- `icn_voice-call-start.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-off.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on-lvl3.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_day_cycle.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `rounded_square.j2c`

- `rounded_square.j2k`

- `rounded_square.jp2`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tabarea.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `textures.xml`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `transparent.j2k`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/bottomtray/ (94 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `gesture_18.png`

- `hammer_18.png`

- `inventory_18.png`

- `map_18.png`

- `minimap_18.png`

- `move_18.png`

- `nearbychat_18.png`

- `phoenix_18.png`

- `search_18.png`

- `view_18.png`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/icons/ (257 files)

- `AddItem_Disabled.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Friends_Icon_24x24.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Alpha_Link.png`

- `Inv_Animation.png`

- `Inv_Animation_Link.png`

- `Inv_BodyShape.png`

- `Inv_BodyShape_Link.png`

- `Inv_CallingCard.png`

- `Inv_CallingCard_Link.png`

- `Inv_Clothing.png`

- `Inv_Clothing_Link.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_Eye_Link.png`

- `Inv_FolderClosed.png`

- `Inv_FolderClosed_Link.png`

- `Inv_FolderOpen.png`

- `Inv_FolderOpen_Link.png`

- `Inv_Gesture.png`

- `Inv_Gesture_Link.png`

- `Inv_Gloves.png`

- `Inv_Gloves_Link.png`

- `Inv_Hair.png`

- `Inv_Hair_Link.png`

- `Inv_Invalid.png`

- `Inv_Jacket.png`

- `Inv_Jacket_Link.png`

- `Inv_Landmark.png`

- `Inv_Landmark_Link.png`

- `Inv_Link.png`

- `Inv_LinkFolder.png`

- `Inv_LinkFolder_Link.png`

- `Inv_LinkItem.png`

- `Inv_LinkItem_Broken.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderClosed_Link.png`

- `Inv_LookFolderOpen.png`

- `Inv_LookFolderOpen_Link.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Notecard.png`

- `Inv_Notecard_Link.png`

- `Inv_Object.png`

- `Inv_Object_Link.png`

- `Inv_Object_Multi.png`

- `Inv_Object_Multi_Link.png`

- `Inv_Pants.png`

- `Inv_Pants_Link.png`

- `Inv_Script.png`

- `Inv_Script_Link.png`

- `Inv_Shirt.png`

- `Inv_Shirt_Link.png`

- `Inv_Shoe.png`

- `Inv_Shoe_Link.png`

- `Inv_Skin.png`

- `Inv_Skin_Link.png`

- `Inv_Skirt.png`

- `Inv_Skirt_Link.png`

- `Inv_Snapshot.png`

- `Inv_Snapshot_Link.png`

- `Inv_Socks.png`

- `Inv_Socks_Link.png`

- `Inv_Sound.png`

- `Inv_Sound_Link.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Tattoo_Link.png`

- `Inv_Texture.png`

- `Inv_Texture_Link.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Underpants_Link.png`

- `Inv_Undershirt.png`

- `Inv_Undershirt_Link.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `Parcel_BuildNo_Dark.png`

- `Parcel_BuildNo_Light.png`

- `Parcel_Build_Dark.png`

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `PowerOff_Off.png`

- `PowerOff_Over.png`

- `PowerOff_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `TrashItem_Disabled.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `call_end_icon_24x24.png`

- `call_icon_24x24.png`

- `edit_mine.png`

- `edit_theirs.png`

- `genie_icon_24x24.png`

- `gift_icon_24x24.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `profile_icon_24x24.png`

- `sale_icon_24x24.png`

- `see_me_online.png`

- `see_on_map.png`

- `unknown_icon.png`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/navbar/ (35 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/quick_tips/ (13 files)

- `avatar_free_mode.png`

- `camera_free_mode.png`

- `camera_orbit_mode.png`

- `camera_pan_mode.png`

- `camera_preset_front_view.png`

- `camera_preset_group_view.png`

- `camera_preset_rear_view.png`

- `move_fly_first.png`

- `move_fly_second.png`

- `move_run_first.png`

- `move_run_second.png`

- `move_walk_first.png`

- `move_walk_second.png`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/taskpanel/ (42 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`

- `translate_icon_24x24.png`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/widgets/ (156 files)

- `Arrow_Down.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.pdn`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/windows/ (46 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/metaharper/themes/cool_ocean/textures/world/ (9 files)

- `BeaconArrow.png`

- `NoEntryLines.png`

- `NoEntryPassLines.png`

- `Overhead_Arrow_L.png`

- `Overhead_Arrow_M.png`

- `Overhead_Arrow_S.png`

- `Overhead_L.png`

- `Overhead_M.png`

- `Overhead_S.png`


## indra/newview/skins/metaharper/xui/en/ (7 files)

- `main_view.xml`

- `panel_group_info_sidetray.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_media.xml`

- `panel_outfits_wearing.xml`

- `panel_toolbar_view.xml`

- `panel_volume_pulldown.xml`


## indra/newview/skins/metaharper/xui/en/widgets/ (3 files)

- `progress_bar.xml`

- `toolbar.xml`

- `toolbar_vertical.xml`


## indra/newview/skins/starlight/ (1 files)

- `colors.xml`


## indra/newview/skins/starlight/textures/ (41 files)

- `BottomTray_BG.png`

- `arrow_keys.png`

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `down_arrow.png`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-pvtfocus.tga`

- `icon_avatar_online_h.tga`

- `icon_day_cycle.tga`

- `icon_event_adult.tga`

- `icon_lock.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `map_avatar_16.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_8.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `mute_icon.tga`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `show_btn.tga`

- `show_btn_selected.tga`

- `smicon_warn.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `textures.xml`

- `up_arrow.png`


## indra/newview/skins/starlight/textures/bottomtray/ (31 files)

- `Cam_FreeCam_Off_Pref.png`

- `Cam_Pan_Over.png`

- `CameraView_Press.png`

- `ChatBarHandle.png`

- `Move_Fly_Off.png`

- `Move_Walk_Off_Pref.png`

- `Movement_Left_On.png`

- `Movement_Right_On.png`

- `Notices_Unread.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `TabIcon_Things_Bottomtray.png`

- `Unread_Chiclet.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `inventory_18.png`

- `starlight_build.png`

- `starlight_camera.png`

- `starlight_gesture.png`

- `starlight_map.png`

- `starlight_minimap.png`

- `starlight_move.png`

- `starlight_search.png`

- `starlight_snapshot.png`


## indra/newview/skins/starlight/textures/containers/ (17 files)

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Selected.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Selected.png`


## indra/newview/skins/starlight/textures/icons/ (50 files)

- `AddItem_Over.png`

- `BackArrow_Over.png`

- `DragHandle.png`

- `Draw_Distance.png`

- `Edit_Prefs_Wrench.png`

- `Edit_Wrench.png`

- `Generic_Object.png`

- `Generic_Person.png`

- `Hierarchy_View_On.png`

- `Inv_Gift.png`

- `Inv_Link.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Mesh.png`

- `Inv_Physics.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Universal.png`

- `Inv_WaterLight.png`

- `Inv_WindLight.png`

- `OptionsMenu_Over.png`

- `OutboxPush_On_Selected.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

- `SL_Logo.png`

- `Shop.png`

- `Toolbar_Gesture_btn.png`

- `TrashItem_Over.png`

- `Web_Profile_Off.png`

- `check_mark.png`

- `icn_toolbar_inventory.tga`

- `icn_toolbar_sidebar.png`

- `icn_toolbar_speak.png`

- `icon_avatar_online.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`


## indra/newview/skins/starlight/textures/model_wizard/ (3 files)

- `divider_line.png`

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/starlight/textures/navbar/ (9 files)

- `Arrow_Left_Over.png`

- `Arrow_Right_Over.png`

- `Favorite_Link_Over.png`

- `FileMenu_BarSelect.png`

- `Help_Over.png`

- `Home_Over.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/starlight/textures/taskpanel/ (12 files)

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Selected.png`


## indra/newview/skins/starlight/textures/toolbar_icons/ (15 files)

- `Environment.png`

- `build.png`

- `gestures.png`

- `google.png`

- `gridstatus.png`

- `highlighting.png`

- `highlighting_selected.png`

- `land.png`

- `mini_cart.png`

- `outbox.png`

- `phototools_fs.png`

- `region.png`

- `statistics.png`

- `teleporthome.png`

- `translate.png`


## indra/newview/skins/starlight/textures/widgets/ (67 files)

- `Arrow_Down.png`

- `Badge_Background_New.png`

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

- `Checkbox_On_Over.png`

- `Checkbox_Over.png`

- `ComboButton_On.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Opened_Over.png`

- `DropDown_On.png`

- `ListItem_Select.png`

- `ProgressBar.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_On_Over.png`

- `RadioButton_Over.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Up_Over.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert_Over.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SpeakBtn_Left_Selected_Press.png`

- `Stepper_Down_Over.png`

- `Stepper_Up_Over.png`

- `Tooltip.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`


## indra/newview/skins/starlight/textures/windows/ (17 files)

- `Flyout.png`

- `Flyout_Pointer_Up.png`

- `Icon_Close_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Press.png`

- `Inspector_Hover.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `yellow_gradient.png`


## indra/newview/skins/starlight/themes/mono_teal/ (1 files)

- `colors.xml`


## indra/newview/skins/starlight/themes/mono_teal/textures/ (143 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_keys.png`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `green_checkmark.png`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_avatar_online_h.tga`

- `icon_day_cycle.tga`

- `icon_day_cycle_12am.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `payment_info_used.tga`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `red_x.png`

- `rounded_square.j2c`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/starlight/themes/mono_teal/textures/bottomtray/ (104 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Off_pref.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Off_Pref.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `TabIcon_Things_Bottomtray.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `camera_load.png`

- `camera_store.png`

- `chatbar_18.png`

- `inventory_18.png`

- `starlight_build.png`

- `starlight_camera.png`

- `starlight_map.png`

- `starlight_minimap.png`

- `starlight_move.png`

- `starlight_search.png`

- `starlight_snapshot.png`


## indra/newview/skins/starlight/themes/mono_teal/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/starlight/themes/mono_teal/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/starlight/themes/mono_teal/textures/icons/ (311 files)

- `AddItem_Disabled.png`

- `AddItem_Menu.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Chat_History.png`

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

- `Conv_toolbar_plus.png`

- `Conv_toolbar_sort.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Draw_Distance.png`

- `Edit_Flip_X.png`

- `Edit_Prefs_Wrench.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Friends_Icon_24x24.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_DialogStack.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_FolderClosed.png`

- `Inv_FolderOpen.png`

- `Inv_Gesture.png`

- `Inv_Gift.png`

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

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_WaterLight.png`

- `Inv_WindLight.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `Music_Off.png`

- `Music_Over.png`

- `Music_Press.png`

- `Muted_Chat.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_On_Selected.png`

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

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Parcel_WindLight.png`

- `Pathfinding_Dirty_Light.png`

- `Pathfinding_Disabled_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `Sync_Disabled.png`

- `Sync_Enabled.png`

- `Sync_Progress_1.png`

- `Sync_Progress_2.png`

- `Sync_Progress_3.png`

- `Sync_Progress_4.png`

- `Sync_Progress_5.png`

- `Sync_Progress_6.png`

- `Toolbar_Gesture_btn.png`

- `TrashItem_Disabled.png`

- `TrashItem_Menu.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `call_end_icon_24x24.png`

- `call_icon_24x24.png`

- `check_mark.png`

- `collapse_to_one_line.png`

- `edit_mine.png`

- `edit_mine_h.png`

- `edit_theirs.png`

- `edit_theirs_h.png`

- `expand_one_liner.png`

- `genie_icon_24x24.png`

- `gift_icon_24x24.png`

- `icn_toolbar_inventory.tga`

- `icn_toolbar_sidebar.png`

- `icn_toolbar_speak.png`

- `icon_avatar_online.png`

- `nearby_chat_icon.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `profile_icon_24x24.png`

- `request_tp_icon_24x24.png`

- `sale_icon_24x24.png`

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

- `see_me_online.png`

- `see_me_online_h.png`

- `see_on_map.png`

- `see_on_map_h.png`

- `teleport_menu.png`

- `unknown_icon.png`


## indra/newview/skins/starlight/themes/mono_teal/textures/model_wizard/ (3 files)

- `divider_line.png`

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/starlight/themes/mono_teal/textures/navbar/ (36 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/starlight/themes/mono_teal/textures/taskpanel/ (42 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`

- `translate_icon_24x24.png`


## indra/newview/skins/starlight/themes/mono_teal/textures/toolbar_icons/ (59 files)

- `Environment.png`

- `animation_override.png`

- `appearance.png`

- `areasearch.png`

- `asset_blacklist.png`

- `avatars.png`

- `blocklist.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `chat.png`

- `contact_sets.png`

- `destinations.png`

- `facebook.png`

- `gestures.png`

- `google.png`

- `gridstatus.png`

- `groundsit.png`

- `group_titles.png`

- `highlighting.png`

- `highlighting_selected.png`

- `howto.png`

- `inventory.png`

- `land.png`

- `landmark_here.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `mouselook.png`

- `move.png`

- `movelock.png`

- `nearbychat.png`

- `nearbyvoice.png`

- `outbox.png`

- `people.png`

- `phoenix.png`

- `phototools_cam.png`

- `phototools_fs.png`

- `picks.png`

- `places.png`

- `posestand.png`

- `preferences.png`

- `profile.png`

- `radar.png`

- `region.png`

- `resync_animations.png`

- `search.png`

- `settings_debug.png`

- `snapshot.png`

- `snapshot_to_disk.png`

- `sound_explorer.png`

- `speak.png`

- `statistics.png`

- `teleporthistory.png`

- `teleporthome.png`

- `translate.png`

- `view.png`


## indra/newview/skins/starlight/themes/mono_teal/textures/widgets/ (177 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

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

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Hover.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `button_disabled_32x128.png`

- `button_enabled_32x128.png`

- `button_enabled_selected_32x128.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `horizontal_drag_handle.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`

- `vertical_drag_handle.png`


## indra/newview/skins/starlight/themes/mono_teal/textures/windows/ (52 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Collapse_Foreground.png`

- `Icon_Collapse_Press.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Snooze_Foreground.png`

- `Icon_Snooze_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/starlight/themes/nostalgia_blue/ (1 files)

- `colors.xml`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/ (153 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_keys.png`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `flyout_btn_left.tga`

- `flyout_btn_left_disabled.tga`

- `flyout_btn_left_selected.tga`

- `flyout_btn_right.tga`

- `flyout_btn_right_disabled.tga`

- `flyout_btn_right_selected.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `glowtouchables.tga`

- `green_checkmark.png`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-call-end.tga`

- `icn_voice-call-start.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-off.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on-lvl3.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_avatar_online_h.tga`

- `icon_day_cycle.tga`

- `icon_day_cycle_12am.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `red_x.png`

- `rounded_square.j2c`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/bottomtray/ (102 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Off_Pref.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Off_Pref.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `TabIcon_Things_Bottomtray.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `chatbar_18.png`

- `inventory_18.png`

- `movement_backward_off.png`

- `movement_backward_on.png`

- `movement_down_off.png`

- `movement_down_on.png`

- `movement_forward_off.png`

- `movement_forward_on.png`

- `movement_left_off.png`

- `movement_left_on.png`

- `movement_right_off.png`

- `movement_right_on.png`

- `movement_turnleft_off.png`

- `movement_turnleft_on.png`

- `movement_turnright_off.png`

- `movement_turnright_on.png`

- `movement_up_off.png`

- `movement_up_on.png`

- `starlight_build.png`

- `starlight_camera.png`

- `starlight_map.png`

- `starlight_minimap.png`

- `starlight_move.png`

- `starlight_search.png`

- `starlight_snapshot.png`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/containers/ (43 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_IM_Unselected.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_IM_Unselected.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_IM_Unselected.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Over.png`

- `tabtop_Left_Press.png`

- `tabtop_left_off.png`

- `tabtop_left_selected.png`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/icons/ (271 files)

- `AddItem_Disabled.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Draw_Distance.png`

- `Edit_Prefs_Wrench.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_DialogStack.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_FolderClosed.png`

- `Inv_FolderOpen.png`

- `Inv_Gesture.png`

- `Inv_Gift.png`

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

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_WaterLight.png`

- `Inv_WindLight.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `Music_Off.png`

- `Music_Over.png`

- `Music_Press.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_On_Selected.png`

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

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

- `PowerOff_Off.png`

- `PowerOff_Over.png`

- `PowerOff_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `Sync_Disabled.png`

- `Sync_Enabled.png`

- `Sync_Progress_1.png`

- `Sync_Progress_2.png`

- `Sync_Progress_3.png`

- `Sync_Progress_4.png`

- `Sync_Progress_5.png`

- `Sync_Progress_6.png`

- `Toolbar_Gesture_btn.png`

- `TrashItem_Disabled.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `check_mark.png`

- `edit_mine.png`

- `edit_mine_h.png`

- `edit_theirs.png`

- `edit_theirs_h.png`

- `icn_toolbar_inventory.tga`

- `icn_toolbar_sidebar.png`

- `icn_toolbar_speak.png`

- `icon_avatar_online.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `see_me_online.png`

- `see_me_online_h.png`

- `see_on_map.png`

- `see_on_map_h.png`

- `unknown_icon.png`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/model_wizard/ (3 files)

- `divider_line.png`

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/navbar/ (36 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/taskpanel/ (41 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/toolbar_icons/ (44 files)

- `Environment.png`

- `animation_override.png`

- `appearance.png`

- `areasearch.png`

- `avatars.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `chat.png`

- `destinations.png`

- `gestures.png`

- `google.png`

- `gridstatus.png`

- `highlighting.png`

- `highlighting_selected.png`

- `howto.png`

- `inventory.png`

- `land.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `move.png`

- `nearbychat.png`

- `nearbyvoice.png`

- `outbox.png`

- `people.png`

- `phoenix.png`

- `phototools_cam.png`

- `phototools_fs.png`

- `picks.png`

- `places.png`

- `preferences.png`

- `profile.png`

- `region.png`

- `search.png`

- `settings_debug.png`

- `snapshot.png`

- `speak.png`

- `statistics.png`

- `teleporthome.png`

- `translate.png`

- `view.png`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/widgets/ (178 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Badge_Background.png`

- `Badge_Background_New.png`

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

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Hover.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`


## indra/newview/skins/starlight/themes/nostalgia_blue/textures/windows/ (50 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Collapse_Foreground.png`

- `Icon_Collapse_Press.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/starlight/themes/original_orange/ (1 files)

- `colors.xml`


## indra/newview/skins/starlight/themes/original_orange/textures/ (153 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_keys.png`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `flyout_btn_left.tga`

- `flyout_btn_left_disabled.tga`

- `flyout_btn_left_selected.tga`

- `flyout_btn_right.tga`

- `flyout_btn_right_disabled.tga`

- `flyout_btn_right_selected.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `glowtouchables.tga`

- `green_checkmark.png`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-call-end.tga`

- `icn_voice-call-start.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-off.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on-lvl3.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_avatar_online_h.tga`

- `icon_day_cycle.tga`

- `icon_day_cycle_12am.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `red_x.png`

- `rounded_square.j2c`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/starlight/themes/original_orange/textures/bottomtray/ (103 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Off_Pref.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Off_Pref.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `TabIcon_Things_Bottomtray.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `chatbar_18.png`

- `inventory_18.png`

- `starlight_build.png`

- `starlight_camera.png`

- `starlight_gesture.png`

- `starlight_map.png`

- `starlight_minimap.png`

- `starlight_move.png`

- `starlight_search.png`

- `starlight_snapshot.png`


## indra/newview/skins/starlight/themes/original_orange/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/starlight/themes/original_orange/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/starlight/themes/original_orange/textures/icons/ (270 files)

- `AddItem_Disabled.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Draw_Distance.png`

- `Edit_Prefs_Wrench.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_FolderClosed.png`

- `Inv_FolderOpen.png`

- `Inv_Gesture.png`

- `Inv_Gift.png`

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

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_WaterLight.png`

- `Inv_WindLight.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `Music_Off.png`

- `Music_Over.png`

- `Music_Press.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_On_Selected.png`

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

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

- `PowerOff_Off.png`

- `PowerOff_Over.png`

- `PowerOff_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `Sync_Disabled.png`

- `Sync_Enabled.png`

- `Sync_Progress_1.png`

- `Sync_Progress_2.png`

- `Sync_Progress_3.png`

- `Sync_Progress_4.png`

- `Sync_Progress_5.png`

- `Sync_Progress_6.png`

- `Toolbar_Gesture_btn.png`

- `TrashItem_Disabled.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `check_mark.png`

- `edit_mine.png`

- `edit_mine_h.png`

- `edit_theirs.png`

- `edit_theirs_h.png`

- `icn_toolbar_inventory.tga`

- `icn_toolbar_sidebar.png`

- `icn_toolbar_speak.png`

- `icon_avatar_online.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `see_me_online.png`

- `see_me_online_h.png`

- `see_on_map.png`

- `see_on_map_h.png`

- `unknown_icon.png`


## indra/newview/skins/starlight/themes/original_orange/textures/model_wizard/ (3 files)

- `divider_line.png`

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/starlight/themes/original_orange/textures/navbar/ (36 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/starlight/themes/original_orange/textures/taskpanel/ (41 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`


## indra/newview/skins/starlight/themes/original_orange/textures/toolbar_icons/ (44 files)

- `Environment.png`

- `animation_override.png`

- `appearance.png`

- `areasearch.png`

- `avatars.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `chat.png`

- `destinations.png`

- `gestures.png`

- `google.png`

- `gridstatus.png`

- `highlighting.png`

- `highlighting_selected.png`

- `howto.png`

- `inventory.png`

- `land.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `move.png`

- `nearbychat.png`

- `nearbyvoice.png`

- `outbox.png`

- `people.png`

- `phoenix.png`

- `phototools_cam.png`

- `phototools_fs.png`

- `picks.png`

- `places.png`

- `preferences.png`

- `profile.png`

- `region.png`

- `search.png`

- `settings_debug.png`

- `snapshot.png`

- `speak.png`

- `statistics.png`

- `teleporthome.png`

- `translate.png`

- `view.png`


## indra/newview/skins/starlight/themes/original_orange/textures/widgets/ (177 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Badge_Background.png`

- `Badge_Background_New.png`

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

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`


## indra/newview/skins/starlight/themes/original_orange/textures/windows/ (48 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/starlight/themes/original_teal/ (1 files)

- `colors.xml`


## indra/newview/skins/starlight/themes/original_teal/textures/ (154 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_keys.png`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `flyout_btn_left.tga`

- `flyout_btn_left_disabled.tga`

- `flyout_btn_left_selected.tga`

- `flyout_btn_right.tga`

- `flyout_btn_right_disabled.tga`

- `flyout_btn_right_selected.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `glowtouchables.tga`

- `green_checkmark.png`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-call-end.tga`

- `icn_voice-call-start.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-off.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on-lvl3.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_avatar_online_h.tga`

- `icon_day_cycle.tga`

- `icon_day_cycle_12am.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_32.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `red_x.png`

- `rounded_square.j2c`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/starlight/themes/original_teal/textures/bottomtray/ (102 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Off_Pref.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Off_Pref.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `TabIcon_Things_Bottomtray.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `chatbar_18.png`

- `inventory_18.png`

- `starlight_build.png`

- `starlight_camera.png`

- `starlight_map.png`

- `starlight_minimap.png`

- `starlight_move.png`

- `starlight_search.png`

- `starlight_snapshot.png`


## indra/newview/skins/starlight/themes/original_teal/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/starlight/themes/original_teal/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/starlight/themes/original_teal/textures/icons/ (271 files)

- `AddItem_Disabled.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Draw_Distance.png`

- `Edit_Prefs_Wrench.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_FolderClosed.png`

- `Inv_FolderOpen.png`

- `Inv_Gesture.png`

- `Inv_Gift.png`

- `Inv_Gloves.png`

- `Inv_Hair.png`

- `Inv_Invalid.png`

- `Inv_Jacket.png`

- `Inv_Landmark.png`

- `Inv_Link.png`

- `Inv_LinkFolder.png`

- `Inv_LinkItem.png`

- `Inv_LinkItem_Broken.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderOpen.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_WaterLight.png`

- `Inv_WindLight.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `Music_Off.png`

- `Music_Over.png`

- `Music_Press.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_On_Selected.png`

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

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

- `PowerOff_Off.png`

- `PowerOff_Over.png`

- `PowerOff_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `Sync_Disabled.png`

- `Sync_Enabled.png`

- `Sync_Progress_1.png`

- `Sync_Progress_2.png`

- `Sync_Progress_3.png`

- `Sync_Progress_4.png`

- `Sync_Progress_5.png`

- `Sync_Progress_6.png`

- `Toolbar_Gesture_btn.png`

- `TrashItem_Disabled.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `check_mark.png`

- `edit_mine.png`

- `edit_mine_h.png`

- `edit_theirs.png`

- `edit_theirs_h.png`

- `icn_toolbar_inventory.tga`

- `icn_toolbar_sidebar.png`

- `icn_toolbar_speak.png`

- `icon_avatar_online.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `see_me_online.png`

- `see_me_online_h.png`

- `see_on_map.png`

- `see_on_map_h.png`

- `unknown_icon.png`


## indra/newview/skins/starlight/themes/original_teal/textures/model_wizard/ (3 files)

- `divider_line.png`

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/starlight/themes/original_teal/textures/navbar/ (36 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/starlight/themes/original_teal/textures/taskpanel/ (41 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`


## indra/newview/skins/starlight/themes/original_teal/textures/toolbar_icons/ (42 files)

- `Environment.png`

- `animation_override.png`

- `appearance.png`

- `areasearch.png`

- `avatars.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `chat.png`

- `destinations.png`

- `gestures.png`

- `google.png`

- `gridstatus.png`

- `howto.png`

- `inventory.png`

- `land.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `move.png`

- `nearbychat.png`

- `nearbyvoice.png`

- `outbox.png`

- `people.png`

- `phoenix.png`

- `phototools_cam.png`

- `phototools_fs.png`

- `picks.png`

- `places.png`

- `preferences.png`

- `profile.png`

- `region.png`

- `search.png`

- `settings_debug.png`

- `snapshot.png`

- `speak.png`

- `statistics.png`

- `teleporthome.png`

- `translate.png`

- `view.png`


## indra/newview/skins/starlight/themes/original_teal/textures/widgets/ (177 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Badge_Background.png`

- `Badge_Background_New.png`

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

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`


## indra/newview/skins/starlight/themes/original_teal/textures/windows/ (48 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/starlight/themes/silver_blue/ (1 files)

- `colors.xml`


## indra/newview/skins/starlight/themes/silver_blue/textures/ (143 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_keys.png`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `green_checkmark.png`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_avatar_online_h.tga`

- `icon_day_cycle.tga`

- `icon_day_cycle_12am.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `payment_info_used.tga`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `red_x.png`

- `rounded_square.j2c`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/starlight/themes/silver_blue/textures/bottomtray/ (104 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Off_pref.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Off_Pref.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `TabIcon_Things_Bottomtray.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `camera_load.png`

- `camera_store.png`

- `chatbar_18.png`

- `inventory_18.png`

- `starlight_build.png`

- `starlight_camera.png`

- `starlight_map.png`

- `starlight_minimap.png`

- `starlight_move.png`

- `starlight_search.png`

- `starlight_snapshot.png`


## indra/newview/skins/starlight/themes/silver_blue/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/starlight/themes/silver_blue/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/starlight/themes/silver_blue/textures/icons/ (308 files)

- `AddItem_Disabled.png`

- `AddItem_Menu.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Chat_History.png`

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

- `Conv_toolbar_plus.png`

- `Conv_toolbar_sort.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Draw_Distance.png`

- `Edit_Flip_X.png`

- `Edit_Prefs_Wrench.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Friends_Icon_24x24.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_DialogStack.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_FolderClosed.png`

- `Inv_FolderOpen.png`

- `Inv_Gesture.png`

- `Inv_Gift.png`

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

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_WaterLight.png`

- `Inv_WindLight.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `Music_Off.png`

- `Music_Over.png`

- `Music_Press.png`

- `Muted_Chat.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_On_Selected.png`

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

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Parcel_WindLight.png`

- `Pathfinding_Dirty_Light.png`

- `Pathfinding_Disabled_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `Sync_Disabled.png`

- `Sync_Enabled.png`

- `Sync_Progress_1.png`

- `Sync_Progress_2.png`

- `Sync_Progress_3.png`

- `Sync_Progress_4.png`

- `Sync_Progress_5.png`

- `Sync_Progress_6.png`

- `Toolbar_Gesture_btn.png`

- `TrashItem_Disabled.png`

- `TrashItem_Menu.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `call_end_icon_24x24.png`

- `call_icon_24x24.png`

- `check_mark.png`

- `collapse_to_one_line.png`

- `edit_mine.png`

- `edit_mine_h.png`

- `edit_theirs.png`

- `edit_theirs_h.png`

- `expand_one_liner.png`

- `genie_icon_24x24.png`

- `gift_icon_24x24.png`

- `icn_toolbar_inventory.tga`

- `icn_toolbar_sidebar.png`

- `icn_toolbar_speak.png`

- `icon_avatar_online.png`

- `nearby_chat_icon.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `profile_icon_24x24.png`

- `request_tp_icon_24x24.png`

- `sale_icon_24x24.png`

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

- `see_me_online.png`

- `see_me_online_h.png`

- `see_on_map.png`

- `see_on_map_h.png`

- `teleport_menu.png`

- `unknown_icon.png`


## indra/newview/skins/starlight/themes/silver_blue/textures/model_wizard/ (3 files)

- `divider_line.png`

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/starlight/themes/silver_blue/textures/navbar/ (36 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/starlight/themes/silver_blue/textures/taskpanel/ (42 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`

- `translate_icon_24x24.png`


## indra/newview/skins/starlight/themes/silver_blue/textures/toolbar_icons/ (59 files)

- `Environment.png`

- `animation_override.png`

- `appearance.png`

- `areasearch.png`

- `asset_blacklist.png`

- `avatars.png`

- `blocklist.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `chat.png`

- `contact_sets.png`

- `destinations.png`

- `facebook.png`

- `gestures.png`

- `google.png`

- `gridstatus.png`

- `groundsit.png`

- `group_titles.png`

- `highlighting.png`

- `highlighting_selected.png`

- `howto.png`

- `inventory.png`

- `land.png`

- `landmark_here.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `mouselook.png`

- `move.png`

- `movelock.png`

- `nearbychat.png`

- `nearbyvoice.png`

- `outbox.png`

- `people.png`

- `phoenix.png`

- `phototools_cam.png`

- `phototools_fs.png`

- `picks.png`

- `places.png`

- `posestand.png`

- `preferences.png`

- `profile.png`

- `radar.png`

- `region.png`

- `resync_animations.png`

- `search.png`

- `settings_debug.png`

- `snapshot.png`

- `snapshot_to_disk.png`

- `sound_explorer.png`

- `speak.png`

- `statistics.png`

- `teleporthistory.png`

- `teleporthome.png`

- `translate.png`

- `view.png`


## indra/newview/skins/starlight/themes/silver_blue/textures/widgets/ (178 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Badge_Background.png`

- `Badge_Background_New.png`

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

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Hover.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `button_disabled_32x128.png`

- `button_enabled_32x128.png`

- `button_enabled_selected_32x128.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `horizontal_drag_handle.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`

- `vertical_drag_handle.png`


## indra/newview/skins/starlight/themes/silver_blue/textures/windows/ (52 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Collapse_Foreground.png`

- `Icon_Collapse_Press.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Snooze_Foreground.png`

- `Icon_Snooze_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/starlight/themes/silver_blue/textures/world/ (1 files)

- `NoEntryLines.png`


## indra/newview/skins/starlight/themes/silver_pink/ (1 files)

- `colors.xml`


## indra/newview/skins/starlight/themes/silver_pink/textures/ (143 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_keys.png`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `green_checkmark.png`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_avatar_online_h.tga`

- `icon_day_cycle.tga`

- `icon_day_cycle_12am.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `payment_info_used.tga`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `red_x.png`

- `rounded_square.j2c`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/starlight/themes/silver_pink/textures/bottomtray/ (104 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Off_pref.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Off_Pref.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `TabIcon_Things_Bottomtray.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `camera_load.png`

- `camera_store.png`

- `chatbar_18.png`

- `inventory_18.png`

- `starlight_build.png`

- `starlight_camera.png`

- `starlight_map.png`

- `starlight_minimap.png`

- `starlight_move.png`

- `starlight_search.png`

- `starlight_snapshot.png`


## indra/newview/skins/starlight/themes/silver_pink/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/starlight/themes/silver_pink/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/starlight/themes/silver_pink/textures/icons/ (308 files)

- `AddItem_Disabled.png`

- `AddItem_Menu.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Chat_History.png`

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

- `Conv_toolbar_plus.png`

- `Conv_toolbar_sort.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Draw_Distance.png`

- `Edit_Flip_X.png`

- `Edit_Prefs_Wrench.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Friends_Icon_24x24.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_DialogStack.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_FolderClosed.png`

- `Inv_FolderOpen.png`

- `Inv_Gesture.png`

- `Inv_Gift.png`

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

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_WaterLight.png`

- `Inv_WindLight.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `Music_Off.png`

- `Music_Over.png`

- `Music_Press.png`

- `Muted_Chat.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_On_Selected.png`

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

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Parcel_WindLight.png`

- `Pathfinding_Dirty_Light.png`

- `Pathfinding_Disabled_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `Sync_Disabled.png`

- `Sync_Enabled.png`

- `Sync_Progress_1.png`

- `Sync_Progress_2.png`

- `Sync_Progress_3.png`

- `Sync_Progress_4.png`

- `Sync_Progress_5.png`

- `Sync_Progress_6.png`

- `Toolbar_Gesture_btn.png`

- `TrashItem_Disabled.png`

- `TrashItem_Menu.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `call_end_icon_24x24.png`

- `call_icon_24x24.png`

- `check_mark.png`

- `collapse_to_one_line.png`

- `edit_mine.png`

- `edit_mine_h.png`

- `edit_theirs.png`

- `edit_theirs_h.png`

- `expand_one_liner.png`

- `genie_icon_24x24.png`

- `gift_icon_24x24.png`

- `icn_toolbar_inventory.tga`

- `icn_toolbar_sidebar.png`

- `icn_toolbar_speak.png`

- `icon_avatar_online.png`

- `nearby_chat_icon.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `profile_icon_24x24.png`

- `request_tp_icon_24x24.png`

- `sale_icon_24x24.png`

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

- `see_me_online.png`

- `see_me_online_h.png`

- `see_on_map.png`

- `see_on_map_h.png`

- `teleport_menu.png`

- `unknown_icon.png`


## indra/newview/skins/starlight/themes/silver_pink/textures/model_wizard/ (3 files)

- `divider_line.png`

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/starlight/themes/silver_pink/textures/navbar/ (36 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/starlight/themes/silver_pink/textures/taskpanel/ (42 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`

- `translate_icon_24x24.png`


## indra/newview/skins/starlight/themes/silver_pink/textures/toolbar_icons/ (59 files)

- `Environment.png`

- `animation_override.png`

- `appearance.png`

- `areasearch.png`

- `asset_blacklist.png`

- `avatars.png`

- `blocklist.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `chat.png`

- `contact_sets.png`

- `destinations.png`

- `facebook.png`

- `gestures.png`

- `google.png`

- `gridstatus.png`

- `groundsit.png`

- `group_titles.png`

- `highlighting.png`

- `highlighting_selected.png`

- `howto.png`

- `inventory.png`

- `land.png`

- `landmark_here.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `mouselook.png`

- `move.png`

- `movelock.png`

- `nearbychat.png`

- `nearbyvoice.png`

- `outbox.png`

- `people.png`

- `phoenix.png`

- `phototools_cam.png`

- `phototools_fs.png`

- `picks.png`

- `places.png`

- `posestand.png`

- `preferences.png`

- `profile.png`

- `radar.png`

- `region.png`

- `resync_animations.png`

- `search.png`

- `settings_debug.png`

- `snapshot.png`

- `snapshot_to_disk.png`

- `sound_explorer.png`

- `speak.png`

- `statistics.png`

- `teleporthistory.png`

- `teleporthome.png`

- `translate.png`

- `view.png`


## indra/newview/skins/starlight/themes/silver_pink/textures/widgets/ (178 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Badge_Background.png`

- `Badge_Background_New.png`

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

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Hover.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `SpeakBtn_Left_Off.png`

- `SpeakBtn_Left_Selected_Press.png`

- `SpeakBtn_Right_Off.png`

- `SpeakBtn_Right_Selected_Press.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `button_disabled_32x128.png`

- `button_enabled_32x128.png`

- `button_enabled_selected_32x128.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `horizontal_drag_handle.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`

- `vertical_drag_handle.png`


## indra/newview/skins/starlight/themes/silver_pink/textures/windows/ (52 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Collapse_Foreground.png`

- `Icon_Collapse_Press.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Snooze_Foreground.png`

- `Icon_Snooze_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/starlight/themes/silver_pink/textures/world/ (1 files)

- `NoEntryLines.png`


## indra/newview/skins/starlight/xui/de/ (1 files)

- `panel_status_bar.xml`


## indra/newview/skins/starlight/xui/en/ (59 files)

- `favorites_bar_button.xml`

- `floater_avatar_textures.xml`

- `floater_buy_object.xml`

- `floater_critical.xml`

- `floater_im_container.xml`

- `floater_map.xml`

- `floater_region_restarting.xml`

- `floater_script.xml`

- `floater_sell_land.xml`

- `floater_side_bar_tab.xml`

- `floater_test_line_editor.xml`

- `floater_test_widgets.xml`

- `floater_tools.xml`

- `floater_ui_preview.xml`

- `floater_world_map.xml`

- `main_view.xml`

- `panel_avatar_tag.xml`

- `panel_classified_info.xml`

- `panel_classifieds_list_item.xml`

- `panel_clothing_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_edit_classified.xml`

- `panel_edit_pick.xml`

- `panel_edit_profile.xml`

- `panel_edit_wearable.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_generic_tip.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_hint.xml`

- `panel_landmark_info.xml`

- `panel_main_inventory.xml`

- `panel_media_settings_security.xml`

- `panel_my_profile.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_media.xml`

- `panel_notes.xml`

- `panel_outfit_edit.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_pick_info.xml`

- `panel_pick_list_item.xml`

- `panel_picks.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_status_bar.xml`

- `panel_sys_well_item.xml`

- `panel_teleport_history.xml`

- `panel_toolbar_view.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_task_info.xml`


## indra/newview/skins/starlight/xui/en/widgets/ (20 files)

- `avatar_list_item.xml`

- `chiclet_im_p2p.xml`

- `deletable_wearable_list_item.xml`

- `drop_down.xml`

- `floater.xml`

- `fs_chiclet_im_p2p.xml`

- `gesture_combo_list.xml`

- `icon.xml`

- `inventory_list_item.xml`

- `inventory_panel.xml`

- `location_input.xml`

- `panel.xml`

- `recent_inventory_panel.xml`

- `scroll_container.xml`

- `simple_text_editor.xml`

- `tab_container.xml`

- `talk_button.xml`

- `toolbar.xml`

- `toolbar_vertical.xml`

- `worn_inventory_panel.xml`


## indra/newview/skins/starlight/xui/es/ (7 files)

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_roles.xml`

- `panel_navigation_bar.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlight/xui/it/ (8 files)

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_navigation_bar.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlight/xui/ja/ (9 files)

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_main_inventory.xml`

- `panel_navigation_bar.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlight/xui/pl/ (8 files)

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_navigation_bar.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlight/xui/pt/ (1 files)

- `panel_status_bar.xml`


## indra/newview/skins/starlight/xui/ru/ (7 files)

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_roles.xml`

- `panel_navigation_bar.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlight/xui/zh/ (9 files)

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_main_inventory.xml`

- `panel_navigation_bar.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlightcui/ (1 files)

- `colors.xml`


## indra/newview/skins/starlightcui/textures/ (155 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_keys.png`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `flyout_btn_left.tga`

- `flyout_btn_left_disabled.tga`

- `flyout_btn_left_selected.tga`

- `flyout_btn_right.tga`

- `flyout_btn_right_disabled.tga`

- `flyout_btn_right_selected.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `glowtouchables.tga`

- `green_checkmark.png`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-call-end.tga`

- `icn_voice-call-start.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-off.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on-lvl3.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_avatar_online_h.tga`

- `icon_day_cycle.tga`

- `icon_day_cycle_12am.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_32.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `red_x.png`

- `rounded_square.j2c`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `textures.xml`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/starlightcui/textures/bottomtray/ (102 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Off_Pref.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Off_Pref.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `TabIcon_Things_Bottomtray.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `chatbar_18.png`

- `inventory_18.png`

- `starlight_build.png`

- `starlight_camera.png`

- `starlight_map.png`

- `starlight_minimap.png`

- `starlight_move.png`

- `starlight_search.png`

- `starlight_snapshot.png`


## indra/newview/skins/starlightcui/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/starlightcui/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/starlightcui/textures/icons/ (272 files)

- `AddItem_Disabled.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Draw_Distance.png`

- `Edit_Prefs_Wrench.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_FolderClosed.png`

- `Inv_FolderOpen.png`

- `Inv_Gesture.png`

- `Inv_Gift.png`

- `Inv_Gloves.png`

- `Inv_Hair.png`

- `Inv_Invalid.png`

- `Inv_Jacket.png`

- `Inv_Landmark.png`

- `Inv_Link.png`

- `Inv_LinkFolder.png`

- `Inv_LinkItem.png`

- `Inv_LinkItem_Broken.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderOpen.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_Universal.png`

- `Inv_WaterLight.png`

- `Inv_WindLight.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `Music_Off.png`

- `Music_Over.png`

- `Music_Press.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_On_Selected.png`

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

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

- `PowerOff_Off.png`

- `PowerOff_Over.png`

- `PowerOff_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `Sync_Disabled.png`

- `Sync_Enabled.png`

- `Sync_Progress_1.png`

- `Sync_Progress_2.png`

- `Sync_Progress_3.png`

- `Sync_Progress_4.png`

- `Sync_Progress_5.png`

- `Sync_Progress_6.png`

- `Toolbar_Gesture_btn.png`

- `TrashItem_Disabled.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `check_mark.png`

- `edit_mine.png`

- `edit_mine_h.png`

- `edit_theirs.png`

- `edit_theirs_h.png`

- `icn_toolbar_inventory.tga`

- `icn_toolbar_sidebar.png`

- `icn_toolbar_speak.png`

- `icon_avatar_online.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `see_me_online.png`

- `see_me_online_h.png`

- `see_on_map.png`

- `see_on_map_h.png`

- `unknown_icon.png`


## indra/newview/skins/starlightcui/textures/model_wizard/ (3 files)

- `divider_line.png`

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/starlightcui/textures/navbar/ (36 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/starlightcui/textures/taskpanel/ (41 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`


## indra/newview/skins/starlightcui/textures/toolbar_icons/ (44 files)

- `Environment.png`

- `animation_override.png`

- `appearance.png`

- `areasearch.png`

- `avatars.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `chat.png`

- `destinations.png`

- `gestures.png`

- `google.png`

- `gridstatus.png`

- `highlighting.png`

- `highlighting_selected.png`

- `howto.png`

- `inventory.png`

- `land.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `move.png`

- `nearbychat.png`

- `nearbyvoice.png`

- `outbox.png`

- `people.png`

- `phoenix.png`

- `phototools_cam.png`

- `phototools_fs.png`

- `picks.png`

- `places.png`

- `preferences.png`

- `profile.png`

- `region.png`

- `search.png`

- `settings_debug.png`

- `snapshot.png`

- `speak.png`

- `statistics.png`

- `teleporthome.png`

- `translate.png`

- `view.png`


## indra/newview/skins/starlightcui/textures/widgets/ (170 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Badge_Background.png`

- `Badge_Background_New.png`

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

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Hover.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

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

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`


## indra/newview/skins/starlightcui/textures/windows/ (48 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/starlightcui/themes/custom_dark/ (1 files)

- `colors.xml`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/ (154 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_keys.png`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `flyout_btn_left.tga`

- `flyout_btn_left_disabled.tga`

- `flyout_btn_left_selected.tga`

- `flyout_btn_right.tga`

- `flyout_btn_right_disabled.tga`

- `flyout_btn_right_selected.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `glowtouchables.tga`

- `green_checkmark.png`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-call-end.tga`

- `icn_voice-call-start.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-off.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on-lvl3.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_avatar_online_h.tga`

- `icon_day_cycle.tga`

- `icon_day_cycle_12am.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_32.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `red_x.png`

- `rounded_square.j2c`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/bottomtray/ (102 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Off_Pref.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Off_Pref.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `TabIcon_Things_Bottomtray.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `chatbar_18.png`

- `inventory_18.png`

- `starlight_build.png`

- `starlight_camera.png`

- `starlight_map.png`

- `starlight_minimap.png`

- `starlight_move.png`

- `starlight_search.png`

- `starlight_snapshot.png`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/icons/ (271 files)

- `AddItem_Disabled.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Draw_Distance.png`

- `Edit_Prefs_Wrench.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_FolderClosed.png`

- `Inv_FolderOpen.png`

- `Inv_Gesture.png`

- `Inv_Gift.png`

- `Inv_Gloves.png`

- `Inv_Hair.png`

- `Inv_Invalid.png`

- `Inv_Jacket.png`

- `Inv_Landmark.png`

- `Inv_Link.png`

- `Inv_LinkFolder.png`

- `Inv_LinkItem.png`

- `Inv_LinkItem_Broken.png`

- `Inv_LookFolderClosed.png`

- `Inv_LookFolderOpen.png`

- `Inv_LostClosed.png`

- `Inv_LostOpen.png`

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_WaterLight.png`

- `Inv_WindLight.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `Music_Off.png`

- `Music_Over.png`

- `Music_Press.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_On_Selected.png`

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

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

- `PowerOff_Off.png`

- `PowerOff_Over.png`

- `PowerOff_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `Sync_Disabled.png`

- `Sync_Enabled.png`

- `Sync_Progress_1.png`

- `Sync_Progress_2.png`

- `Sync_Progress_3.png`

- `Sync_Progress_4.png`

- `Sync_Progress_5.png`

- `Sync_Progress_6.png`

- `Toolbar_Gesture_btn.png`

- `TrashItem_Disabled.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `check_mark.png`

- `edit_mine.png`

- `edit_mine_h.png`

- `edit_theirs.png`

- `edit_theirs_h.png`

- `icn_toolbar_inventory.tga`

- `icn_toolbar_sidebar.png`

- `icn_toolbar_speak.png`

- `icon_avatar_online.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `see_me_online.png`

- `see_me_online_h.png`

- `see_on_map.png`

- `see_on_map_h.png`

- `unknown_icon.png`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/model_wizard/ (3 files)

- `divider_line.png`

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/navbar/ (36 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/taskpanel/ (41 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/toolbar_icons/ (44 files)

- `animation_override.png`

- `appearance.png`

- `areasearch.png`

- `avatars.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `chat.png`

- `destinations.png`

- `environments.png`

- `gestures.png`

- `google.png`

- `gridstatus.png`

- `highlighting.png`

- `highlighting_selected.png`

- `howto.png`

- `inventory.png`

- `land.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `move.png`

- `nearbychat.png`

- `nearbyvoice.png`

- `outbox.png`

- `people.png`

- `phoenix.png`

- `phototools_cam.png`

- `phototools_fs.png`

- `picks.png`

- `places.png`

- `preferences.png`

- `profile.png`

- `region.png`

- `search.png`

- `settings_debug.png`

- `snapshot.png`

- `speak.png`

- `statistics.png`

- `teleporthome.png`

- `translate.png`

- `view.png`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/widgets/ (170 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

- `Arrow_Small_Left.png`

- `Arrow_Small_Right.png`

- `Arrow_Small_Up.png`

- `Arrow_Up.png`

- `Badge_Background.png`

- `Badge_Background_New.png`

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

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Hover.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

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

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `ScrubberThumb_Disabled.png`

- `ScrubberThumb_Focus.png`

- `ScrubberThumb_Off.png`

- `ScrubberThumb_Over.png`

- `ScrubberThumb_Press.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

- `Tooltip.png`

- `bevel_background.png`

- `buy_off.png`

- `buy_over.png`

- `buy_press.png`

- `jump_left_in.png`

- `jump_left_out.png`

- `jump_right_in.png`

- `jump_right_out.png`


## indra/newview/skins/starlightcui/themes/custom_dark/textures/windows/ (48 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/starlightcui/themes/custom_light/ (1 files)

- `colors.xml`


## indra/newview/skins/starlightcui/themes/custom_light/textures/ (143 files)

- `Blank.png`

- `BottomTray_BG.png`

- `Rounded_Rect.png`

- `TaskPanel_BG.png`

- `active_speakers.tga`

- `alpha_gradient.tga`

- `alpha_gradient_2d.j2c`

- `arrow_down.tga`

- `arrow_keys.png`

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

- `checkerboard_transparency_bg.png`

- `circle.tga`

- `cloud-particle.j2c`

- `color_swatch_alpha.tga`

- `crosshairs.tga`

- `default_land_picture.j2c`

- `default_profile_picture.j2c`

- `direction_arrow.tga`

- `down_arrow.png`

- `eye_button_active.tga`

- `eye_button_inactive.tga`

- `folder_arrow.tga`

- `foot_shadow.j2c`

- `green_checkmark.png`

- `icn_active-speakers-dot-lvl0.tga`

- `icn_active-speakers-dot-lvl1.tga`

- `icn_active-speakers-dot-lvl2.tga`

- `icn_active-speakers-typing1.tga`

- `icn_active-speakers-typing2.tga`

- `icn_active-speakers-typing3.tga`

- `icn_chatbar.tga`

- `icn_label_media.tga`

- `icn_label_music.tga`

- `icn_label_web.tga`

- `icn_media.tga`

- `icn_media_movie.tga`

- `icn_media_web.tga`

- `icn_pause.tga`

- `icn_play.tga`

- `icn_rounded-text-field.tga`

- `icn_speaker-muted_dark.tga`

- `icn_speaker_dark.tga`

- `icn_stop.tga`

- `icn_voice-groupfocus.tga`

- `icn_voice-localchat.tga`

- `icn_voice-pvtfocus.tga`

- `icn_voice_ptt-on-lvl1.tga`

- `icn_voice_ptt-on-lvl2.tga`

- `icn_voice_ptt-on.tga`

- `icon_avatar_offline.tga`

- `icon_avatar_online.tga`

- `icon_avatar_online_h.tga`

- `icon_day_cycle.tga`

- `icon_day_cycle_12am.tga`

- `icon_diurnal.tga`

- `icon_event.tga`

- `icon_event_adult.tga`

- `icon_event_mature.tga`

- `icon_for_sale.tga`

- `icon_for_sale_adult.tga`

- `icon_lock.tga`

- `icon_top_pick.tga`

- `image_edit_icon.tga`

- `inv_folder_animation.tga`

- `inv_folder_inbox.tga`

- `jump_left_in.tga`

- `jump_left_out.tga`

- `jump_right_in.tga`

- `jump_right_out.tga`

- `lag_status_critical.tga`

- `lag_status_good.tga`

- `lag_status_warning.tga`

- `legend.tga`

- `locked_image.j2c`

- `map_avatar_16.tga`

- `map_avatar_32.tga`

- `map_avatar_8.tga`

- `map_avatar_above_32.tga`

- `map_avatar_above_8.tga`

- `map_avatar_below_32.tga`

- `map_avatar_below_8.tga`

- `map_avatar_unknown_32.tga`

- `map_avatar_you_8.tga`

- `map_event.tga`

- `map_event_adult.tga`

- `map_event_mature.tga`

- `map_home.tga`

- `map_infohub.tga`

- `map_telehub.tga`

- `map_track_16.tga`

- `map_track_8.tga`

- `menu_bar.tga`

- `menu_separator.png`

- `missing_asset.tga`

- `mute_icon.tga`

- `notify_box_icon.tga`

- `notify_caution_icon.tga`

- `notify_next.png`

- `payment_info_used.tga`

- `pixiesmall.j2c`

- `places_rating_adult.tga`

- `places_rating_mature.tga`

- `places_rating_pg.tga`

- `propertyline.tga`

- `ptt_lock_off.tga`

- `ptt_lock_on.tga`

- `red_x.png`

- `rounded_square.j2c`

- `script_error.j2c`

- `show_btn.tga`

- `show_btn_selected.tga`

- `silhouette.j2c`

- `slim_icon_16_viewer.tga`

- `smicon_warn.tga`

- `snapshot_download.png`

- `snapshot_email.png`

- `spacer24-2.tga`

- `spacer24.tga`

- `spacer35.tga`

- `square_btn_32x128.tga`

- `square_btn_selected_32x128.tga`

- `startup_logo.j2c`

- `status_busy.tga`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `toggle_button_off.png`

- `toggle_button_selected.png`

- `transparent.j2c`

- `up_arrow.png`

- `uv_test1.j2c`

- `uv_test2.tga`

- `voice_meter_dot.j2c`

- `voice_meter_rings.j2c`

- `white.tga`


## indra/newview/skins/starlightcui/themes/custom_light/textures/bottomtray/ (104 files)

- `BottomTray_BG.png`

- `Cam_Avatar_Disabled.png`

- `Cam_Avatar_Off.png`

- `Cam_Avatar_Over.png`

- `Cam_Avatar_Press.png`

- `Cam_FreeCam_Disabled.png`

- `Cam_FreeCam_Off.png`

- `Cam_FreeCam_Off_pref.png`

- `Cam_FreeCam_Over.png`

- `Cam_FreeCam_Press.png`

- `Cam_Orbit_Disabled.png`

- `Cam_Orbit_Off.png`

- `Cam_Orbit_Over.png`

- `Cam_Orbit_Press.png`

- `Cam_Pan_Disabled.png`

- `Cam_Pan_Off.png`

- `Cam_Pan_Over.png`

- `Cam_Pan_Press.png`

- `Cam_Preset_Back_Off.png`

- `Cam_Preset_Back_On.png`

- `Cam_Preset_Eye_Off.png`

- `Cam_Preset_Eye_On.png`

- `Cam_Preset_Front_Off.png`

- `Cam_Preset_Front_On.png`

- `Cam_Preset_Side_Off.png`

- `Cam_Preset_Side_On.png`

- `Cam_Preset_TPP_Off.png`

- `Cam_Preset_TPP_On.png`

- `Cam_Rotate_In.png`

- `Cam_Rotate_Out.png`

- `Cam_Tracking_In.png`

- `Cam_Tracking_Out.png`

- `CameraView_Off.png`

- `CameraView_Over.png`

- `CameraView_Press.png`

- `ChatBarHandle.png`

- `DownArrow.png`

- `Mouselook_View_Off.png`

- `Mouselook_View_On.png`

- `Move_Fly_Disabled.png`

- `Move_Fly_Off.png`

- `Move_Fly_Over.png`

- `Move_Fly_Press.png`

- `Move_Run_Disabled.png`

- `Move_Run_Off.png`

- `Move_Run_Over.png`

- `Move_Run_Press.png`

- `Move_Walk_Disabled.png`

- `Move_Walk_Off.png`

- `Move_Walk_Off_Pref.png`

- `Move_Walk_Over.png`

- `Move_Walk_Press.png`

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

- `NearbyVoice_Lvl1.png`

- `NearbyVoice_Lvl2.png`

- `NearbyVoice_Lvl3.png`

- `NearbyVoice_On.png`

- `Notices_Unread.png`

- `Object_View_Off.png`

- `Object_View_On.png`

- `PanOrbit_Disabled.png`

- `PanOrbit_Off.png`

- `PanOrbit_Over.png`

- `PanOrbit_Press.png`

- `Snapshot_Off.png`

- `Snapshot_Over.png`

- `Snapshot_Press.png`

- `TabIcon_Things_Bottomtray.png`

- `Unread_Chiclet.png`

- `Unread_IM.png`

- `Unread_Msg.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `WellButton_Lit.png`

- `WellButton_Lit_Selected.png`

- `camera_load.png`

- `camera_store.png`

- `chatbar_18.png`

- `inventory_18.png`

- `starlight_build.png`

- `starlight_camera.png`

- `starlight_map.png`

- `starlight_minimap.png`

- `starlight_move.png`

- `starlight_search.png`

- `starlight_snapshot.png`


## indra/newview/skins/starlightcui/themes/custom_light/textures/build/ (40 files)

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

- `Tool_Create_Selected.png`

- `Tool_Dozer.png`

- `Tool_Dozer_Selected.png`

- `Tool_Face.png`

- `Tool_Face_Selected.png`

- `Tool_Grab.png`

- `Tool_Grab_Selected.png`

- `Tool_Zoom.png`

- `Tool_Zoom_Selected.png`


## indra/newview/skins/starlightcui/themes/custom_light/textures/containers/ (40 files)

- `Accordion_ArrowClosed_Off.png`

- `Accordion_ArrowClosed_Over.png`

- `Accordion_ArrowClosed_Press.png`

- `Accordion_ArrowOpened_Off.png`

- `Accordion_ArrowOpened_Over.png`

- `Accordion_ArrowOpened_Press.png`

- `Accordion_Off.png`

- `Accordion_Over.png`

- `Accordion_Press.png`

- `Accordion_Selected.png`

- `Container.png`

- `TabTop_Divider.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Over.png`

- `TabTop_Left_Selected.png`

- `TabTop_Middle_Off.png`

- `TabTop_Middle_Over.png`

- `TabTop_Middle_Press.png`

- `TabTop_Middle_Selected.png`

- `TabTop_Right_Off.png`

- `TabTop_Right_Over.png`

- `TabTop_Right_Press.png`

- `TabTop_Right_Selected.png`

- `Toolbar_Divider.png`

- `Toolbar_Left_Flash.png`

- `Toolbar_Left_Off.png`

- `Toolbar_Left_Over.png`

- `Toolbar_Left_Press.png`

- `Toolbar_Left_Selected.png`

- `Toolbar_Middle_Flash.png`

- `Toolbar_Middle_Off.png`

- `Toolbar_Middle_Over.png`

- `Toolbar_Middle_Press.png`

- `Toolbar_Middle_Selected.png`

- `Toolbar_Right_Flash.png`

- `Toolbar_Right_Off.png`

- `Toolbar_Right_Over.png`

- `Toolbar_Right_Press.png`

- `Toolbar_Right_Selected.png`

- `tabtop_Left_Press.png`


## indra/newview/skins/starlightcui/themes/custom_light/textures/icons/ (311 files)

- `AddItem_Disabled.png`

- `AddItem_Menu.png`

- `AddItem_Off.png`

- `AddItem_Over.png`

- `AddItem_Press.png`

- `AudioMute_Off.png`

- `AudioMute_Over.png`

- `AudioMute_Press.png`

- `Audio_Off.png`

- `Audio_Over.png`

- `Audio_Press.png`

- `BackArrow_Disabled.png`

- `BackArrow_Off.png`

- `BackArrow_Over.png`

- `BackArrow_Press.png`

- `Chat_History.png`

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

- `Conv_toolbar_plus.png`

- `Conv_toolbar_sort.png`

- `Copy.png`

- `DownArrow_Off.png`

- `DragHandle.png`

- `Draw_Distance.png`

- `Edit_Flip_X.png`

- `Edit_Prefs_Wrench.png`

- `Edit_Wrench.png`

- `ExternalBrowser_Off.png`

- `ExternalBrowser_Over.png`

- `ExternalBrowser_Press.png`

- `Female.png`

- `ForSale_Badge.png`

- `ForwardArrow_Off.png`

- `ForwardArrow_Press.png`

- `Friends_Icon_24x24.png`

- `Generic_Group.png`

- `Generic_Group_Large.png`

- `Generic_Object.png`

- `Generic_Object_Large.png`

- `Generic_Object_Medium.png`

- `Generic_Object_Small.png`

- `Generic_Person.png`

- `Generic_Person_Large.png`

- `Hierarchy_View_Disabled.png`

- `Hierarchy_View_On.png`

- `Icon_DialogStack.png`

- `Icon_For_Sale.png`

- `Info.png`

- `Info_Over.png`

- `Info_Small.png`

- `Inv_Accessories.png`

- `Inv_Alpha.png`

- `Inv_Animation.png`

- `Inv_BodyShape.png`

- `Inv_CallingCard.png`

- `Inv_Clothing.png`

- `Inv_DangerousScript.png`

- `Inv_Eye.png`

- `Inv_FolderClosed.png`

- `Inv_FolderOpen.png`

- `Inv_Gesture.png`

- `Inv_Gift.png`

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

- `Inv_Mesh.png`

- `Inv_Notecard.png`

- `Inv_Object.png`

- `Inv_Object_Multi.png`

- `Inv_Pants.png`

- `Inv_Physics.png`

- `Inv_Script.png`

- `Inv_Shirt.png`

- `Inv_Shoe.png`

- `Inv_Skin.png`

- `Inv_Skirt.png`

- `Inv_Snapshot.png`

- `Inv_Socks.png`

- `Inv_Sound.png`

- `Inv_SysClosed.png`

- `Inv_SysClosed.tga`

- `Inv_SysOpen.png`

- `Inv_SysOpen.tga`

- `Inv_Tattoo.png`

- `Inv_Texture.png`

- `Inv_Trash.png`

- `Inv_TrashClosed.png`

- `Inv_TrashOpen.png`

- `Inv_Underpants.png`

- `Inv_Undershirt.png`

- `Inv_WaterLight.png`

- `Inv_WindLight.png`

- `List_View_Disabled.png`

- `List_View_On.png`

- `Lock.png`

- `Locked_Icon.png`

- `Male.png`

- `Microphone_Mute.png`

- `Microphone_On.png`

- `MinusItem_Disabled.png`

- `MinusItem_Off.png`

- `MinusItem_Press.png`

- `Music_Off.png`

- `Music_Over.png`

- `Music_Press.png`

- `Muted_Chat.png`

- `OptionsMenu_Disabled.png`

- `OptionsMenu_Off.png`

- `OptionsMenu_Over.png`

- `OptionsMenu_Press.png`

- `OutboxPush_Disabled.png`

- `OutboxPush_Off.png`

- `OutboxPush_On.png`

- `OutboxPush_On_Over.png`

- `OutboxPush_On_Selected.png`

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

- `Parcel_Build_Light.png`

- `Parcel_DamageNo_Dark.png`

- `Parcel_Damage_Dark.png`

- `Parcel_Damage_Light_Alt.png`

- `Parcel_Evry_Color.png`

- `Parcel_Evry_Dark.png`

- `Parcel_Evry_Light.png`

- `Parcel_Exp_Color.png`

- `Parcel_Exp_Dark.png`

- `Parcel_Exp_Light.png`

- `Parcel_FlyNo_Dark.png`

- `Parcel_FlyNo_Light.png`

- `Parcel_Fly_Dark.png`

- `Parcel_Fly_Light.png`

- `Parcel_ForSaleNo_Dark.png`

- `Parcel_ForSaleNo_Light.png`

- `Parcel_ForSale_Dark.png`

- `Parcel_ForSale_Light.png`

- `Parcel_Health_Dark.png`

- `Parcel_M_Color.png`

- `Parcel_M_Dark.png`

- `Parcel_M_Light.png`

- `Parcel_NoScripts_Light.png`

- `Parcel_PG_Dark.png`

- `Parcel_PG_Light.png`

- `Parcel_PushNo_Dark.png`

- `Parcel_PushNo_Light.png`

- `Parcel_Push_Dark.png`

- `Parcel_Push_Light.png`

- `Parcel_R_Dark.png`

- `Parcel_R_Light.png`

- `Parcel_ScriptsNo_Dark.png`

- `Parcel_Scripts_Dark.png`

- `Parcel_Scripts_Light.png`

- `Parcel_SeeAVsOff_Dark.png`

- `Parcel_SeeAVsOff_Light.png`

- `Parcel_SeeAVsOn_Dark.png`

- `Parcel_SeeAVsOn_Light.png`

- `Parcel_VoiceNo_Dark.png`

- `Parcel_VoiceNo_Light.png`

- `Parcel_Voice_Dark.png`

- `Parcel_Voice_Light.png`

- `Parcel_WindLight.png`

- `Pathfinding_Dirty_Light.png`

- `Pathfinding_Disabled_Light.png`

- `Pause_Off.png`

- `Pause_Over.png`

- `Pause_Press.png`

- `Person_Check.png`

- `Person_Star.png`

- `Play_Off.png`

- `Play_Over.png`

- `Play_Press.png`

- `PowerOn_Off.png`

- `PowerOn_Over.png`

- `PowerOn_Press.png`

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

- `REC_Off.png`

- `REC_On.png`

- `Refresh_Disabled.png`

- `Refresh_Off.png`

- `Refresh_Press.png`

- `SL_Logo.png`

- `Search_Icon.png`

- `Shirt_Large.png`

- `Shop.png`

- `SkipBackward_Off.png`

- `SkipBackward_Over.png`

- `SkipBackward_Press.png`

- `SkipForward_Off.png`

- `SkipForward_Over.png`

- `SkipForward_Press.png`

- `StopReload_Off.png`

- `StopReload_Over.png`

- `StopReload_Press.png`

- `Stop_Off.png`

- `Stop_Over.png`

- `Stop_Press.png`

- `Sync_Disabled.png`

- `Sync_Enabled.png`

- `Sync_Progress_1.png`

- `Sync_Progress_2.png`

- `Sync_Progress_3.png`

- `Sync_Progress_4.png`

- `Sync_Progress_5.png`

- `Sync_Progress_6.png`

- `Toolbar_Gesture_btn.png`

- `TrashItem_Disabled.png`

- `TrashItem_Menu.png`

- `TrashItem_Off.png`

- `TrashItem_Over.png`

- `TrashItem_Press.png`

- `UnZoom_Off.png`

- `UnZoom_Over.png`

- `UnZoom_Press.png`

- `UpArrow_Off.png`

- `VoicePTT_Lvl1.png`

- `VoicePTT_Lvl2.png`

- `VoicePTT_Lvl3.png`

- `VoicePTT_Off.png`

- `VoicePTT_On.png`

- `Web_Profile_Off.png`

- `Widget_DownArrow.png`

- `Widget_UpArrow.png`

- `YouAreHere_Badge.png`

- `Zoom_Off.png`

- `Zoom_Over.png`

- `Zoom_Press.png`

- `avaline_default_icon.jpg`

- `back_arrow_off.png`

- `back_arrow_over.png`

- `back_arrow_press.png`

- `call_end_icon_24x24.png`

- `call_icon_24x24.png`

- `check_mark.png`

- `collapse_to_one_line.png`

- `edit_mine.png`

- `edit_mine_h.png`

- `edit_theirs.png`

- `edit_theirs_h.png`

- `expand_one_liner.png`

- `genie_icon_24x24.png`

- `gift_icon_24x24.png`

- `icn_toolbar_inventory.tga`

- `icn_toolbar_sidebar.png`

- `icn_toolbar_speak.png`

- `icon_avatar_online.png`

- `nearby_chat_icon.png`

- `object_icon.png`

- `parcel_color_EVRY.png`

- `parcel_color_EXP.png`

- `parcel_color_M.png`

- `pop_up_caution.png`

- `profile_icon_24x24.png`

- `request_tp_icon_24x24.png`

- `sale_icon_24x24.png`

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

- `see_me_online.png`

- `see_me_online_h.png`

- `see_on_map.png`

- `see_on_map_h.png`

- `teleport_menu.png`

- `unknown_icon.png`


## indra/newview/skins/starlightcui/themes/custom_light/textures/model_wizard/ (3 files)

- `divider_line.png`

- `progress_bar_bg.png`

- `progress_light.png`


## indra/newview/skins/starlightcui/themes/custom_light/textures/navbar/ (36 files)

- `Arrow_Left_Off.png`

- `Arrow_Left_Over.png`

- `Arrow_Left_Press.png`

- `Arrow_Right_Off.png`

- `Arrow_Right_Over.png`

- `Arrow_Right_Press.png`

- `BuyArrow_Off.png`

- `BuyArrow_Over.png`

- `BuyArrow_Press.png`

- `Favorite_Link_Over.png`

- `Favorite_Star_Active.png`

- `Favorite_Star_Off.png`

- `Favorite_Star_Over.png`

- `Favorite_Star_Press.png`

- `FileMenu_BG.png`

- `FileMenu_BarSelect.png`

- `FileMenu_Divider.png`

- `Flag.png`

- `Help_Off.png`

- `Help_Over.png`

- `Help_Press.png`

- `History_Arrow.png`

- `Home_Off.png`

- `Home_Over.png`

- `Home_Press.png`

- `Info_Off.png`

- `Info_Over.png`

- `Info_Press.png`

- `Lock.png`

- `NavBar_BG.png`

- `NavBar_BG_NoFav.png`

- `NavBar_BG_NoFav_Bevel.png`

- `NavBar_BG_NoNav_Bevel.png`

- `Row_Selection.png`

- `Search.png`

- `separator.png`


## indra/newview/skins/starlightcui/themes/custom_light/textures/taskpanel/ (42 files)

- `Activate_Checkmark.png`

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`

- `TabIcon_Appearance_Large.png`

- `TabIcon_Appearance_Off.png`

- `TabIcon_Appearance_Over.png`

- `TabIcon_Appearance_Selected.png`

- `TabIcon_Close_Off.png`

- `TabIcon_Close_Over.png`

- `TabIcon_Home_Large.png`

- `TabIcon_Home_Off.png`

- `TabIcon_Home_Over.png`

- `TabIcon_Home_Selected.png`

- `TabIcon_Inventory_Large.png`

- `TabIcon_Inventory_Off.png`

- `TabIcon_Inventory_Over.png`

- `TabIcon_Inventory_Selected.png`

- `TabIcon_Me_Large.png`

- `TabIcon_Me_Off.png`

- `TabIcon_Me_Over.png`

- `TabIcon_Me_Selected.png`

- `TabIcon_Open_Off.png`

- `TabIcon_Open_Over.png`

- `TabIcon_People_Large.png`

- `TabIcon_People_Off.png`

- `TabIcon_People_Over.png`

- `TabIcon_People_Selected.png`

- `TabIcon_Places_Large.png`

- `TabIcon_Places_Off.png`

- `TabIcon_Places_Over.png`

- `TabIcon_Places_Selected.png`

- `TabIcon_Things_Large.png`

- `TabIcon_Things_Off.png`

- `TabIcon_Things_Over.png`

- `TabIcon_Things_Selected.png`

- `TaskPanel_BG.png`

- `TaskPanel_Tab_Off.png`

- `TaskPanel_Tab_Over.png`

- `TaskPanel_Tab_Selected.png`

- `translate_icon_24x24.png`


## indra/newview/skins/starlightcui/themes/custom_light/textures/toolbar_icons/ (59 files)

- `animation_override.png`

- `appearance.png`

- `areasearch.png`

- `asset_blacklist.png`

- `avatars.png`

- `blocklist.png`

- `build.png`

- `caret_bottom.png`

- `caret_left.png`

- `caret_right.png`

- `chat.png`

- `contact_sets.png`

- `destinations.png`

- `environments.png`

- `facebook.png`

- `gestures.png`

- `google.png`

- `gridstatus.png`

- `groundsit.png`

- `group_titles.png`

- `highlighting.png`

- `highlighting_selected.png`

- `howto.png`

- `inventory.png`

- `land.png`

- `landmark_here.png`

- `map.png`

- `marketplace.png`

- `mini_cart.png`

- `mini_map.png`

- `mouselook.png`

- `move.png`

- `movelock.png`

- `nearbychat.png`

- `nearbyvoice.png`

- `outbox.png`

- `people.png`

- `phoenix.png`

- `phototools_cam.png`

- `phototools_fs.png`

- `picks.png`

- `places.png`

- `posestand.png`

- `preferences.png`

- `profile.png`

- `radar.png`

- `region.png`

- `resync_animations.png`

- `search.png`

- `settings_debug.png`

- `snapshot.png`

- `snapshot_to_disk.png`

- `sound_explorer.png`

- `speak.png`

- `statistics.png`

- `teleporthistory.png`

- `teleporthome.png`

- `translate.png`

- `view.png`


## indra/newview/skins/starlightcui/themes/custom_light/textures/widgets/ (171 files)

- `Arrow_Down.png`

- `Arrow_Left.png`

- `Arrow_Right.png`

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

- `Checkbox_On_Over.png`

- `Checkbox_On_Press.png`

- `Checkbox_Over.png`

- `Checkbox_Press.png`

- `ComboButton_Disabled.png`

- `ComboButton_Hover.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Over.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `ComboButton_UpOff.png`

- `ComboButton_UpSelected.png`

- `ComboButton_Up_On_Selected.png`

- `DisclosureArrow_Closed_Off.png`

- `DisclosureArrow_Closed_Over.png`

- `DisclosureArrow_Closed_Press.png`

- `DisclosureArrow_Opened_Off.png`

- `DisclosureArrow_Opened_Over.png`

- `DisclosureArrow_Opened_Press.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Over.png`

- `DropDown_Press.png`

- `DropDown_Selected.png`

- `DropTarget.png`

- `Error_Tag_Background.png`

- `Linden_Dollar_Alert.png`

- `Linden_Dollar_Background.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `ListItem_Test.png`

- `MarketplaceBtn_Off.png`

- `MarketplaceBtn_Selected.png`

- `New_Tag_Background.png`

- `New_Tag_Border.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_On.png`

- `PushButton_On_Disabled.png`

- `PushButton_On_Over.png`

- `PushButton_On_Selected.png`

- `PushButton_Over.png`

- `PushButton_Press.png`

- `PushButton_Selected.png`

- `PushButton_Selected_Disabled.png`

- `PushButton_Selected_Over.png`

- `PushButton_Selected_Press.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Over.png`

- `RadioButton_On_Press.png`

- `RadioButton_Over.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Down_Opaque.png`

- `ScrollArrow_Down_Over.png`

- `ScrollArrow_Down_Over_Opaque.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Left_Opaque.png`

- `ScrollArrow_Left_Over.png`

- `ScrollArrow_Left_Over_Opaque.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Right_Opaque.png`

- `ScrollArrow_Right_Over.png`

- `ScrollArrow_Right_Over_Opaque.png`

- `ScrollArrow_Up.png`

- `ScrollArrow_Up_Opaque.png`

- `ScrollArrow_Up_Over.png`

- `ScrollArrow_Up_Over_Opaque.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Horiz_Over.png`

- `ScrollThumb_Vert.png`

- `ScrollThumb_Vert_Over.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `SegmentedBtn_Left_Disabled.png`

- `SegmentedBtn_Left_Off.png`

- `SegmentedBtn_Left_On.png`

- `SegmentedBtn_Left_On_Disabled.png`

- `SegmentedBtn_Left_On_Over.png`

- `SegmentedBtn_Left_On_Selected.png`

- `SegmentedBtn_Left_Over.png`

- `SegmentedBtn_Left_Press.png`

- `SegmentedBtn_Left_Selected.png`

- `SegmentedBtn_Left_Selected_Disabled.png`

- `SegmentedBtn_Left_Selected_Over.png`

- `SegmentedBtn_Left_Selected_Press.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Off.png`

- `SegmentedBtn_Middle_On.png`

- `SegmentedBtn_Middle_On_Over.png`

- `SegmentedBtn_Middle_On_Press.png`

- `SegmentedBtn_Middle_Over.png`

- `SegmentedBtn_Middle_Press.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Over.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SegmentedBtn_Right_Disabled.png`

- `SegmentedBtn_Right_Off.png`

- `SegmentedBtn_Right_On.png`

- `SegmentedBtn_Right_On_Over.png`

- `SegmentedBtn_Right_On_Selected.png`

- `SegmentedBtn_Right_Over.png`

- `SegmentedBtn_Right_Press.png`

- `SegmentedBtn_Right_Selected.png`

- `SegmentedBtn_Right_Selected_Disabled.png`

- `SegmentedBtn_Right_Selected_Over.png`

- `SegmentedBtn_Right_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderThumb_Over.png`

- `SliderThumb_Press.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `Stepper_Down_Disabled.png`

- `Stepper_Down_Off.png`

- `Stepper_Down_Over.png`

- `Stepper_Down_Press.png`

- `Stepper_Up_Disabled.png`

- `Stepper_Up_Off.png`

- `Stepper_Up_Over.png`

- `Stepper_Up_Press.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Active.png`

- `TextField_Search_Disabled.png`

- `TextField_Search_Off.png`

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

- `vertical_drag_handle.png`


## indra/newview/skins/starlightcui/themes/custom_light/textures/windows/ (48 files)

- `Dragbar.png`

- `Flyout.png`

- `Flyout_Left.png`

- `Flyout_Pointer.png`

- `Flyout_Pointer_Up.png`

- `Flyout_Right.png`

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Close_Toast.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Gear_Background.png`

- `Icon_Gear_Foreground.png`

- `Icon_Gear_Over.png`

- `Icon_Gear_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Info.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Restore_Foreground.png`

- `Icon_Restore_Press.png`

- `Icon_Undock_Foreground.png`

- `Icon_Undock_Press.png`

- `Inspector_Background.png`

- `Inspector_Hover.png`

- `Inspector_I.png`

- `Login_Pod.png`

- `Resize_Corner.png`

- `TimeBasedMediaBackground.png`

- `Toast_Background.png`

- `Toast_CloseBtn.png`

- `Toast_Over.png`

- `Volume_Background.png`

- `Wearables_Divider.png`

- `WebBasedMediaBackground.png`

- `Window_Background.png`

- `Window_Foreground.png`

- `Window_NoTitle_Background.png`

- `Window_NoTitle_Foreground.png`

- `hint_arrow_down.png`

- `hint_arrow_left.png`

- `hint_arrow_lower_left.png`

- `hint_arrow_right.png`

- `hint_arrow_up.png`

- `hint_background.png`

- `startup_logo.png`

- `yellow_gradient.png`


## indra/newview/skins/starlightcui/xui/az/ (9 files)

- `floater_preferences.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_roles.xml`

- `panel_navigation_bar.xml`

- `panel_preferences_custom_colors.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlightcui/xui/de/ (3 files)

- `floater_preferences.xml`

- `panel_preferences_custom_colors.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlightcui/xui/en/ (67 files)

- `alert_icon.xml`

- `favorites_bar_button.xml`

- `floater_avatar_textures.xml`

- `floater_buy_object.xml`

- `floater_critical.xml`

- `floater_im_container.xml`

- `floater_map.xml`

- `floater_moveview.xml`

- `floater_preferences.xml`

- `floater_price_for_listing.xml`

- `floater_region_restarting.xml`

- `floater_script.xml`

- `floater_sell_land.xml`

- `floater_side_bar_tab.xml`

- `floater_test_line_editor.xml`

- `floater_test_widgets.xml`

- `floater_tools.xml`

- `floater_ui_preview.xml`

- `floater_world_map.xml`

- `line_editor.xml`

- `main_view.xml`

- `panel_avatar_tag.xml`

- `panel_classified_info.xml`

- `panel_classifieds_list_item.xml`

- `panel_clothing_list_item.xml`

- `panel_deletable_wearable_list_item.xml`

- `panel_edit_classified.xml`

- `panel_edit_pick.xml`

- `panel_edit_profile.xml`

- `panel_edit_wearable.xml`

- `panel_fs_login.xml`

- `panel_fs_nui_login.xml`

- `panel_generic_tip.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_hint.xml`

- `panel_landmark_info.xml`

- `panel_main_inventory.xml`

- `panel_media_settings_security.xml`

- `panel_my_profile.xml`

- `panel_navigation_bar.xml`

- `panel_nearby_chat.xml`

- `panel_nearby_media.xml`

- `panel_notes.xml`

- `panel_outfit_edit.xml`

- `panel_outfits_inventory.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_pick_info.xml`

- `panel_pick_list_item.xml`

- `panel_picks.xml`

- `panel_place_profile.xml`

- `panel_places.xml`

- `panel_preferences_custom_colors.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_stand_stop_flying.xml`

- `panel_status_bar.xml`

- `panel_sys_well_item.xml`

- `panel_teleport_history.xml`

- `panel_toolbar_view.xml`

- `sidepanel_appearance.xml`

- `sidepanel_inventory.xml`

- `sidepanel_task_info.xml`


## indra/newview/skins/starlightcui/xui/en/widgets/ (33 files)

- `accordion_tab.xml`

- `avatar_list_item.xml`

- `bodyparts_list_item.xml`

- `button.xml`

- `chiclet_im_p2p.xml`

- `clothing_list_item.xml`

- `combo_box.xml`

- `deletable_wearable_list_item.xml`

- `drop_down.xml`

- `dummy_clothing_list_item.xml`

- `floater.xml`

- `fs_chiclet_im_p2p.xml`

- `gesture_combo_list.xml`

- `icon.xml`

- `inventory_list_item.xml`

- `inventory_panel.xml`

- `line_editor.xml`

- `location_input.xml`

- `menu.xml`

- `menu_bar.xml`

- `panel.xml`

- `progress_bar.xml`

- `recent_inventory_panel.xml`

- `scroll_bar.xml`

- `scroll_container.xml`

- `simple_text_editor.xml`

- `slider_bar.xml`

- `split_button.xml`

- `tab_container.xml`

- `talk_button.xml`

- `toolbar.xml`

- `toolbar_vertical.xml`

- `worn_inventory_panel.xml`


## indra/newview/skins/starlightcui/xui/es/ (9 files)

- `floater_preferences.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_roles.xml`

- `panel_navigation_bar.xml`

- `panel_preferences_custom_colors.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlightcui/xui/it/ (10 files)

- `floater_preferences.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_navigation_bar.xml`

- `panel_preferences_custom_colors.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlightcui/xui/ja/ (11 files)

- `floater_preferences.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_main_inventory.xml`

- `panel_navigation_bar.xml`

- `panel_preferences_custom_colors.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlightcui/xui/pl/ (10 files)

- `floater_preferences.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_navigation_bar.xml`

- `panel_preferences_custom_colors.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlightcui/xui/pt/ (3 files)

- `floater_preferences.xml`

- `panel_preferences_custom_colors.xml`

- `panel_status_bar.xml`


## indra/newview/skins/starlightcui/xui/ru/ (1 files)

- `panel_status_bar.xml`


## indra/newview/skins/starlightcui/xui/zh/ (11 files)

- `floater_preferences.xml`

- `panel_group_general.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_land_money.xml`

- `panel_group_notices.xml`

- `panel_group_notify.xml`

- `panel_group_roles.xml`

- `panel_main_inventory.xml`

- `panel_navigation_bar.xml`

- `panel_preferences_custom_colors.xml`

- `panel_status_bar.xml`


## indra/newview/skins/vintage/ (3 files)

- `colors.xml`

- `settings.xml`

- `toolbars.xml`


## indra/newview/skins/vintage/textures/ (4 files)

- `Rounded_Rect_Top.png`

- `tearoff_pressed.tga`

- `tearoffbox.tga`

- `textures.xml`


## indra/newview/skins/vintage/textures/containers/ (6 files)

- `TabBottom_Left_Off.png`

- `TabBottom_Left_Selected.png`

- `TabLeft_Top_Off.png`

- `TabLeft_Top_Selected.png`

- `TabTop_Left_Off.png`

- `TabTop_Left_Selected.png`


## indra/newview/skins/vintage/textures/taskpanel/ (4 files)

- `Sidebar_Icon_Dock_Foreground.png`

- `Sidebar_Icon_Dock_Press.png`

- `Sidebar_Icon_Undock_Foreground.png`

- `Sidebar_Icon_Undock_Press.png`


## indra/newview/skins/vintage/textures/widgets/ (54 files)

- `Checkbox_Disabled.png`

- `Checkbox_Off.png`

- `Checkbox_On.png`

- `Checkbox_On_Disabled.png`

- `Checkbox_On_Press.png`

- `Checkbox_Press.png`

- `ComboButton_Off.png`

- `ComboButton_On.png`

- `ComboButton_Press.png`

- `ComboButton_Selected.png`

- `DropDown_Disabled.png`

- `DropDown_Off.png`

- `DropDown_On.png`

- `DropDown_Press.png`

- `ListItem_Over.png`

- `ListItem_Select.png`

- `ProgressBar.png`

- `ProgressTrack.png`

- `PushButton_Disabled.png`

- `PushButton_Off.png`

- `PushButton_Selected.png`

- `RadioButton_Disabled.png`

- `RadioButton_Off.png`

- `RadioButton_On.png`

- `RadioButton_On_Disabled.png`

- `RadioButton_On_Press.png`

- `RadioButton_Press.png`

- `ScrollArrow_Down.png`

- `ScrollArrow_Left.png`

- `ScrollArrow_Right.png`

- `ScrollArrow_Up.png`

- `ScrollThumb_Horiz.png`

- `ScrollThumb_Vert.png`

- `ScrollTrack_Horiz.png`

- `ScrollTrack_Vert.png`

- `SegmentedBtn_Middle_Disabled.png`

- `SegmentedBtn_Middle_Selected.png`

- `SegmentedBtn_Middle_Selected_Disabled.png`

- `SegmentedBtn_Middle_Selected_Press.png`

- `SliderThumb_Disabled.png`

- `SliderThumb_Off.png`

- `SliderTrack_Horiz.png`

- `SliderTrack_Vert.png`

- `SplitButtonLeft_Disabled.png`

- `SplitButtonLeft_Off.png`

- `SplitButtonLeft_Selected.png`

- `SplitButtonRight_Disabled.png`

- `SplitButtonRight_Off.png`

- `SplitButtonRight_Selected.png`

- `TextField_Active.png`

- `TextField_Disabled.png`

- `TextField_Off.png`

- `TextField_Search_Highlight.png`

- `Tooltip.png`


## indra/newview/skins/vintage/textures/windows/ (15 files)

- `Icon_Close_Foreground.png`

- `Icon_Close_Press.png`

- `Icon_Dock_Foreground.png`

- `Icon_Dock_Press.png`

- `Icon_Help_Foreground.png`

- `Icon_Help_Press.png`

- `Icon_Minimize_Foreground.png`

- `Icon_Minimize_Press.png`

- `Icon_Snooze_Foreground.png`

- `Icon_Snooze_Press.png`

- `Inspector_Hover.png`

- `Resize_Corner.png`

- `floater_background.tga`

- `floater_background_header.tga`

- `floater_script_background.tga`


## indra/newview/skins/vintage/xui/de/ (10 files)

- `floater_fs_voice_controls.xml`

- `panel_block_list_sidetray.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_radar.xml`

- `panel_group_notify.xml`

- `panel_main_inventory.xml`

- `panel_people.xml`

- `panel_toolbar_view.xml`

- `sidepanel_inventory.xml`


## indra/newview/skins/vintage/xui/en/ (52 files)

- `floater_fs_contacts.xml`

- `floater_fs_im_container.xml`

- `floater_fs_im_session.xml`

- `floater_fs_nearby_chat.xml`

- `floater_fs_voice_controls.xml`

- `floater_inventory_item_properties.xml`

- `floater_live_lsleditor.xml`

- `floater_map.xml`

- `floater_my_inventory.xml`

- `floater_people.xml`

- `floater_preferences.xml`

- `floater_script.xml`

- `floater_tools.xml`

- `panel_block_list_sidetray.xml`

- `panel_edit_eyes.xml`

- `panel_edit_gloves.xml`

- `panel_edit_hair.xml`

- `panel_edit_jacket.xml`

- `panel_edit_pants.xml`

- `panel_edit_shape.xml`

- `panel_edit_shirt.xml`

- `panel_edit_shoes.xml`

- `panel_edit_skin.xml`

- `panel_edit_skirt.xml`

- `panel_edit_socks.xml`

- `panel_edit_underpants.xml`

- `panel_edit_undershirt.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_radar.xml`

- `panel_group_info_sidetray.xml`

- `panel_group_list_item.xml`

- `panel_group_list_item_short.xml`

- `panel_group_notify.xml`

- `panel_instant_message.xml`

- `panel_main_inventory.xml`

- `panel_outfits_list.xml`

- `panel_outfits_wearing.xml`

- `panel_people.xml`

- `panel_profile_classified.xml`

- `panel_profile_classifieds.xml`

- `panel_profile_pick.xml`

- `panel_profile_picks.xml`

- `panel_profile_secondlife.xml`

- `panel_progress_mini.xml`

- `panel_script_ed.xml`

- `panel_script_ed_preproc.xml`

- `panel_side_tray_tab_caption.xml`

- `panel_toast.xml`

- `panel_toolbar_view.xml`

- `sidepanel_inventory.xml`

- `sidepanel_task_info.xml`


## indra/newview/skins/vintage/xui/en/widgets/ (16 files)

- `button.xml`

- `filter_editor.xml`

- `floater.xml`

- `flyout_button.xml`

- `inventory_panel.xml`

- `line_editor.xml`

- `location_input.xml`

- `progress_bar.xml`

- `recent_inventory_panel.xml`

- `search_editor.xml`

- `simple_text_editor.xml`

- `tab_container.xml`

- `text.xml`

- `tool_tip.xml`

- `toolbar.xml`

- `worn_inventory_panel.xml`


## indra/newview/skins/vintage/xui/es/ (9 files)

- `floater_people.xml`

- `panel_block_list_sidetray.xml`

- `panel_fs_radar.xml`

- `panel_group_notify.xml`

- `panel_main_inventory.xml`

- `panel_outfits_list.xml`

- `panel_people.xml`

- `panel_toolbar_view.xml`

- `sidepanel_inventory.xml`


## indra/newview/skins/vintage/xui/fr/ (12 files)

- `floater_fs_voice_controls.xml`

- `floater_people.xml`

- `panel_block_list_sidetray.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_radar.xml`

- `panel_group_notify.xml`

- `panel_main_inventory.xml`

- `panel_people.xml`

- `panel_profile_pick.xml`

- `panel_profile_secondlife.xml`

- `panel_toolbar_view.xml`

- `sidepanel_inventory.xml`


## indra/newview/skins/vintage/xui/it/ (12 files)

- `floater_fs_voice_controls.xml`

- `floater_people.xml`

- `panel_block_list_sidetray.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_radar.xml`

- `panel_group_notify.xml`

- `panel_main_inventory.xml`

- `panel_people.xml`

- `panel_profile_pick.xml`

- `panel_profile_secondlife.xml`

- `panel_toolbar_view.xml`

- `sidepanel_inventory.xml`


## indra/newview/skins/vintage/xui/ja/ (13 files)

- `floater_fs_voice_controls.xml`

- `floater_people.xml`

- `panel_block_list_sidetray.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_contacts_friends.xml`

- `panel_fs_radar.xml`

- `panel_group_notify.xml`

- `panel_main_inventory.xml`

- `panel_people.xml`

- `panel_profile_pick.xml`

- `panel_profile_secondlife.xml`

- `panel_toolbar_view.xml`

- `sidepanel_inventory.xml`


## indra/newview/skins/vintage/xui/pl/ (12 files)

- `floater_fs_voice_controls.xml`

- `floater_people.xml`

- `panel_block_list_sidetray.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_radar.xml`

- `panel_group_notify.xml`

- `panel_main_inventory.xml`

- `panel_people.xml`

- `panel_profile_pick.xml`

- `panel_profile_secondlife.xml`

- `panel_toolbar_view.xml`

- `sidepanel_inventory.xml`


## indra/newview/skins/vintage/xui/pt/ (9 files)

- `floater_fs_voice_controls.xml`

- `panel_block_list_sidetray.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_radar.xml`

- `panel_group_notify.xml`

- `panel_main_inventory.xml`

- `panel_people.xml`

- `panel_toolbar_view.xml`

- `sidepanel_inventory.xml`


## indra/newview/skins/vintage/xui/ru/ (12 files)

- `floater_fs_voice_controls.xml`

- `floater_people.xml`

- `panel_block_list_sidetray.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_radar.xml`

- `panel_group_notify.xml`

- `panel_main_inventory.xml`

- `panel_people.xml`

- `panel_profile_pick.xml`

- `panel_profile_secondlife.xml`

- `panel_toolbar_view.xml`

- `sidepanel_inventory.xml`


## indra/newview/skins/vintage/xui/zh/ (12 files)

- `floater_fs_voice_controls.xml`

- `floater_people.xml`

- `panel_block_list_sidetray.xml`

- `panel_fs_block_list_sidetray.xml`

- `panel_fs_radar.xml`

- `panel_group_notify.xml`

- `panel_main_inventory.xml`

- `panel_people.xml`

- `panel_profile_pick.xml`

- `panel_profile_secondlife.xml`

- `panel_toolbar_view.xml`

- `sidepanel_inventory.xml`


## indra/newview/tests/ (35 files)

- `cppfeatures_test.cpp`

- `fsgridhandler_test.cpp`

- `fslslpreprocpath_test.cpp`

- `fsslurl_test.cpp`

- `llagentaccess_test.cpp`

- `llchatservicehistorycore_test.cpp`

- `llconversationlog_test.cpp`

- `lldateutil_test.cpp`

- `lldir_stub.cpp`

- `llgamecontrol_stub.cpp`

- `llhttpretrypolicy_test.cpp`

- `lllogininstance_test.cpp`

- `llmediadataclient_test.cpp`

- `llremoteparcelrequest_test.cpp`

- `llscripteditorws_test.cpp`

- `llsecapi_test.cpp`

- `llsechandler_basic_test.cpp`

- `llslurl_test.cpp`

- `lltextureinfo_test.cpp`

- `lltextureinfodetails_test.cpp`

- `lltexturematrix_test.cpp`

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

- `llxmlrpclistener_test.cpp`

- `opensim_test_support.cpp`

- `opensim_test_support.h`

- `test_llxmlrpc_peer.py`


## indra/newview/tr.lproj/ (1 files)

- `language.txt`


## indra/newview/uk.lproj/ (1 files)

- `language.txt`


## indra/newview/vmp_icons/ (4 files)

- `SL_Logo.gif`

- `SL_Logo.png`

- `head-sl-logo.gif`

- `head-sl-logo.png`


## indra/newview/zh-Hans.lproj/ (1 files)

- `language.txt`


## indra/test/ (16 files)

- `CMakeLists.txt`

- `catch_and_store_what_in.h`

- `chained_callback.h`

- `debug.h`

- `llsdtraits.h`

- `lltestapp.h`

- `lltut.cpp`

- `lltut.h`

- `namedtempfile.h`

- `nonasciipaths.h`

- `print.h`

- `setenv.h`

- `sync.h`

- `test.cpp`

- `test.h`

- `test_llmanifest.py`


## indra/tools/manifests/ (2 files)

- `compatibility.manifest`

- `legacy.manifest`


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


## indra/win_crash_logger/ (3 files)

- `firestorm_icon.ico`

- `llcrashlookupwindows.cpp`

- `llcrashlookupwindows.h`


## scripts/ (5 files)

- `configure_firestorm.sh`

- `md5check.py`

- `packages-formatter.py`

- `setup-path.py`

- `template_verifier.py`


## scripts/code_tools/ (4 files)

- `fix_whitespace.py`

- `fix_xml_indentations.py`

- `modified-strings.sh`

- `modified_strings.py`


## scripts/content_tools/ (4 files)

- `anim_tool.py`

- `arche_tool.py`

- `dae_tool.py`

- `skel_tool.py`


## scripts/messages/ (2 files)

- `message_template.msg`

- `message_template.msg.sha1`


## scripts/metrics/ (3 files)

- `slp_conv.py`

- `viewer_asset_logs.py`

- `viewerstats.py`


## scripts/perf/ (5 files)

- `logsdir.py`

- `perfbot_run.py`

- `profile_cmp.py`

- `profile_csv.py`

- `profile_pretty.py`


## scripts/templates/ (2 files)

- `template-cpp.cpp`

- `template-h.h`


## scripts/testing/lsl/ (4 files)

- `axon_test_region_driver.lsl`

- `cycle_object_animations.lsl`

- `cycle_object_animations_v2.lsl`

- `move_in_circle_using_llSetRegionPos.lsl`
