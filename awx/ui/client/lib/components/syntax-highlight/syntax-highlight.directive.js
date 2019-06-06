const templateUrl = require('~components/syntax-highlight/syntax-highlight.partial.html');

function atSyntaxHighlightController ($scope, AngularCodeMirror) {
    const vm = this;
    const varName = `${$scope.name}_codemirror`;

    function init () {
        if ($scope.disabled === 'true') {
            $scope.disabled = true;
        } else if ($scope.disabled === 'false') {
            $scope.disabled = false;
        }
        $scope.value = $scope.value || $scope.default;

        $scope.varName = varName;
        $scope[varName] = $scope.value;
        const codeMirror = AngularCodeMirror($scope.disabled);
        codeMirror.addModes({
            jinja2: {
                mode: $scope.mode,
                matchBrackets: true,
                autoCloseBrackets: true,
                styleActiveLine: true,
                lineNumbers: true,
                gutters: ['CodeMirror-lint-markers'],
                lint: true,
                scrollbarStyle: null,
            }
        });
        codeMirror.showTextArea({
            scope: $scope,
            model: varName,
            element: `${$scope.name}_codemirror`,
            lineNumbers: true,
            mode: $scope.mode,
        });

        $scope.$watch(varName, () => {
            $scope.value = $scope[varName];
        });
    }

    vm.name = $scope.name;
    vm.rows = $scope.rows || 6;
    if ($scope.init) {
        $scope.init = init;
    }
    angular.element(document).ready(() => {
        init();
    });
}

atSyntaxHighlightController.$inject = [
    '$scope',
    'AngularCodeMirror'
];

function atCodeMirrorTextarea () {
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl,
        controller: atSyntaxHighlightController,
        controllerAs: 'vm',
        scope: {
            disabled: '@',
            label: '@',
            labelClass: '@',
            tooltip: '@',
            tooltipPlacement: '@',
            value: '=',
            name: '@',
            init: '=',
            default: '@',
            rows: '@',
            mode: '@',
        }
    };
}

export default atCodeMirrorTextarea;
