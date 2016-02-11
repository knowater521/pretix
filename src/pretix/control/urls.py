from django.conf.urls import include, url

from pretix.control.views import (
    auth, event, item, main, orders, organizer, user, vouchers,
)

urlpatterns = [
    url(r'^logout$', auth.logout, name='auth.logout'),
    url(r'^login$', auth.login, name='auth.login'),
    url(r'^register$', auth.register, name='auth.register'),
    url(r'^forgot$', auth.Forgot.as_view(), name='auth.forgot'),
    url(r'^forgot/recover$', auth.Recover.as_view(), name='auth.forgot.recover'),
    url(r'^$', main.index, name='index'),
    url(r'^settings$', user.UserSettings.as_view(), name='user.settings'),
    url(r'^organizers/$', organizer.OrganizerList.as_view(), name='organizers'),
    url(r'^organizers/add$', organizer.OrganizerCreate.as_view(), name='organizers.add'),
    url(r'^organizer/(?P<organizer>[^/]+)/edit$', organizer.OrganizerUpdate.as_view(), name='organizer.edit'),
    url(r'^events/$', main.EventList.as_view(), name='events'),
    url(r'^events/add$', main.EventCreateStart.as_view(), name='events.add'),
    url(r'^event/(?P<organizer>[^/]+)/add', main.EventCreate.as_view(), name='events.create'),
    url(r'^event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/', include([
        url(r'^$', event.index, name='event.index'),
        url(r'^settings/$', event.EventUpdate.as_view(), name='event.settings'),
        url(r'^settings/plugins$', event.EventPlugins.as_view(), name='event.settings.plugins'),
        url(r'^settings/permissions$', event.EventPermissions.as_view(), name='event.settings.permissions'),
        url(r'^settings/payment$', event.PaymentSettings.as_view(), name='event.settings.payment'),
        url(r'^settings/tickets$', event.TicketSettings.as_view(), name='event.settings.tickets'),
        url(r'^settings/email$', event.MailSettings.as_view(), name='event.settings.mail'),
        url(r'^items/$', item.ItemList.as_view(), name='event.items'),
        url(r'^items/add$', item.ItemCreate.as_view(), name='event.items.add'),
        url(r'^items/(?P<item>\d+)/$', item.ItemUpdateGeneral.as_view(), name='event.item'),
        url(r'^items/(?P<item>\d+)/variations$', item.ItemVariations.as_view(),
            name='event.item.variations'),
        url(r'^items/(?P<item>\d+)/up$', item.item_move_up, name='event.items.up'),
        url(r'^items/(?P<item>\d+)/down$', item.item_move_down, name='event.items.down'),
        url(r'^items/(?P<item>\d+)/delete$', item.ItemDelete.as_view(), name='event.items.delete'),
        url(r'^categories/$', item.CategoryList.as_view(), name='event.items.categories'),
        url(r'^categories/(?P<category>\d+)/delete$', item.CategoryDelete.as_view(),
            name='event.items.categories.delete'),
        url(r'^categories/(?P<category>\d+)/up$', item.category_move_up, name='event.items.categories.up'),
        url(r'^categories/(?P<category>\d+)/down$', item.category_move_down,
            name='event.items.categories.down'),
        url(r'^categories/(?P<category>\d+)/$', item.CategoryUpdate.as_view(),
            name='event.items.categories.edit'),
        url(r'^categories/add$', item.CategoryCreate.as_view(), name='event.items.categories.add'),
        url(r'^questions/$', item.QuestionList.as_view(), name='event.items.questions'),
        url(r'^questions/(?P<question>\d+)/delete$', item.QuestionDelete.as_view(),
            name='event.items.questions.delete'),
        url(r'^questions/(?P<question>\d+)/$', item.QuestionUpdate.as_view(),
            name='event.items.questions.edit'),
        url(r'^questions/add$', item.QuestionCreate.as_view(), name='event.items.questions.add'),
        url(r'^quotas/$', item.QuotaList.as_view(), name='event.items.quotas'),
        url(r'^quotas/(?P<quota>\d+)/$', item.QuotaUpdate.as_view(), name='event.items.quotas.edit'),
        url(r'^quotas/(?P<quota>\d+)/delete$', item.QuotaDelete.as_view(),
            name='event.items.quotas.delete'),
        url(r'^quotas/add$', item.QuotaCreate.as_view(), name='event.items.quotas.add'),
        url(r'^vouchers/$', vouchers.VoucherList.as_view(), name='event.vouchers'),
        url(r'^vouchers/(?P<voucher>\d+)/$', vouchers.VoucherUpdate.as_view(), name='event.voucher'),
        url(r'^vouchers/(?P<voucher>\d+)/delete$', vouchers.VoucherDelete.as_view(),
            name='event.voucher.delete'),
        url(r'^vouchers/add$', vouchers.VoucherCreate.as_view(), name='event.vouchers.add'),
        url(r'^orders/(?P<code>[0-9A-Z]+)/transition$', orders.OrderTransition.as_view(),
            name='event.order.transition'),
        url(r'^orders/(?P<code>[0-9A-Z]+)/resend$', orders.OrderResendLink.as_view(),
            name='event.order.resendlink'),
        url(r'^orders/(?P<code>[0-9A-Z]+)/extend$', orders.OrderExtend.as_view(),
            name='event.order.extend'),
        url(r'^orders/(?P<code>[0-9A-Z]+)/$', orders.OrderDetail.as_view(), name='event.order'),
        url(r'^orders/(?P<code>[0-9A-Z]+)/download/(?P<output>[^/]+)$', orders.OrderDownload.as_view(),
            name='event.order.download'),
        url(r'^orders/overview/$', orders.OverView.as_view(), name='event.orders.overview'),
        url(r'^orders/export/$', orders.ExportView.as_view(), name='event.orders.export'),
        url(r'^orders/go$', orders.OrderGo.as_view(), name='event.orders.go'),
        url(r'^orders/$', orders.OrderList.as_view(), name='event.orders'),
    ])),
]
