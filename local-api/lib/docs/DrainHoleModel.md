# DrainHoleModel

A drain hole of the model in the scene. Composes OrientationModel and ScenePositionModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orientation** | [**OrientationModel**](OrientationModel.md) |  | 
**position** | [**ScenePositionModel**](ScenePositionModel.md) |  | 
**diameter_mm** | **float** | The diameter of the drain hole, in mm | 
**depth_mm** | [**DrainHoleModelDepthMm**](DrainHoleModelDepthMm.md) |  | 
**outset_mm** | **float** | The back depth of the drain hole, in mm | [optional] 
**create_plug** | **bool** | Whether or not to create a plug for the drain hole | 
**max_search_distance** | **float** | The maximum distance, in mm, from the given position to search for a point on the surface of the model. Must be combined with depth_mm: \&quot;AUTO\&quot;. | [optional] 

## Example

```python
from formlabs_local_api.models.drain_hole_model import DrainHoleModel

# TODO update the JSON string below
json = "{}"
# create an instance of DrainHoleModel from a JSON string
drain_hole_model_instance = DrainHoleModel.from_json(json)
# print the JSON string representation of the object
print(DrainHoleModel.to_json())

# convert the object into a dict
drain_hole_model_dict = drain_hole_model_instance.to_dict()
# create an instance of DrainHoleModel from a dict
drain_hole_model_from_dict = DrainHoleModel.from_dict(drain_hole_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


