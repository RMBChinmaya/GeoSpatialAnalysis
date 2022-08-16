#5-Dimentional GeoSpatial analysis
#Importing necessart Modules
import holoviews as hv, geoviews as gv, param, dask.dataframe as dd, panel as pn, numpy as np
from colorcet import cm
from holoviews.operation.datashader import rasterize, shade

#Importing parquet file of the txt dataset provided
usecols = ['Lat','Lng','time','D','Intensity']
df = dd.read_parquet(r"C:\Users\chinm\Desktop\python_train\InnoCentive\GeoSpatialAnalysis\output.parquet")[usecols].persist()
df['D'] = df['D'].apply(str, meta=('D', 'object'))
df['Intensity'] = df['Intensity'].apply(int, meta=('Intensity', 'int64'))
df['Lat'] = df['Lat']*100000
df['Lng'] = df['Lng']*100000


#Creating Class/Methods for GeoSpatial Visualization
opts = dict(width=1000,height=600,xaxis=None,yaxis=None,bgcolor='black',show_grid=False)
cmaps = ['fire','bgy','bgyw','bmy','gray','kbc']
a,b,x,lamn,lamx,lgmn,lgmx = dd.compute(df.Intensity.min(), df.Intensity.max(),df.D.unique(),df.Lat.min(), df.Lat.max(),df.Lng.min(), df.Lng.max())

class WeatherDataExplorer(param.Parameterized):
    #parameterizing input variables
    map_layer  = param.ObjectSelector(cm['fire'], objects={c:cm[c] for c in cmaps})
    d          = param.ObjectSelector(default = x.to_list()[0], objects = x.to_list())
    day_time   = param.Range(default=(0, 24), bounds=(0, 24))
    intensity  = param.Range(default=(a, b), bounds=(a, b))
    latitude   = param.Range(default=(lamn,lamx), bounds=(lamn,lamx))
    longitude  = param.Range(default=(lgmn,lgmx), bounds=(lgmn,lgmx))
    
    
    @param.depends('day_time','intensity')
    def points(self):
        points = hv.Points(df, kdims=['Lat','Lng'], vdims=['time', 'Intensity'])
        if self.day_time != (0, 24): points = points.select(time=self.day_time)
        if self.intensity != (0, 100000): points = points.select(Intensity=self.intensity)
        if self.latitude != (lamn,lamx): points = points.select(Lat=self.latitude)
        if self.longitude != (lgmn,lgmx): points = points.select(Lng=self.longitude)
        if self.d != x.to_list() : points = points.select(D=self.d)
        return points

    def view(self,**kwargs):
        points = hv.DynamicMap(self.points)
        tiles = gv.tile_sources.StamenTerrain().apply.opts(**opts)
        agg = rasterize(points, x_sampling=0.01, y_sampling=0.01, width=600, height=400)
        return tiles * shade(agg, cmap=self.param.map_layer)

hv.extension('bokeh', logo=False)

sun = WeatherDataExplorer(name="Geo Data Viz")
pn.Row(sun.param, sun.view()).servable()