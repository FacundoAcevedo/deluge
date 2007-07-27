<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE glade-interface SYSTEM "glade-2.0.dtd">
<!--*- mode: xml -*-->
<glade-interface>
  <widget class="GtkWindow" id="main_window">
    <property name="title">Deluge</property>
    <signal name="destroy" handler="quit"/>
    <signal name="destroy_event" handler="quit"/>
    <signal name="delete_event" handler="delete"/>
    <child>
      <widget class="GtkTable" id="layout_table">
        <property name="visible">True</property>
        <property name="n_rows">4</property>
        <property name="n_columns">3</property>
        <child>
          <widget class="GtkToolbar" id="tb_left">
            <property name="visible">True</property>
            <property name="show_arrow">False</property>
            <child>
              <widget class="GtkToolButton" id="toolbutton_add">
                <property name="visible">True</property>
                <property name="tooltip" translatable="yes">Add Torrent</property>
                <property name="label" translatable="yes">Add</property>
                <property name="use_underline">True</property>
                <property name="stock_id">gtk-add</property>
                <signal name="clicked" handler="add_torrent"/>
              </widget>
              <packing>
                <property name="expand">False</property>
              </packing>
            </child>
            <child>
              <widget class="GtkToolButton" id="toolbutton_remove">
                <property name="visible">True</property>
                <property name="sensitive">False</property>
                <property name="tooltip" translatable="yes">Remove Torrent</property>
                <property name="label" translatable="yes">Remove</property>
                <property name="use_underline">True</property>
                <property name="stock_id">gtk-remove</property>
                <signal name="clicked" handler="remove_torrent"/>
              </widget>
              <packing>
                <property name="expand">False</property>
              </packing>
            </child>
            <child>
              <widget class="GtkToolButton" id="toolbutton3">
                <property name="visible">True</property>
                <property name="tooltip" translatable="yes">Clear Finished Torrents</property>
                <property name="label" translatable="yes">Clear</property>
                <property name="use_underline">True</property>
                <property name="stock_id">gtk-clear</property>
                <signal name="clicked" handler="clear_finished"/>
              </widget>
              <packing>
                <property name="expand">False</property>
              </packing>
            </child>
            <child>
              <widget class="GtkSeparatorToolItem" id="separatortoolitem1">
                <property name="visible">True</property>
              </widget>
              <packing>
                <property name="expand">False</property>
                <property name="homogeneous">False</property>
              </packing>
            </child>
            <child>
              <widget class="GtkToolButton" id="toolbutton_pause">
                <property name="visible">True</property>
                <property name="sensitive">False</property>
                <property name="tooltip" translatable="yes">Start or Pause torrent</property>
                <property name="label" translatable="yes">Start</property>
                <property name="use_underline">True</property>
                <property name="stock_id">gtk-media-play</property>
                <signal name="clicked" handler="start_pause"/>
              </widget>
              <packing>
                <property name="expand">False</property>
              </packing>
            </child>
            <child>
              <widget class="GtkToolButton" id="toolbutton_up">
                <property name="visible">True</property>
                <property name="sensitive">False</property>
                <property name="tooltip" translatable="yes">Queue Torrent Up</property>
                <property name="label" translatable="yes">Up</property>
                <property name="use_underline">True</property>
                <property name="stock_id">gtk-go-up</property>
                <signal name="clicked" handler="queue_up"/>
              </widget>
              <packing>
                <property name="expand">False</property>
              </packing>
            </child>
            <child>
              <widget class="GtkToolButton" id="toolbutton_down">
                <property name="visible">True</property>
                <property name="sensitive">False</property>
                <property name="tooltip" translatable="yes">Queue Torrent Down</property>
                <property name="label" translatable="yes">Down</property>
                <property name="use_underline">True</property>
                <property name="stock_id">gtk-go-down</property>
                <signal name="clicked" handler="queue_down"/>
              </widget>
              <packing>
                <property name="expand">False</property>
              </packing>
            </child>
            <child>
              <widget class="GtkSeparatorToolItem" id="separatortoolitem2">
                <property name="visible">True</property>
              </widget>
              <packing>
                <property name="expand">False</property>
                <property name="homogeneous">False</property>
              </packing>
            </child>
            <child>
              <widget class="GtkToolButton" id="toolbutton1">
                <property name="visible">True</property>
                <property name="tooltip" translatable="yes">Change Deluge preferences</property>
                <property name="label" translatable="yes">Preferences</property>
                <property name="use_underline">True</property>
                <property name="stock_id">gtk-preferences</property>
                <signal name="clicked" handler="pref_clicked"/>
              </widget>
              <packing>
                <property name="expand">False</property>
              </packing>
            </child>
            <child>
              <widget class="GtkToolButton" id="toolbutton2">
                <property name="visible">True</property>
                <property name="tooltip" translatable="yes">Open the plugins dialog</property>
                <property name="label" translatable="yes">Plugins</property>
                <property name="use_underline">True</property>
                <property name="stock_id">gtk-disconnect</property>
                <signal name="clicked" handler="plugins_clicked"/>
              </widget>
              <packing>
                <property name="expand">False</property>
              </packing>
            </child>
          </widget>
          <packing>
            <property name="top_attach">1</property>
            <property name="bottom_attach">2</property>
            <property name="y_options">GTK_FILL</property>
          </packing>
        </child>
        <child>
          <widget class="GtkToolbar" id="tb_middle">
            <property name="visible">True</property>
            <property name="show_arrow">False</property>
          </widget>
          <packing>
            <property name="left_attach">1</property>
            <property name="right_attach">2</property>
            <property name="top_attach">1</property>
            <property name="bottom_attach">2</property>
            <property name="x_options">GTK_FILL</property>
            <property name="y_options">GTK_FILL</property>
          </packing>
        </child>
        <child>
          <widget class="GtkToolbar" id="tb_right">
            <property name="visible">True</property>
            <property name="show_arrow">False</property>
          </widget>
          <packing>
            <property name="left_attach">2</property>
            <property name="right_attach">3</property>
            <property name="top_attach">1</property>
            <property name="bottom_attach">2</property>
            <property name="x_options"></property>
            <property name="y_options">GTK_FILL</property>
          </packing>
        </child>
        <child>
          <widget class="GtkMenuBar" id="menubar">
            <property name="visible">True</property>
            <child>
              <widget class="GtkMenuItem" id="menu_file">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_File</property>
                <property name="use_underline">True</property>
                <child>
                  <widget class="GtkMenu" id="menuitem1_menu">
                    <child>
                      <widget class="GtkImageMenuItem" id="menuitem1">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">_Add Torrent</property>
                        <property name="use_underline">True</property>
                        <signal name="activate" handler="add_torrent"/>
                        <child internal-child="image">
                          <widget class="GtkImage" id="menu-item-image1">
                            <property name="visible">True</property>
                            <property name="stock">gtk-add</property>
                            <property name="icon_size">1</property>
                          </widget>
                        </child>
                      </widget>
                    </child>
                    <child>
                      <widget class="GtkMenuItem" id="menuitem2">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">Add _URL</property>
                        <property name="use_underline">True</property>
                        <signal name="activate" handler="add_torrent_url"/>
                      </widget>
                    </child>
                    <child>
                      <widget class="GtkImageMenuItem" id="menuitem5">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">_Clear Completed</property>
                        <property name="use_underline">True</property>
                        <signal name="activate" handler="clear_finished"/>
                        <child internal-child="image">
                          <widget class="GtkImage" id="menu-item-image4">
                            <property name="visible">True</property>
                            <property name="stock">gtk-clear</property>
                            <property name="icon_size">1</property>
                          </widget>
                        </child>
                      </widget>
                    </child>
                    <child>
                      <widget class="GtkSeparatorMenuItem" id="separatormenuitem1">
                        <property name="visible">True</property>
                      </widget>
                    </child>
                    <child>
                      <widget class="GtkImageMenuItem" id="imagemenuitem1">
                        <property name="visible">True</property>
                        <property name="label">gtk-quit</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <signal name="activate" handler="menu_quit"/>
                      </widget>
                    </child>
                  </widget>
                </child>
              </widget>
            </child>
            <child>
              <widget class="GtkMenuItem" id="menu_edit">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_Edit</property>
                <property name="use_underline">True</property>
                <child>
                  <widget class="GtkMenu" id="menu2">
                    <property name="visible">True</property>
                    <child>
                      <widget class="GtkImageMenuItem" id="menuitem9">
                        <property name="visible">True</property>
                        <property name="label">gtk-preferences</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <signal name="activate" handler="pref_clicked"/>
                      </widget>
                    </child>
                    <child>
                      <widget class="GtkImageMenuItem" id="plugins1">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">Pl_ugins</property>
                        <property name="use_underline">True</property>
                        <signal name="activate" handler="plugins_clicked"/>
                        <child internal-child="image">
                          <widget class="GtkImage" id="menu-item-image3">
                            <property name="visible">True</property>
                            <property name="stock">gtk-disconnect</property>
                            <property name="icon_size">1</property>
                          </widget>
                        </child>
                      </widget>
                    </child>
                  </widget>
                </child>
              </widget>
            </child>
            <child>
              <widget class="GtkMenuItem" id="menu_torrent">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_Torrent</property>
                <property name="use_underline">True</property>
              </widget>
            </child>
            <child>
              <widget class="GtkMenuItem" id="menu_view">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_View</property>
                <property name="use_underline">True</property>
                <child>
                  <widget class="GtkMenu" id="menu1">
                    <property name="visible">True</property>
                    <child>
                      <widget class="GtkCheckMenuItem" id="chk_toolbar">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">_Toolbar</property>
                        <property name="use_underline">True</property>
                        <property name="active">True</property>
                        <signal name="toggled" handler="toolbar_toggle"/>
                      </widget>
                    </child>
                    <child>
                      <widget class="GtkCheckMenuItem" id="chk_infopane">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">_Details</property>
                        <property name="use_underline">True</property>
                        <property name="active">True</property>
                        <signal name="toggled" handler="infopane_toggle"/>
                      </widget>
                    </child>
                    <child>
                      <widget class="GtkMenuItem" id="menu_column">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">Columns</property>
                        <property name="use_underline">True</property>
                        <child>
                          <widget class="GtkMenu" id="menu3">
                            <property name="visible">True</property>
                            <child>
                              <widget class="GtkCheckMenuItem" id="chk_size">
                                <property name="visible">True</property>
                                <property name="label" translatable="yes">Size</property>
                                <property name="use_underline">True</property>
                                <property name="active">True</property>
                                <signal name="toggled" handler="size_toggle"/>
                              </widget>
                            </child>
                            <child>
                              <widget class="GtkCheckMenuItem" id="chk_status">
                                <property name="visible">True</property>
                                <property name="label" translatable="yes">Status</property>
                                <property name="use_underline">True</property>
                                <property name="active">True</property>
                                <signal name="toggled" handler="status_toggle"/>
                              </widget>
                            </child>
                            <child>
                              <widget class="GtkCheckMenuItem" id="chk_seed">
                                <property name="visible">True</property>
                                <property name="label" translatable="yes">Seeders</property>
                                <property name="use_underline">True</property>
                                <property name="active">True</property>
                                <signal name="toggled" handler="seeders_toggle"/>
                              </widget>
                            </child>
                            <child>
                              <widget class="GtkCheckMenuItem" id="chk_peer">
                                <property name="visible">True</property>
                                <property name="label" translatable="yes">Peers</property>
                                <property name="use_underline">True</property>
                                <property name="active">True</property>
                                <signal name="toggled" handler="peers_toggle"/>
                              </widget>
                            </child>
                            <child>
                              <widget class="GtkCheckMenuItem" id="chk_download">
                                <property name="visible">True</property>
                                <property name="label" translatable="yes">Down Speed</property>
                                <property name="use_underline">True</property>
                                <property name="active">True</property>
                                <signal name="toggled" handler="dl_toggle"/>
                              </widget>
                            </child>
                            <child>
                              <widget class="GtkCheckMenuItem" id="chk_upload">
                                <property name="visible">True</property>
                                <property name="label" translatable="yes">Up Speed</property>
                                <property name="use_underline">True</property>
                                <property name="active">True</property>
                                <signal name="toggled" handler="ul_toggle"/>
                              </widget>
                            </child>
                            <child>
                              <widget class="GtkCheckMenuItem" id="chk_eta">
                                <property name="visible">True</property>
                                <property name="label" translatable="yes">Time Remaining</property>
                                <property name="use_underline">True</property>
                                <property name="active">True</property>
                                <signal name="toggled" handler="eta_toggle"/>
                              </widget>
                            </child>
                            <child>
                              <widget class="GtkCheckMenuItem" id="chk_availability">
                                <property name="visible">True</property>
                                <property name="label" translatable="yes">Availability</property>
                                <property name="use_underline">True</property>
                                <property name="active">True</property>
                                <signal name="toggled" handler="availability_toggle"/>
                              </widget>
                            </child>
                            <child>
                              <widget class="GtkCheckMenuItem" id="chk_ratio">
                                <property name="visible">True</property>
                                <property name="label" translatable="yes">Share Ratio</property>
                                <property name="use_underline">True</property>
                                <property name="active">True</property>
                                <signal name="toggled" handler="share_toggle"/>
                              </widget>
                            </child>
                          </widget>
                        </child>
                      </widget>
                    </child>
                  </widget>
                </child>
              </widget>
            </child>
            <child>
              <widget class="GtkMenuItem" id="menu_help">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_Help</property>
                <property name="use_underline">True</property>
                <child>
                  <widget class="GtkMenu" id="menuitem2_menu">
                    <child>
                      <widget class="GtkImageMenuItem" id="menuitem3">
                        <property name="visible">True</property>
                        <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                        <property name="tooltip" translatable="yes">Help translate this application</property>
                        <property name="label" translatable="yes">_Translate This Application...</property>
                        <property name="use_underline">True</property>
                        <signal name="activate" handler="launchpad"/>
                        <child internal-child="image">
                          <widget class="GtkImage" id="menu-item-image5">
                            <property name="visible">True</property>
                            <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                            <property name="stock">gtk-edit</property>
                            <property name="icon_size">1</property>
                          </widget>
                        </child>
                      </widget>
                    </child>
                    <child>
                      <widget class="GtkSeparatorMenuItem" id="separatormenuitem2">
                        <property name="visible">True</property>
                        <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                      </widget>
                    </child>
                    <child>
                      <widget class="GtkImageMenuItem" id="menuitem4">
                        <property name="visible">True</property>
                        <property name="label">gtk-about</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <signal name="activate" handler="show_about_dialog"/>
                      </widget>
                    </child>
                  </widget>
                </child>
              </widget>
            </child>
          </widget>
          <packing>
            <property name="right_attach">3</property>
            <property name="y_options"></property>
          </packing>
        </child>
        <child>
          <widget class="GtkStatusbar" id="statusbar">
            <property name="visible">True</property>
          </widget>
          <packing>
            <property name="right_attach">3</property>
            <property name="top_attach">3</property>
            <property name="bottom_attach">4</property>
            <property name="y_options"></property>
          </packing>
        </child>
        <child>
          <widget class="GtkVPaned" id="vpaned1">
            <property name="visible">True</property>
            <child>
              <widget class="GtkAlignment" id="alignment5">
                <property name="visible">True</property>
                <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                <child>
                  <widget class="GtkScrolledWindow" id="scrolledwindow1">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="hscrollbar_policy">GTK_POLICY_AUTOMATIC</property>
                    <property name="vscrollbar_policy">GTK_POLICY_AUTOMATIC</property>
                    <child>
                      <widget class="GtkTreeView" id="torrent_view">
                        <property name="visible">True</property>
                        <property name="headers_clickable">True</property>
                        <property name="reorderable">True</property>
                        <property name="rules_hint">True</property>
                        <property name="enable_search">False</property>
                      </widget>
                    </child>
                  </widget>
                </child>
              </widget>
              <packing>
                <property name="resize">True</property>
                <property name="shrink">False</property>
              </packing>
            </child>
            <child>
              <widget class="GtkAlignment" id="alignment1">
                <property name="visible">True</property>
                <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                <child>
                  <widget class="GtkNotebook" id="torrent_info">
                    <property name="visible">True</property>
                    <property name="show_border">False</property>
                    <property name="homogeneous">True</property>
                    <child>
                      <widget class="GtkScrolledWindow" id="scrolledwindow2">
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                        <property name="hscrollbar_policy">GTK_POLICY_AUTOMATIC</property>
                        <property name="vscrollbar_policy">GTK_POLICY_NEVER</property>
                        <child>
                          <widget class="GtkViewport" id="viewport1">
                            <property name="visible">True</property>
                            <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                            <property name="resize_mode">GTK_RESIZE_QUEUE</property>
                            <property name="shadow_type">GTK_SHADOW_NONE</property>
                            <child>
                              <widget class="GtkTable" id="table1">
                                <property name="visible">True</property>
                                <property name="n_rows">1</property>
                                <property name="n_columns">2</property>
                                <property name="column_spacing">10</property>
                                <child>
                                  <widget class="GtkFrame" id="frame2">
                                    <property name="visible">True</property>
                                    <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                    <property name="label_xalign">0</property>
                                    <child>
                                      <widget class="GtkAlignment" id="alignment12">
                                        <property name="visible">True</property>
                                        <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                        <property name="top_padding">10</property>
                                        <property name="bottom_padding">10</property>
                                        <property name="left_padding">15</property>
                                        <property name="right_padding">15</property>
                                        <child>
                                          <widget class="GtkTable" id="table3">
                                            <property name="visible">True</property>
                                            <property name="n_rows">5</property>
                                            <property name="n_columns">2</property>
                                            <property name="row_spacing">2</property>
                                            <child>
                                              <widget class="GtkLabel" id="summary_next_announce">
                                                <property name="visible">True</property>
                                                <property name="xalign">0</property>
                                              </widget>
                                              <packing>
                                                <property name="left_attach">1</property>
                                                <property name="right_attach">2</property>
                                                <property name="top_attach">4</property>
                                                <property name="bottom_attach">5</property>
                                                <property name="y_options"></property>
                                              </packing>
                                            </child>
                                            <child>
                                              <widget class="GtkLabel" id="summary_tracker_status">
                                                <property name="visible">True</property>
                                                <property name="xalign">0</property>
                                              </widget>
                                              <packing>
                                                <property name="left_attach">1</property>
                                                <property name="right_attach">2</property>
                                                <property name="top_attach">3</property>
                                                <property name="bottom_attach">4</property>
                                                <property name="y_options"></property>
                                              </packing>
                                            </child>
                                            <child>
                                              <widget class="GtkLabel" id="summary_tracker">
                                                <property name="visible">True</property>
                                                <property name="xalign">0</property>
                                                <property name="wrap">True</property>
                                                <property name="wrap_mode">PANGO_WRAP_WORD_CHAR</property>
                                              </widget>
                                              <packing>
                                                <property name="left_attach">1</property>
                                                <property name="right_attach">2</property>
                                                <property name="top_attach">2</property>
                                                <property name="bottom_attach">3</property>
                                                <property name="y_options"></property>
                                              </packing>
                                            </child>
                                            <child>
                                              <widget class="GtkAlignment" id="alignment13">
                                                <property name="visible">True</property>
                                                <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                                <property name="right_padding">5</property>
                                                <child>
                                                  <widget class="GtkLabel" id="label10">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                    <property name="yalign">0</property>
                                                    <property name="ypad">1</property>
                                                    <property name="label" translatable="yes">&lt;b&gt;Name:&lt;/b&gt;</property>
                                                    <property name="use_markup">True</property>
                                                  </widget>
                                                </child>
                                              </widget>
                                              <packing>
                                                <property name="x_options">GTK_FILL</property>
                                              </packing>
                                            </child>
                                            <child>
                                              <widget class="GtkAlignment" id="alignment20">
                                                <property name="visible">True</property>
                                                <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                                <property name="right_padding">5</property>
                                                <child>
                                                  <widget class="GtkLabel" id="label23">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                    <property name="ypad">1</property>
                                                    <property name="label" translatable="yes">&lt;b&gt;Next Announce:&lt;/b&gt;</property>
                                                    <property name="use_markup">True</property>
                                                  </widget>
                                                </child>
                                              </widget>
                                              <packing>
                                                <property name="top_attach">4</property>
                                                <property name="bottom_attach">5</property>
                                                <property name="x_options">GTK_FILL</property>
                                              </packing>
                                            </child>
                                            <child>
                                              <widget class="GtkAlignment" id="alignment17">
                                                <property name="visible">True</property>
                                                <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                                <property name="right_padding">5</property>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment19">
                                                    <property name="visible">True</property>
                                                    <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label21">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="ypad">1</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;Tracker Status:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                </child>
                                              </widget>
                                              <packing>
                                                <property name="top_attach">3</property>
                                                <property name="bottom_attach">4</property>
                                                <property name="x_options">GTK_FILL</property>
                                              </packing>
                                            </child>
                                            <child>
                                              <widget class="GtkAlignment" id="alignment15">
                                                <property name="visible">True</property>
                                                <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                                <property name="right_padding">5</property>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment18">
                                                    <property name="visible">True</property>
                                                    <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label15">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="ypad">1</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;Tracker:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                </child>
                                              </widget>
                                              <packing>
                                                <property name="top_attach">2</property>
                                                <property name="bottom_attach">3</property>
                                                <property name="x_options">GTK_FILL</property>
                                              </packing>
                                            </child>
                                            <child>
                                              <widget class="GtkAlignment" id="alignment14">
                                                <property name="visible">True</property>
                                                <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                                <property name="right_padding">5</property>
                                                <child>
                                                  <widget class="GtkLabel" id="label11">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                    <property name="ypad">1</property>
                                                    <property name="label" translatable="yes">&lt;b&gt;Total Size:&lt;/b&gt;</property>
                                                    <property name="use_markup">True</property>
                                                  </widget>
                                                </child>
                                              </widget>
                                              <packing>
                                                <property name="top_attach">1</property>
                                                <property name="bottom_attach">2</property>
                                                <property name="x_options">GTK_FILL</property>
                                              </packing>
                                            </child>
                                            <child>
                                              <widget class="GtkLabel" id="summary_name">
                                                <property name="visible">True</property>
                                                <property name="xalign">0</property>
                                                <property name="wrap">True</property>
                                                <property name="wrap_mode">PANGO_WRAP_WORD_CHAR</property>
                                              </widget>
                                              <packing>
                                                <property name="left_attach">1</property>
                                                <property name="right_attach">2</property>
                                                <property name="y_options"></property>
                                              </packing>
                                            </child>
                                            <child>
                                              <widget class="GtkLabel" id="summary_total_size">
                                                <property name="visible">True</property>
                                                <property name="xalign">0</property>
                                              </widget>
                                              <packing>
                                                <property name="left_attach">1</property>
                                                <property name="right_attach">2</property>
                                                <property name="top_attach">1</property>
                                                <property name="bottom_attach">2</property>
                                                <property name="y_options"></property>
                                              </packing>
                                            </child>
                                          </widget>
                                        </child>
                                      </widget>
                                    </child>
                                    <child>
                                      <widget class="GtkLabel" id="label16">
                                        <property name="visible">True</property>
                                        <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                        <property name="label" translatable="yes">&lt;b&gt;Torrent Info&lt;/b&gt;</property>
                                        <property name="use_markup">True</property>
                                      </widget>
                                      <packing>
                                        <property name="type">label_item</property>
                                      </packing>
                                    </child>
                                  </widget>
                                  <packing>
                                    <property name="left_attach">1</property>
                                    <property name="right_attach">2</property>
                                    <property name="y_options">GTK_FILL</property>
                                  </packing>
                                </child>
                                <child>
                                  <widget class="GtkFrame" id="frame1">
                                    <property name="visible">True</property>
                                    <property name="label_xalign">0</property>
                                    <child>
                                      <widget class="GtkAlignment" id="alignment2">
                                        <property name="visible">True</property>
                                        <property name="top_padding">10</property>
                                        <property name="bottom_padding">10</property>
                                        <property name="left_padding">15</property>
                                        <property name="right_padding">15</property>
                                        <child>
                                          <widget class="GtkVBox" id="vbox1">
                                            <property name="visible">True</property>
                                            <property name="spacing">5</property>
                                            <child>
                                              <widget class="GtkProgressBar" id="progressbar">
                                                <property name="visible">True</property>
                                                <property name="pulse_step">0.10000000149</property>
                                              </widget>
                                              <packing>
                                                <property name="expand">False</property>
                                                <property name="fill">False</property>
                                              </packing>
                                            </child>
                                            <child>
                                              <widget class="GtkTable" id="table2">
                                                <property name="visible">True</property>
                                                <property name="n_rows">5</property>
                                                <property name="n_columns">4</property>
                                                <property name="row_spacing">5</property>
                                                <child>
                                                  <widget class="GtkLabel" id="summary_availability">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                    <property name="wrap">True</property>
                                                    <property name="wrap_mode">PANGO_WRAP_WORD_CHAR</property>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">3</property>
                                                    <property name="right_attach">4</property>
                                                    <property name="top_attach">4</property>
                                                    <property name="bottom_attach">5</property>
                                                    <property name="y_options"></property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment21">
                                                    <property name="visible">True</property>
                                                    <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                                    <property name="left_padding">15</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label14">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="ypad">1</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;Availability:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">2</property>
                                                    <property name="right_attach">3</property>
                                                    <property name="top_attach">4</property>
                                                    <property name="bottom_attach">5</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment16">
                                                    <property name="visible">True</property>
                                                    <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="summary_pieces">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">1</property>
                                                    <property name="right_attach">2</property>
                                                    <property name="top_attach">4</property>
                                                    <property name="bottom_attach">5</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkLabel" id="label12">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                    <property name="ypad">1</property>
                                                    <property name="label" translatable="yes">&lt;b&gt;Pieces:&lt;/b&gt;</property>
                                                    <property name="use_markup">True</property>
                                                  </widget>
                                                  <packing>
                                                    <property name="top_attach">4</property>
                                                    <property name="bottom_attach">5</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment11">
                                                    <property name="visible">True</property>
                                                    <property name="left_padding">15</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label8">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;ETA:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">2</property>
                                                    <property name="right_attach">3</property>
                                                    <property name="top_attach">3</property>
                                                    <property name="bottom_attach">4</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment10">
                                                    <property name="visible">True</property>
                                                    <property name="left_padding">15</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label7">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;Peers:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">2</property>
                                                    <property name="right_attach">3</property>
                                                    <property name="top_attach">2</property>
                                                    <property name="bottom_attach">3</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment9">
                                                    <property name="visible">True</property>
                                                    <property name="left_padding">15</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label6">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;Speed:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">2</property>
                                                    <property name="right_attach">3</property>
                                                    <property name="top_attach">1</property>
                                                    <property name="bottom_attach">2</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment8">
                                                    <property name="visible">True</property>
                                                    <property name="left_padding">15</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label5">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;Speed:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">2</property>
                                                    <property name="right_attach">3</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment7">
                                                    <property name="visible">True</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label4">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;Share Ratio:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                  <packing>
                                                    <property name="top_attach">3</property>
                                                    <property name="bottom_attach">4</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment6">
                                                    <property name="visible">True</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label3">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;Seeders:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                  <packing>
                                                    <property name="top_attach">2</property>
                                                    <property name="bottom_attach">3</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment4">
                                                    <property name="visible">True</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label2">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;Uploaded:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                  <packing>
                                                    <property name="top_attach">1</property>
                                                    <property name="bottom_attach">2</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkAlignment" id="alignment3">
                                                    <property name="visible">True</property>
                                                    <property name="right_padding">5</property>
                                                    <child>
                                                      <widget class="GtkLabel" id="label1">
                                                        <property name="visible">True</property>
                                                        <property name="xalign">0</property>
                                                        <property name="label" translatable="yes">&lt;b&gt;Downloaded:&lt;/b&gt;</property>
                                                        <property name="use_markup">True</property>
                                                      </widget>
                                                    </child>
                                                  </widget>
                                                </child>
                                                <child>
                                                  <widget class="GtkLabel" id="summary_eta">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">3</property>
                                                    <property name="right_attach">4</property>
                                                    <property name="top_attach">3</property>
                                                    <property name="bottom_attach">4</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkLabel" id="summary_share_ratio">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">1</property>
                                                    <property name="right_attach">2</property>
                                                    <property name="top_attach">3</property>
                                                    <property name="bottom_attach">4</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkLabel" id="summary_peers">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">3</property>
                                                    <property name="right_attach">4</property>
                                                    <property name="top_attach">2</property>
                                                    <property name="bottom_attach">3</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkLabel" id="summary_seeders">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">1</property>
                                                    <property name="right_attach">2</property>
                                                    <property name="top_attach">2</property>
                                                    <property name="bottom_attach">3</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkLabel" id="summary_upload_speed">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">3</property>
                                                    <property name="right_attach">4</property>
                                                    <property name="top_attach">1</property>
                                                    <property name="bottom_attach">2</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkLabel" id="summary_total_uploaded">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">1</property>
                                                    <property name="right_attach">2</property>
                                                    <property name="top_attach">1</property>
                                                    <property name="bottom_attach">2</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkLabel" id="summary_download_speed">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">3</property>
                                                    <property name="right_attach">4</property>
                                                  </packing>
                                                </child>
                                                <child>
                                                  <widget class="GtkLabel" id="summary_total_downloaded">
                                                    <property name="visible">True</property>
                                                    <property name="xalign">0</property>
                                                  </widget>
                                                  <packing>
                                                    <property name="left_attach">1</property>
                                                    <property name="right_attach">2</property>
                                                  </packing>
                                                </child>
                                              </widget>
                                              <packing>
                                                <property name="expand">False</property>
                                                <property name="position">1</property>
                                              </packing>
                                            </child>
                                          </widget>
                                        </child>
                                      </widget>
                                    </child>
                                    <child>
                                      <widget class="GtkLabel" id="label9">
                                        <property name="visible">True</property>
                                        <property name="events">GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK</property>
                                        <property name="label" translatable="yes">&lt;b&gt;Statistics&lt;/b&gt;</property>
                                        <property name="use_markup">True</property>
                                      </widget>
                                      <packing>
                                        <property name="type">label_item</property>
                                      </packing>
                                    </child>
                                  </widget>
                                  <packing>
                                    <property name="x_options"></property>
                                    <property name="y_options">GTK_FILL</property>
                                  </packing>
                                </child>
                              </widget>
                            </child>
                          </widget>
                        </child>
                      </widget>
                      <packing>
                        <property name="tab_expand">False</property>
                      </packing>
                    </child>
                    <child>
                      <widget class="GtkLabel" id="label17">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">Details</property>
                      </widget>
                      <packing>
                        <property name="type">tab</property>
                        <property name="tab_expand">False</property>
                        <property name="tab_fill">False</property>
                      </packing>
                    </child>
                    <child>
                      <widget class="GtkScrolledWindow" id="scrolledwindow3">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="hscrollbar_policy">GTK_POLICY_AUTOMATIC</property>
                        <property name="vscrollbar_policy">GTK_POLICY_AUTOMATIC</property>
                        <child>
                          <widget class="GtkTreeView" id="peer_view">
                            <property name="visible">True</property>
                          </widget>
                        </child>
                      </widget>
                      <packing>
                        <property name="position">1</property>
                        <property name="tab_expand">False</property>
                      </packing>
                    </child>
                    <child>
                      <widget class="GtkLabel" id="label18">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">Peers</property>
                      </widget>
                      <packing>
                        <property name="type">tab</property>
                        <property name="position">1</property>
                        <property name="tab_expand">False</property>
                        <property name="tab_fill">False</property>
                      </packing>
                    </child>
                    <child>
                      <widget class="GtkScrolledWindow" id="scrolledwindow4">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="hscrollbar_policy">GTK_POLICY_AUTOMATIC</property>
                        <property name="vscrollbar_policy">GTK_POLICY_AUTOMATIC</property>
                        <child>
                          <widget class="GtkTreeView" id="file_view">
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                          </widget>
                        </child>
                      </widget>
                      <packing>
                        <property name="position">2</property>
                        <property name="tab_expand">False</property>
                      </packing>
                    </child>
                    <child>
                      <widget class="GtkLabel" id="label19">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">Files</property>
                      </widget>
                      <packing>
                        <property name="type">tab</property>
                        <property name="position">2</property>
                        <property name="tab_expand">False</property>
                        <property name="tab_fill">False</property>
                      </packing>
                    </child>
                  </widget>
                </child>
              </widget>
              <packing>
                <property name="resize">False</property>
                <property name="shrink">False</property>
              </packing>
            </child>
          </widget>
          <packing>
            <property name="right_attach">3</property>
            <property name="top_attach">2</property>
            <property name="bottom_attach">3</property>
          </packing>
        </child>
      </widget>
    </child>
  </widget>
</glade-interface>
