using AutoMapper;
using Creo.ViewModels.Organisation;
using Domain.EntityFramework;

namespace Creo.Mappings
{
	public class OrganistionProfile : Profile
	{
		public OrganistionProfile( )
		{
			CreateMap<Organisation, OrganisationListItem>( );
		}
	}
}