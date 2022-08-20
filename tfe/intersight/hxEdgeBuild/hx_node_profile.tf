/*
resource "intersight_hyperflex_node_profile" "hx_node_profile_1" {
  name = "${var.cluster_name}_node_1"
  assigned_server {
    selector = "$filter=Serial eq 'xxxx'"
  }
  cluster_profile {
    moid = intersight_hyperflex_cluster_profile.hx_cluster_profile.results[0].moid
  }
}
resource "intersight_hyperflex_node_profile" "hx_node_profile_2" {
  name = "${var.cluster_name}_node_2"
  assigned_server {
    selector = "$filter=Serial eq 'WZP231803R5'"
  }
  cluster_profile {
    moid = intersight_hyperflex_cluster_profile.hx_cluster_profile.moid
  }
}
*/
