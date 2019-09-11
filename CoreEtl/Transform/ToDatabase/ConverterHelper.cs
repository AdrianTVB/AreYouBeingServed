using Domain.EntityFramework;
using System;
using System.Collections.Generic;
using System.Linq;

namespace CoreEtl.Transform.ToDatabase
{
	public class ConverterHelper
	{
		private static Dictionary<string, Organisation> orgCache = new Dictionary<string, Organisation>( );
		private static Dictionary<string, Meeting> meetingCache = new Dictionary<string, Meeting>( );
		private static Dictionary<string, Official> officialCache = new Dictionary<string, Official>( );
		public Organisation GetOrCreateOrganisation( creo_dbEntities dbContext, string orgName )
		{
			string nameRefined = orgName.ToLower( ).Trim( );

			Organisation entity = null;
			if ( !orgCache.TryGetValue( nameRefined, out entity ) )
			{
				entity = dbContext.Organisations.FirstOrDefault( o => o.Name.ToLower( ) == nameRefined );
				if ( entity == null )
				{
					dbContext.Organisations.Add( entity = new Organisation( ) { Name = orgName } );
				}
				orgCache.Add( nameRefined, entity );
			}
			return entity;
		}

		public Meeting GetOrCreateMeeting( creo_dbEntities dbContext, string meetingName, DateTime date, Organisation organisation )
		{
			string nameRefined = meetingName.ToLower( ).Trim( );

			Meeting entity = null;
			if ( !meetingCache.TryGetValue( nameRefined, out entity ) )
			{
				entity = dbContext.Meetings.FirstOrDefault( o => o.Name.ToLower( ) == nameRefined && o.Date == date );
				if ( entity == null )
				{
					entity = new Meeting( ) { Name = meetingName, Date = date, Organisation = organisation };
					dbContext.Meetings.Add( entity );
				}
				meetingCache.Add( nameRefined, entity );
			}
			return entity;
		}

		public Official GetOrCreateOfficial( creo_dbEntities dbContext, string officialName, Organisation organisation )
		{
			string nameRefined = officialName.ToLower( ).Trim( );

			Official entity = null;
			if ( !officialCache.TryGetValue( nameRefined, out entity ) )
			{
				entity = dbContext.Officials.FirstOrDefault( o => o.Name.ToLower( ) == nameRefined );
				if ( entity == null )
				{
					entity = new Official( ) { Name = officialName, Organisation = organisation };
					dbContext.Officials.Add( entity );
				}
				officialCache.Add( nameRefined, entity );
			}
			return entity;
		}
	}
}