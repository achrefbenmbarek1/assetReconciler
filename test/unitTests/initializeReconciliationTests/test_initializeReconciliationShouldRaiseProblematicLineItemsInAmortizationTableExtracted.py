from QuantityReconciliation.Reconciler.domainEvent.ProblematicLineItemsInAmortizationTableExtracted import (
    ProblematicLineItemsInAmortizationTableExtracted,
)
from QuantityReconciliation.Reconciler.entity.Reconciler import Reconciler
from QuantityReconciliation.infrastructure.command.InitializeReconciliation import (
    InitializeReconciliation,
)
from QuantityReconciliation.Reconciler.entity.Reconciler import Reconciler

import pytest


@pytest.fixture()
def initializeReconciliationCmdWithNoProblematicLineItemsInAmortizationTable():
    filename = "dfhdf"
    amortizationTable = [
        {
            "NumFiche": "Pwc_00001",
            "Descriptif": "jfdkfj",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "ghd",
            "marque": "jfk",
            "model": "dkfj",
            "fournisseur": "dfj",
            "groupe": "dfjkd",
            "famille": "dkf",
            "sousFamille": "dkfj",
        },
        {
            "NumFiche": "Pwc_0003",
            "Descriptif": "Missing",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "dfjj",
            "marque": "djf",
            "model": "dff",
            "fournisseur": "df",
            "groupe": "kdjf",
            "famille": "dfkj",
            "sousFamille": "djkf",
        },
        {
            "NumFiche": "Pwc_0004",
            "Descriptif": "dfkjfkj",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "dfjj",
            "marque": "djf",
            "model": "dff",
            "fournisseur": "dfkj",
            "groupe": "dkfk",
            "famille": "dkf",
            "sousFamille": "djkf",
        },
    ]

    physicalInventory = [
        {
            "cb": "Bs_45585",
            "NumFiche": "Pwc_00001",
            "Descriptif": "jfdkfj",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "thidjkdjk",
            "marque": "jfk",
            "model": "dkfj",
            "fournisseur": "dfj",
            "groupe": "dfjkd",
            "famille": "dkf",
            "sousFamille": "dkfj",
        },
        {
            "cb": "Bs_4558",
            "NumFiche": "Missing",
            "Descriptif": "dfkjfkj",
            "Valide": "Missing",
            "Etablissement": "pwc",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "dfjjfdfk",
            "marque": "dfj",
            "model": "df",
            "fournisseur": "dfkj",
            "groupe": "dkfk",
            "famille": "dkf",
            "sousFamille": "dkfj",
        },
    ]

    eventsIds = ["dfhdf", "djfk", "dfih", "dfhi"]
    return InitializeReconciliation(
        filename, physicalInventory, amortizationTable, eventsIds
    )


@pytest.fixture()
def initializeReconciliationCmdWithSomeProblematicLineItemsInAmortizationTable():
    filename = "dfhdf"
    amortizationTable = [
        {
            "NumFiche": "",
            "Descriptif": "jfdkfj",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "ghd",
            "marque": "jfk",
            "model": "dkfj",
            "fournisseur": "dfj",
            "groupe": "dfjkd",
            "famille": "dkf",
            "sousFamille": "dkfj",
        },
        {
            "NumFiche": "Pwc_0003",
            "Descriptif": "Missing",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "dfjj",
            "marque": "djf",
            "model": "dff",
            "fournisseur": "df",
            "groupe": "kdjf",
            "famille": "dfkj",
            "sousFamille": "djkf",
        },
        {
            "NumFiche": "Pwc_0004",
            "Descriptif": "dfkjfkj",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "dfjj",
            "marque": "djf",
            "model": "dff",
            "fournisseur": "dfkj",
            "groupe": "dkfk",
            "famille": "dkf",
            "sousFamille": "djkf",
        },
    ]

    physicalInventory = [
        {
            "cb": "Bs_45585",
            "NumFiche": "Pwc_00001",
            "Descriptif": "jfdkfj",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "thidjkdjk",
            "marque": "jfk",
            "model": "dkfj",
            "fournisseur": "dfj",
            "groupe": "dfjkd",
            "famille": "dkf",
            "sousFamille": "dkfj",
        },
        {
            "cb": "Bs_4558",
            "NumFiche": "Missing",
            "Descriptif": "dfkjfkj",
            "Valide": "Missing",
            "Etablissement": "pwc",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "dfjjfdfk",
            "marque": "dfj",
            "model": "df",
            "fournisseur": "dfkj",
            "groupe": "dkfk",
            "famille": "dkf",
            "sousFamille": "dkfj",
        },
    ]

    eventsIds = ["dfhdf", "djfk", "dfih", "dfhi"]
    return InitializeReconciliation(
        filename, physicalInventory, amortizationTable, eventsIds
    )


@pytest.fixture()
def initializeReconciliationCmdWithAllProblematicLineItemsInAmortizationTable():
    filename = "dfhdf"
    amortizationTable = [
        {
            "NumFiche": "",
            "Descriptif": "jfdkfj",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "ghd",
            "marque": "jfk",
            "model": "dkfj",
            "fournisseur": "dfj",
            "groupe": "dfjkd",
            "famille": "dkf",
            "sousFamille": "dkfj",
        },
        {
            "NumFiche": "",
            "Descriptif": "Missing",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "dfjj",
            "marque": "djf",
            "model": "dff",
            "fournisseur": "df",
            "groupe": "kdjf",
            "famille": "dfkj",
            "sousFamille": "djkf",
        },
        {
            "NumFiche": "",
            "Descriptif": "dfkjfkj",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "dfjj",
            "marque": "djf",
            "model": "dff",
            "fournisseur": "dfkj",
            "groupe": "dkfk",
            "famille": "dkf",
            "sousFamille": "djkf",
        },
    ]

    physicalInventory = [
        {
            "cb": "Bs_45585",
            "NumFiche": "Pwc_00001",
            "Descriptif": "jfdkfj",
            "Valide": "Missing",
            "Etablissement": "Siege",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "thidjkdjk",
            "marque": "jfk",
            "model": "dkfj",
            "fournisseur": "dfj",
            "groupe": "dfjkd",
            "famille": "dkf",
            "sousFamille": "dkfj",
        },
        {
            "cb": "Bs_4558",
            "NumFiche": "Missing",
            "Descriptif": "dfkjfkj",
            "Valide": "Missing",
            "Etablissement": "pwc",
            "CompteG\\u00e9n\\u00e9ral": "Missing",
            "Sch\\u00e9ma": "Missing",
            "Intitule": "dfjjfdfk",
            "marque": "dfj",
            "model": "df",
            "fournisseur": "dfkj",
            "groupe": "dkfk",
            "famille": "dkf",
            "sousFamille": "dkfj",
        },
    ]

    eventsIds = ["dfhdf", "djfk", "dfih", "dfhi"]
    return InitializeReconciliation(
        filename, physicalInventory, amortizationTable, eventsIds
    )


class TestInitializeReconciliationShouldRaiseProblematicLineItemsInAmortizationTableExtracted:
    def test_one_no_problematic_line_items_in_amortization_table(
        self, initializeReconciliationCmdWithNoProblematicLineItemsInAmortizationTable
    ):
        reconciler = Reconciler([])
        reconciler.initializeReconciliation(
            initializeReconciliationCmdWithNoProblematicLineItemsInAmortizationTable
        )
        doesTheEventProblematicLineItemsInAmortizationTableExtractedExist = False
        isExpectedReconciliationId = False
        isExpectedPayload = False
        for event in reconciler.domainEvents:
            if isinstance(event, ProblematicLineItemsInAmortizationTableExtracted):
                doesTheEventProblematicLineItemsInAmortizationTableExtractedExist = True
                isExpectedReconciliationId = (
                    event.reconciliationId
                    == initializeReconciliationCmdWithNoProblematicLineItemsInAmortizationTable.reconciliationId
                )
                isExpectedPayload = (
                    event.payload["problematicLineItemsInAmortizationTable"] == []
                )

        assert doesTheEventProblematicLineItemsInAmortizationTableExtractedExist
        assert isExpectedPayload
        assert isExpectedReconciliationId

    def test_two_some_missing_line_items_in_amortization_table(
        self, initializeReconciliationCmdWithSomeProblematicLineItemsInAmortizationTable
    ):
        reconciler = Reconciler([])
        reconciler.initializeReconciliation(
            initializeReconciliationCmdWithSomeProblematicLineItemsInAmortizationTable
        )
        doesTheEventProblematicLineItemsInAmortizationTableExtractedExist = False
        isExpectedReconciliationId = False
        isExpectedPayload = False
        for event in reconciler.domainEvents:
            if isinstance(event, ProblematicLineItemsInAmortizationTableExtracted):
                doesTheEventProblematicLineItemsInAmortizationTableExtractedExist = True
                isExpectedReconciliationId = (
                    event.reconciliationId
                    == initializeReconciliationCmdWithSomeProblematicLineItemsInAmortizationTable.reconciliationId
                )
                isExpectedPayload = event.payload[
                    "problematicLineItemsInAmortizationTable"
                ] == [
                    {
                        "NumFiche": "",
                        "Descriptif": "jfdkfj",
                        "Valide": "Missing",
                        "Etablissement": "Siege",
                        "CompteG\\u00e9n\\u00e9ral": "Missing",
                        "Sch\\u00e9ma": "Missing",
                        "Intitule": "ghd",
                        "marque": "jfk",
                        "model": "dkfj",
                        "fournisseur": "dfj",
                        "groupe": "dfjkd",
                        "famille": "dkf",
                        "sousFamille": "dkfj",
                    }
                ]

        assert doesTheEventProblematicLineItemsInAmortizationTableExtractedExist
        assert isExpectedPayload
        assert isExpectedReconciliationId

    def test_three_all_missing_line_items_in_amortization_table(
        self, initializeReconciliationCmdWithAllProblematicLineItemsInAmortizationTable
    ):
        reconciler = Reconciler([])
        reconciler.initializeReconciliation(
            initializeReconciliationCmdWithAllProblematicLineItemsInAmortizationTable
        )
        doesTheEventProblematicLineItemsInAmortizationTableExtractedExist = False
        isExpectedReconciliationId = False
        isExpectedPayload = False
        for event in reconciler.domainEvents:
            if isinstance(event, ProblematicLineItemsInAmortizationTableExtracted):
                doesTheEventProblematicLineItemsInAmortizationTableExtractedExist = True
                isExpectedReconciliationId = (
                    event.reconciliationId
                    == initializeReconciliationCmdWithAllProblematicLineItemsInAmortizationTable.reconciliationId
                )
                isExpectedPayload = event.payload[
                    "problematicLineItemsInAmortizationTable"
                ] == [
                    {
                        "NumFiche": "",
                        "Descriptif": "jfdkfj",
                        "Valide": "Missing",
                        "Etablissement": "Siege",
                        "CompteG\\u00e9n\\u00e9ral": "Missing",
                        "Sch\\u00e9ma": "Missing",
                        "Intitule": "ghd",
                        "marque": "jfk",
                        "model": "dkfj",
                        "fournisseur": "dfj",
                        "groupe": "dfjkd",
                        "famille": "dkf",
                        "sousFamille": "dkfj",
                    },
                    {
                        "NumFiche": "",
                        "Descriptif": "Missing",
                        "Valide": "Missing",
                        "Etablissement": "Siege",
                        "CompteG\\u00e9n\\u00e9ral": "Missing",
                        "Sch\\u00e9ma": "Missing",
                        "Intitule": "dfjj",
                        "marque": "djf",
                        "model": "dff",
                        "fournisseur": "df",
                        "groupe": "kdjf",
                        "famille": "dfkj",
                        "sousFamille": "djkf",
                    },
                    {
                        "NumFiche": "",
                        "Descriptif": "dfkjfkj",
                        "Valide": "Missing",
                        "Etablissement": "Siege",
                        "CompteG\\u00e9n\\u00e9ral": "Missing",
                        "Sch\\u00e9ma": "Missing",
                        "Intitule": "dfjj",
                        "marque": "djf",
                        "model": "dff",
                        "fournisseur": "dfkj",
                        "groupe": "dkfk",
                        "famille": "dkf",
                        "sousFamille": "djkf",
                    },
                ]

        assert doesTheEventProblematicLineItemsInAmortizationTableExtractedExist
        assert isExpectedPayload
        assert isExpectedReconciliationId

    if __name__ == "__main__":
        pytest.main()
