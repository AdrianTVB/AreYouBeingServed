namespace Creo.ViewModels.Images
{
	public class WordCloudImage
	{
		public string ImageUrl { get; set; }

		public WordCloudImage( )
		{

		}

		public WordCloudImage( string imageUrl )
		{
			ImageUrl = imageUrl;
		}
	}
}