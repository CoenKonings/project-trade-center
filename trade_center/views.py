from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, View
from . import models
from .forms import ProposalForm


class CreateProposalView(View):
    template_name = "trade_center/create_proposal.html"
    form = None

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        self.form = ProposalForm(request.POST)

        if self.form.is_valid():
            proposal = models.SwitchProposal(
                from_project=self.form.cleaned_data["from_project"],
                to_project=self.form.cleaned_data["to_project"],
                name=self.form.cleaned_data["name"],
            )

            proposal.save()
            matches = proposal.find_matches()
            return redirect("/proposals/{}".format(proposal.id))
        else:
            return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = {
            "projects": models.Project.objects.all(),
            "proposals": models.SwitchProposal.objects.all(),
            "form": self.form if self.form else ProposalForm(),
            "success": False,
        }

        return context


class ProposalDetailView(DetailView):
    model = models.SwitchProposal
    template_name = "trade_center/proposal_detail.html"
    context_object_name = "proposal"
