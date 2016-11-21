from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required


from baseapp.views.district_views import *
urlpatterns = patterns('',

    url(
        regex=r'^district/create/$',
        view=login_required(DistrictCreateView.as_view()),
        name='baseapp_district_create'
    ),


    url(
        regex=r'^district/(?P<pk>\d+?)/delete/$',
        view=login_required(DistrictDeleteView.as_view()),
        name='baseapp_district_delete'
    ),
    url(
        regex=r'^district/(?P<pk>\d+?)/$',
        view=login_required(DistrictDetailView.as_view()),
        name='baseapp_district_detail'
    ),
    url(
        regex=r'^district/$',
        view=login_required(DistrictListView.as_view()),
        name='baseapp_district_list'
    ),


    url(
        regex=r'^district/(?P<pk>\d+?)/update/$',
        view=login_required(DistrictUpdateView.as_view()),
        name='baseapp_district_update'
    ),


)


from baseapp.views.block_views import *
urlpatterns += patterns('',

    url(
        regex=r'^block/create/$',
        view=login_required(BlockCreateView.as_view()),
        name='baseapp_block_create'
    ),


    url(
        regex=r'^block/(?P<pk>\d+?)/delete/$',
        view=login_required(BlockDeleteView.as_view()),
        name='baseapp_block_delete'
    ),
    url(
        regex=r'^block/(?P<pk>\d+?)/$',
        view=login_required(BlockDetailView.as_view()),
        name='baseapp_block_detail'
    ),
    url(
        regex=r'^block/$',
        view=login_required(BlockListView.as_view()),
        name='baseapp_block_list'
    ),


    url(
        regex=r'^block/(?P<pk>\d+?)/update/$',
        view=login_required(BlockUpdateView.as_view()),
        name='baseapp_block_update'
    ),


)


from baseapp.views.assembly_views import *
urlpatterns += patterns('',

    url(
        regex=r'^assembly/create/$',
        view=login_required(AssemblyCreateView.as_view()),
        name='baseapp_assembly_create'
    ),


    url(
        regex=r'^assembly/(?P<pk>\d+?)/delete/$',
        view=login_required(AssemblyDeleteView.as_view()),
        name='baseapp_assembly_delete'
    ),
    url(
        regex=r'^assembly/(?P<pk>\d+?)/$',
        view=login_required(AssemblyDetailView.as_view()),
        name='baseapp_assembly_detail'
    ),
    url(
        regex=r'^assembly/$',
        view=login_required(AssemblyListView.as_view()),
        name='baseapp_assembly_list'
    ),


    url(
        regex=r'^assembly/(?P<pk>\d+?)/update/$',
        view=login_required(AssemblyUpdateView.as_view()),
        name='baseapp_assembly_update'
    ),


)


from baseapp.views.parliamentary_views import *
urlpatterns += patterns('',

    url(
        regex=r'^parliamentary/create/$',
        view=login_required(ParliamentaryCreateView.as_view()),
        name='baseapp_parliamentary_create'
    ),


    url(
        regex=r'^parliamentary/(?P<pk>\d+?)/delete/$',
        view=login_required(ParliamentaryDeleteView.as_view()),
        name='baseapp_parliamentary_delete'
    ),
    url(
        regex=r'^parliamentary/(?P<pk>\d+?)/$',
        view=login_required(ParliamentaryDetailView.as_view()),
        name='baseapp_parliamentary_detail'
    ),
    url(
        regex=r'^parliamentary/$',
        view=login_required(ParliamentaryListView.as_view()),
        name='baseapp_parliamentary_list'
    ),


    url(
        regex=r'^parliamentary/(?P<pk>\d+?)/update/$',
        view=login_required(ParliamentaryUpdateView.as_view()),
        name='baseapp_parliamentary_update'
    ),


)



from baseapp.views.habitation_views import *
urlpatterns += patterns('',

    url(
        regex=r'^habitation/create/$',
        view=login_required(HabitationCreateView.as_view()),
        name='baseapp_habitation_create'
    ),


    url(
        regex=r'^habitation/(?P<pk>\d+?)/delete/$',
        view=login_required(HabitationDeleteView.as_view()),
        name='baseapp_habitation_delete'
    ),
    url(
        regex=r'^habitation/(?P<pk>\d+?)/$',
        view=login_required(HabitationDetailView.as_view()),
        name='baseapp_habitation_detail'
    ),
    url(
        regex=r'^habitation/$',
        view=login_required(HabitationListView.as_view()),
        name='baseapp_habitation_list'
    ),


    url(
        regex=r'^habitation/(?P<pk>\d+?)/update/$',
        view=login_required(HabitationUpdateView.as_view()),
        name='baseapp_habitation_update'
    ),


)


from baseapp.views.management_views import *
urlpatterns += patterns('',

    url(
        regex=r'^management/create/$',
        view=login_required(ManagementCreateView.as_view()),
        name='baseapp_management_create'
    ),


    url(
        regex=r'^management/(?P<pk>\d+?)/delete/$',
        view=login_required(ManagementDeleteView.as_view()),
        name='baseapp_management_delete'
    ),
    url(
        regex=r'^management/(?P<pk>\d+?)/$',
        view=login_required(ManagementDetailView.as_view()),
        name='baseapp_management_detail'
    ),
    url(
        regex=r'^management/$',
        view=login_required(ManagementListView.as_view()),
        name='baseapp_management_list'
    ),


    url(
        regex=r'^management/(?P<pk>\d+?)/update/$',
        view=login_required(ManagementUpdateView.as_view()),
        name='baseapp_management_update'
    ),


)

from baseapp.views.category_views import *
urlpatterns += patterns('',

    url(
        regex=r'^category/create/$',
        view=login_required(CategoryCreateView.as_view()),
        name='baseapp_category_create'
    ),


    url(
        regex=r'^category/(?P<pk>\d+?)/delete/$',
        view=login_required(CategoryDeleteView.as_view()),
        name='baseapp_category_delete'
    ),
    url(
        regex=r'^category/(?P<pk>\d+?)/$',
        view=login_required(CategoryDetailView.as_view()),
        name='baseapp_category_detail'
    ),
    url(
        regex=r'^category/$',
        view=login_required(CategoryListView.as_view()),
        name='baseapp_category_list'
    ),


    url(
        regex=r'^category/(?P<pk>\d+?)/update/$',
        view=login_required(CategoryUpdateView.as_view()),
        name='baseapp_category_update'
    ),


)
from baseapp.views.school_views import *
urlpatterns += patterns('',

    url(
        regex=r'^school/create/$',
        view=login_required(SchoolCreateView.as_view()),
        name='baseapp_school_create'
    ),


    url(
        regex=r'^school/(?P<pk>\d+?)/delete/$',
        view=login_required(SchoolDeleteView.as_view()),
        name='baseapp_school_delete'
    ),
    url(
        regex=r'^school/(?P<pk>\d+?)/$',
        view=login_required(SchoolDetailView.as_view()),
        name='baseapp_school_detail'
    ),
    url(
        regex=r'^school/$',
        view=login_required(SchoolListView.as_view()),
        name='baseapp_school_list'
    ),


    url(
        regex=r'^school/(?P<pk>\d+?)/update/$',
        view=login_required(SchoolUpdateView.as_view()),
        name='baseapp_school_update'
    ),


)


from baseapp.views.taluk_views import *
urlpatterns += patterns('',

    url(
        regex=r'^taluk/create/$',
        view=login_required(TalukCreateView.as_view()),
        name='baseapp_taluk_create'
    ),


    url(
        regex=r'^taluk/(?P<pk>\d+?)/delete/$',
        view=login_required(TalukDeleteView.as_view()),
        name='baseapp_taluk_delete'
    ),
    url(
        regex=r'^taluk/(?P<pk>\d+?)/$',
        view=login_required(TalukDetailView.as_view()),
        name='baseapp_taluk_detail'
    ),
    url(
        regex=r'^taluk/$',
        view=login_required(TalukListView.as_view()),
        name='baseapp_taluk_list'
    ),


    url(
        regex=r'^taluk/(?P<pk>\d+?)/update/$',
        view=login_required(TalukUpdateView.as_view()),
        name='baseapp_taluk_update'
    ),


)


from baseapp.views.educational_district_views import *
urlpatterns += patterns('',

    url(
        regex=r'^educational_district/create/$',
        view=login_required(Educational_districtCreateView.as_view()),
        name='baseapp_educational_district_create'
    ),


    url(
        regex=r'^educational_district/(?P<pk>\d+?)/delete/$',
        view=login_required(Educational_districtDeleteView.as_view()),
        name='baseapp_educational_district_delete'
    ),
    url(
        regex=r'^educational_district/(?P<pk>\d+?)/$',
        view=login_required(Educational_districtDetailView.as_view()),
        name='baseapp_educational_district_detail'
    ),
    url(
        regex=r'^educational_district/$',
        view=login_required(Educational_districtListView.as_view()),
        name='baseapp_educational_district_list'
    ),


    url(
        regex=r'^educational_district/(?P<pk>\d+?)/update/$',
        view=login_required(Educational_districtUpdateView.as_view()),
        name='baseapp_educational_district_update'
    ),


)


from baseapp.views.educational_block_views import *
urlpatterns += patterns('',

    url(
        regex=r'^educational_block/create/$',
        view=login_required(Educational_blockCreateView.as_view()),
        name='baseapp_educational_block_create'
    ),


    url(
        regex=r'^educational_block/(?P<pk>\d+?)/delete/$',
        view=login_required(Educational_blockDeleteView.as_view()),
        name='baseapp_educational_block_delete'
    ),
    url(
        regex=r'^educational_block/(?P<pk>\d+?)/$',
        view=login_required(Educational_blockDetailView.as_view()),
        name='baseapp_educational_block_detail'
    ),
    url(
        regex=r'^educational_block/$',
        view=login_required(Educational_blockListView.as_view()),
        name='baseapp_educational_block_list'
    ),


    url(
        regex=r'^educational_block/(?P<pk>\d+?)/update/$',
        view=login_required(Educational_blockUpdateView.as_view()),
        name='baseapp_educational_block_update'
    ),


)


from baseapp.views.revenue_block_views import *
urlpatterns += patterns('',

    url(
        regex=r'^revenue_block/create/$',
        view=login_required(Revenue_blockCreateView.as_view()),
        name='baseapp_revenue_block_create'
    ),


    url(
        regex=r'^revenue_block/(?P<pk>\d+?)/delete/$',
        view=login_required(Revenue_blockDeleteView.as_view()),
        name='baseapp_revenue_block_delete'
    ),
    url(
        regex=r'^revenue_block/(?P<pk>\d+?)/$',
        view=login_required(Revenue_blockDetailView.as_view()),
        name='baseapp_revenue_block_detail'
    ),
    url(
        regex=r'^revenue_block/$',
        view=login_required(Revenue_blockListView.as_view()),
        name='baseapp_revenue_block_list'
    ),


    url(
        regex=r'^revenue_block/(?P<pk>\d+?)/update/$',
        view=login_required(Revenue_blockUpdateView.as_view()),
        name='baseapp_revenue_block_update'
    ),


)


from baseapp.views.community_views import *
urlpatterns += patterns('',

    url(
        regex=r'^community/create/$',
        view=login_required(CommunityCreateView.as_view()),
        name='baseapp_community_create'
    ),


    url(
        regex=r'^community/(?P<pk>\d+?)/delete/$',
        view=login_required(CommunityDeleteView.as_view()),
        name='baseapp_community_delete'
    ),
    url(
        regex=r'^community/(?P<pk>\d+?)/$',
        view=login_required(CommunityDetailView.as_view()),
        name='baseapp_community_detail'
    ),
    url(
        regex=r'^community/$',
        view=login_required(CommunityListView.as_view()),
        name='baseapp_community_list'
    ),


    url(
        regex=r'^community/(?P<pk>\d+?)/update/$',
        view=login_required(CommunityUpdateView.as_view()),
        name='baseapp_community_update'
    ),


)


from baseapp.views.religion_views import *
urlpatterns += patterns('',

    url(
        regex=r'^religion/create/$',
        view=login_required(ReligionCreateView.as_view()),
        name='baseapp_religion_create'
    ),


    url(
        regex=r'^religion/(?P<pk>\d+?)/delete/$',
        view=login_required(ReligionDeleteView.as_view()),
        name='baseapp_religion_delete'
    ),
    url(
        regex=r'^religion/(?P<pk>\d+?)/$',
        view=login_required(ReligionDetailView.as_view()),
        name='baseapp_religion_detail'
    ),
    url(
        regex=r'^religion/$',
        view=login_required(ReligionListView.as_view()),
        name='baseapp_religion_list'
    ),


    url(
        regex=r'^religion/(?P<pk>\d+?)/update/$',
        view=login_required(ReligionUpdateView.as_view()),
        name='baseapp_religion_update'
    ),


)


from baseapp.views.language_views import *
urlpatterns += patterns('',

    url(
        regex=r'^language/create/$',
        view=login_required(LanguageCreateView.as_view()),
        name='baseapp_language_create'
    ),


    url(
        regex=r'^language/(?P<pk>\d+?)/delete/$',
        view=login_required(LanguageDeleteView.as_view()),
        name='baseapp_language_delete'
    ),
    url(
        regex=r'^language/(?P<pk>\d+?)/$',
        view=login_required(LanguageDetailView.as_view()),
        name='baseapp_language_detail'
    ),
    url(
        regex=r'^language/$',
        view=login_required(LanguageListView.as_view()),
        name='baseapp_language_list'
    ),


    url(
        regex=r'^language/(?P<pk>\d+?)/update/$',
        view=login_required(LanguageUpdateView.as_view()),
        name='baseapp_language_update'
    ),


)


from baseapp.views.differently_abled_views import *
urlpatterns += patterns('',

    url(
        regex=r'^differently_abled/create/$',
        view=login_required(Differently_abledCreateView.as_view()),
        name='baseapp_differently_abled_create'
    ),


    url(
        regex=r'^differently_abled/(?P<pk>\d+?)/delete/$',
        view=login_required(Differently_abledDeleteView.as_view()),
        name='baseapp_differently_abled_delete'
    ),
    url(
        regex=r'^differently_abled/(?P<pk>\d+?)/$',
        view=login_required(Differently_abledDetailView.as_view()),
        name='baseapp_differently_abled_detail'
    ),
    url(
        regex=r'^differently_abled/$',
        view=login_required(Differently_abledListView.as_view()),
        name='baseapp_differently_abled_list'
    ),


    url(
        regex=r'^differently_abled/(?P<pk>\d+?)/update/$',
        view=login_required(Differently_abledUpdateView.as_view()),
        name='baseapp_differently_abled_update'
    ),


)


from baseapp.views.disadvantaged_group_views import *
urlpatterns += patterns('',

    url(
        regex=r'^disadvantaged_group/create/$',
        view=login_required(Disadvantaged_groupCreateView.as_view()),
        name='baseapp_disadvantaged_group_create'
    ),


    url(
        regex=r'^disadvantaged_group/(?P<pk>\d+?)/delete/$',
        view=login_required(Disadvantaged_groupDeleteView.as_view()),
        name='baseapp_disadvantaged_group_delete'
    ),
    url(
        regex=r'^disadvantaged_group/(?P<pk>\d+?)/$',
        view=login_required(Disadvantaged_groupDetailView.as_view()),
        name='baseapp_disadvantaged_group_detail'
    ),
    url(
        regex=r'^disadvantaged_group/$',
        view=login_required(Disadvantaged_groupListView.as_view()),
        name='baseapp_disadvantaged_group_list'
    ),


    url(
        regex=r'^disadvantaged_group/(?P<pk>\d+?)/update/$',
        view=login_required(Disadvantaged_groupUpdateView.as_view()),
        name='baseapp_disadvantaged_group_update'
    ),


)


from baseapp.views.schemes_views import *
urlpatterns += patterns('',

    url(
        regex=r'^schemes/create/$',
        view=login_required(SchemesCreateView.as_view()),
        name='baseapp_schemes_create'
    ),


    url(
        regex=r'^schemes/(?P<pk>\d+?)/delete/$',
        view=login_required(SchemesDeleteView.as_view()),
        name='baseapp_schemes_delete'
    ),
    url(
        regex=r'^schemes/(?P<pk>\d+?)/$',
        view=login_required(SchemesDetailView.as_view()),
        name='baseapp_schemes_detail'
    ),
    url(
        regex=r'^schemes/$',
        view=login_required(SchemesListView.as_view()),
        name='baseapp_schemes_list'
    ),


    url(
        regex=r'^schemes/(?P<pk>\d+?)/update/$',
        view=login_required(SchemesUpdateView.as_view()),
        name='baseapp_schemes_update'
    ),


)

from baseapp.views.academic_year_views import *
urlpatterns += patterns('',

    url(
        regex=r'^academic_year/create/$',
        view=login_required(Academic_YearCreateView.as_view()),
        name='baseapp_academic_year_create'
    ),

    url(
        regex=r'^academic_year/(?P<pk>\d+?)/delete/$',
        view=login_required(Academic_YearDeleteView.as_view()),
        name='baseapp_academic_year_delete'
    ),
    url(
        regex=r'^academic_year/(?P<pk>\d+?)/$',
        view=login_required(Academic_YearDetailView.as_view()),
        name='baseapp_academic_year_detail'
    ),
    url(
        regex=r'^academic_year/$',
        view=login_required(Academic_YearListView.as_view()),
        name='baseapp_academic_year_list'
    ),


    url(
        regex=r'^academic_year/(?P<pk>\d+?)/update/$',
        view=login_required(Academic_YearUpdateView.as_view()),
        name='baseapp_academic_year_update'
    ),

)

from baseapp.views.bank_views import *
urlpatterns += patterns('',

    url(
        regex=r'^bank/create/$',
        view=login_required(BankCreateView.as_view()),
        name='baseapp_bank_create'
    ),


    url(
        regex=r'^bank/(?P<pk>\d+?)/delete/$',
        view=login_required(BankDeleteView.as_view()),
        name='baseapp_bank_delete'
    ),
    url(
        regex=r'^bank/(?P<pk>\d+?)/$',
        view=login_required(BankDetailView.as_view()),
        name='baseapp_bank_detail'
    ),
    url(
        regex=r'^bank/$',
        view=login_required(BankListView.as_view()),
        name='baseapp_bank_list'
    ),


    url(
        regex=r'^bank/(?P<pk>\d+?)/update/$',
        view=login_required(BankUpdateView.as_view()),
        name='baseapp_bank_update'
    ),

)

from baseapp.views.education_medium_views import *
urlpatterns += patterns('',

    url(
        regex=r'^education_medium/create/$',
        view=login_required(Education_mediumCreateView.as_view()),
        name='baseapp_education_medium_create'
    ),


    url(
        regex=r'^education_medium/(?P<pk>\d+?)/delete/$',
        view=login_required(Education_mediumDeleteView.as_view()),
        name='baseapp_education_medium_delete'
    ),
    url(
        regex=r'^education_medium/(?P<pk>\d+?)/$',
        view=login_required(Education_mediumDetailView.as_view()),
        name='baseapp_education_medium_detail'
    ),
    url(
        regex=r'^education_medium/$',
        view=login_required(Education_mediumListView.as_view()),
        name='baseapp_education_medium_list'
    ),

    url(
        regex=r'^education_medium/(?P<pk>\d+?)/update/$',
        view=login_required(Education_mediumUpdateView.as_view()),
        name='baseapp_education_medium_update'
    ),

)


from baseapp.views.zone_views import *
urlpatterns += patterns('',

    url(
        regex=r'^zone/create/$',
        view=login_required(ZoneCreateView.as_view()),
        name='baseapp_zone_create'
    ),

    url(
        regex=r'^zone/(?P<pk>\d+?)/delete/$',
        view=login_required(ZoneDeleteView.as_view()),
        name='baseapp_zone_delete'
    ),
    url(
        regex=r'^zone/(?P<pk>\d+?)/$',
        view=login_required(ZoneDetailView.as_view()),
        name='baseapp_zone_detail'
    ),
    url(
        regex=r'^zone/$',
        view=login_required(ZoneListView.as_view()),
        name='baseapp_zone_list'
    ),

    url(
        regex=r'^zone/(?P<pk>\d+?)/update/$',
        view=login_required(ZoneUpdateView.as_view()),
        name='baseapp_zone_update'
    ),

)

from baseapp.views.sub_castes_views import *
urlpatterns += patterns('',

    url(
        regex=r'^sub_castes/create/$',
        view=login_required(Sub_CastesCreateView.as_view()),
        name='baseapp_sub_castes_create'
    ),

    url(
        regex=r'^sub_castes/(?P<pk>\d+?)/delete/$',
        view=login_required(Sub_CastesDeleteView.as_view()),
        name='baseapp_sub_castes_delete'
    ),
    url(
        regex=r'^sub_castes/(?P<pk>\d+?)/$',
        view=login_required(Sub_CastesDetailView.as_view()),
        name='baseapp_sub_castes_detail'
    ),
    url(
        regex=r'^sub_castes/$',
        view=login_required(Sub_CastesListView.as_view()),
        name='baseapp_sub_castes_list'
    ),

    url(
        regex=r'^sub_castes/(?P<pk>\d+?)/update/$',
        view=login_required(Sub_CastesUpdateView.as_view()),
        name='baseapp_sub_castes_update'
    ),

)

from baseapp.views.nationality_views import *
urlpatterns += patterns('',

    url(
        regex=r'^nationality/create/$',
        view=login_required(NationalityCreateView.as_view()),
        name='baseapp_nationality_create'
    ),

    url(
        regex=r'^nationality/(?P<pk>\d+?)/delete/$',
        view=login_required(NationalityDeleteView.as_view()),
        name='baseapp_nationality_delete'
    ),
    url(
        regex=r'^nationality/(?P<pk>\d+?)/$',
        view=login_required(NationalityDetailView.as_view()),
        name='baseapp_nationality_detail'
    ),
    url(
        regex=r'^nationality/$',
        view=login_required(NationalityListView.as_view()),
        name='baseapp_nationality_list'
    ),

    url(
        regex=r'^nationality/(?P<pk>\d+?)/update/$',
        view=login_required(NationalityUpdateView.as_view()),
        name='baseapp_nationality_update'
    ),

)

from baseapp.views.class_studying_views import *
urlpatterns += patterns('',

    url(
        regex=r'^class_studying/create/$',
        view=login_required(Class_StudyingCreateView.as_view()),
        name='baseapp_class_studying_create'
    ),

    url(
        regex=r'^class_studying/(?P<pk>\d+?)/delete/$',
        view=login_required(Class_StudyingDeleteView.as_view()),
        name='baseapp_class_studying_delete'
    ),
    url(
        regex=r'^class_studying/(?P<pk>\d+?)/$',
        view=login_required(Class_StudyingDetailView.as_view()),
        name='baseapp_class_studying_detail'
    ),
    url(
        regex=r'^class_studying/$',
        view=login_required(Class_StudyingListView.as_view()),
        name='baseapp_class_studying_list'
    ),

    url(
        regex=r'^class_studying/(?P<pk>\d+?)/update/$',
        view=login_required(Class_StudyingUpdateView.as_view()),
        name='baseapp_class_studying_update'
    ),

)

from baseapp.views.group_code_views import *
urlpatterns += patterns('',

    url(
        regex=r'^group_code/create/$',
        view=login_required(Group_codeCreateView.as_view()),
        name='baseapp_group_code_create'
    ),

    url(
        regex=r'^group_code/(?P<pk>\d+?)/delete/$',
        view=login_required(Group_codeDeleteView.as_view()),
        name='baseapp_group_code_delete'
    ),
    url(
        regex=r'^group_code/(?P<pk>\d+?)/$',
        view=login_required(Group_codeDetailView.as_view()),
        name='baseapp_group_code_detail'
    ),
    url(
        regex=r'^group_code/$',
        view=login_required(Group_codeListView.as_view()),
        name='baseapp_group_code_list'
    ),

    url(
        regex=r'^group_code/(?P<pk>\d+?)/update/$',
        view=login_required(Group_codeUpdateView.as_view()),
        name='baseapp_group_code_update'
    ),

)
