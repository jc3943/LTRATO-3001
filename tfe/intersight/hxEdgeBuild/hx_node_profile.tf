
resource "intersight_hyperflex_node_profile" "hx_node_profile_1" {
  name = "${var.cluster_name}-01"
  assigned_server {
    selector = "$filter=Name eq 'sandbox-01'"
    //moid = intersight_hyperflex_cluster_profile.hx_cluster_profile.moid
    object_type = "compute.RackUnit"
  }
  cluster_profile {
    moid = intersight_hyperflex_cluster_profile.hx_cluster_profile.moid
    object_type = "hyperflex.ClusterProfile"
  }
}
resource "intersight_hyperflex_node_profile" "hx_node_profile_2" {
  name = "${var.cluster_name}-02"
  assigned_server {
    selector = "$filter=Name eq 'sandbox-02'"
    //moid = intersight_hyperflex_cluster_profile.hx_cluster_profile.moid
    object_type = "compute.RackUnit"
  }
  cluster_profile {
    moid = intersight_hyperflex_cluster_profile.hx_cluster_profile.moid
    object_type = "hyperflex.ClusterProfile"
  }
}
resource "intersight_hyperflex_node_profile" "hx_node_profile_3" {
  name = "${var.cluster_name}-03"
  assigned_server {
    selector = "$filter=Name eq 'sandbox-03'"
    //moid = intersight_hyperflex_cluster_profile.hx_cluster_profile.moid
    object_type = "compute.RackUnit"  
  }
  cluster_profile {
    moid = intersight_hyperflex_cluster_profile.hx_cluster_profile.moid
    object_type = "hyperflex.ClusterProfile"
  }
}
